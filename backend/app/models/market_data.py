from sqlalchemy import Column, String, Float, DateTime, Integer, Index
from app.database import Base
from datetime import datetime

class MarketData(Base):
    __tablename__ = "market_data"
    
    symbol = Column(String(20), primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    
    __table_args__ = (
        Index("ix_market_data_symbol_timestamp", "symbol", "timestamp"),
        {"postgresql_hypertable": {"time_column_name": "timestamp", "partitioning_column": "symbol"}}
    )
