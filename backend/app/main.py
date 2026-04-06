from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.routes import market, portfolio, options, strategy, screener, news, analytics, command
from app.websocket.endpoints import router as ws_router
from app.services.data_ingestion import start_market_data_simulator
from app.services.redis_client import redis_client
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables (in production use Alembic)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Connect to Redis
    await redis_client.connect()
    
    # Start background data ingestion
    asyncio.create_task(start_market_data_simulator())
    
    yield
    
    # Cleanup
    await redis_client.close()
    await engine.dispose()

app = FastAPI(title="AlgoFinex Terminal API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(market.router, prefix="/api/market", tags=["market"])
app.include_router(portfolio.router, prefix="/api/portfolio", tags=["portfolio"])
app.include_router(options.router, prefix="/api/options", tags=["options"])
app.include_router(strategy.router, prefix="/api/strategies", tags=["strategies"])
app.include_router(screener.router, prefix="/api/screener", tags=["screener"])
app.include_router(news.router, prefix="/api/news", tags=["news"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(command.router, prefix="/api/command", tags=["command"])
app.include_router(ws_router, prefix="/ws")

@app.get("/health")
async def health():
    return {"status": "ok"}
