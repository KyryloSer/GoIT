from sqlalchemy.orm import Session
from src.models import NewsOne
from src.schemas.news import NewsBase, NewsUpdate


async def get_all_news(db: Session, skip, limit):
    all_news = db.query(NewsOne).offset(skip).limit(limit).all()
    return all_news


async def get_news(db: Session, news_id):
    one_news = db.query(NewsOne).filter(NewsOne.id == news_id).first()
    return one_news


async def create_news(db: Session, one_news: NewsBase):
    new_news = NewsOne(title=one_news.title, created=one_news.created, link_news=one_news.link_news,
                       views=one_news.views)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news


async def update_news(db: Session, news_id: int, u_one_news: NewsUpdate):
    one_news = db.query(NewsOne).filter(NewsOne.id == news_id).first()
    if one_news:
        one_news.title = u_one_news.title
        one_news.created = u_one_news.created
        one_news.link_news = u_one_news.link_news
        one_news.views = u_one_news.views
        db.commit()
    return one_news


async def delete_news(db: Session, news_id: int):
    one_news = db.query(NewsOne).filter(NewsOne.id == news_id).first()
    if one_news:
        db.delete(one_news)
        db.commit()
    return one_news
