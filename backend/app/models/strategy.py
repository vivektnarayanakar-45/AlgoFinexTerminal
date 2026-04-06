from sqlalchemy import Column, Integer, String, Boolean, Float, JSON, DateTime
from app.database import Base

class AlgoStrategy(Base):
    __tablename__ = "algo_strategies"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(500))
    is_active = Column(Boolean, default=False)
    parameters = Column(JSON)  # e.g. {"fast_ma": 10, "slow_ma": 30}
    current_pnl = Column(Float, default=0.0)
    last_update = Column(DateTime)
