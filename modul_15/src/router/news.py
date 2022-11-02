from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query, Path
from sqlalchemy.orm import Session

from db.connect import get_db
from src.repository import news
from src.schemas.news import NewsBase, NewsResponse, NewsUpdate

router = APIRouter(prefix='/news', tags=['news'])


@router.get("/", response_model=List[NewsResponse])
async def get_all_news(db: Session = Depends(get_db), skip: int = 0,
                       limit: int = Query(10, ge=1, le=100, description="How news you get")):
    all_news = await news.get_all_news(db, skip, limit)
    return all_news


@router.get("/{news_id}", response_model=NewsResponse)
async def get_news(news_id: int = Path(ge=1, description="The ID of the news"), db: Session = Depends(get_db)):
    one_news = await news.get_news(db, news_id)
    if one_news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'News with ID {news_id} not found')
    return one_news


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NewsResponse)
async def create_news(one_news: NewsBase, db: Session = Depends(get_db)):
    print(one_news)
    one_news = await news.create_news(db, one_news)
    return one_news


@router.put("/{new_id}", response_model=NewsResponse)
async def update_news(news_id, one_news: NewsUpdate, db: Session = Depends(get_db)):
    one_news = await news.update_news(db, news_id, one_news)
    if one_news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'News with ID {news_id} not found')
    return one_news


@router.delete("/{new_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(news_id, db: Session = Depends(get_db)):
    one_news = await news.delete_news(db, news_id)
    if one_news is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'News with ID {news_id} not found')
    return one_news
