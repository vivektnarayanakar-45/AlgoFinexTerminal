from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base

class NewsArticle(Base):
    __tablename__ = "news_articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    content = Column(Text)
    source = Column(String(100))
    published_at = Column(DateTime)
    sentiment_score = Column(Float)  # -1 to 1
    symbols_mentioned = Column(String(500))  # comma separated
