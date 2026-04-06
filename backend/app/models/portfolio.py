from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    cash_balance = Column(Float, default=0.0)

class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    symbol = Column(String(20), nullable=False)
    quantity = Column(Float, nullable=False)
    avg_price = Column(Float, nullable=False)
    
    account = relationship("Account")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    symbol = Column(String(20))
    side = Column(String(4))  # buy/sell
    quantity = Column(Float)
    price = Column(Float)
    timestamp = Column(DateTime)
