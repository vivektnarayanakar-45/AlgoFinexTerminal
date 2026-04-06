from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.database import Base

class OptionContract(Base):
    __tablename__ = "option_contracts"
    id = Column(Integer, primary_key=True)
    symbol = Column(String(20), nullable=False)  # underlying
    strike = Column(Float, nullable=False)
    expiry = Column(DateTime, nullable=False)
    option_type = Column(String(4))  # call/put
    implied_vol = Column(Float, default=0.2)
    last_price = Column(Float, nullable=True)
