import datetime

from pydantic import BaseModel, Field


class NewsBase(BaseModel):
    title: str = Field(max_length=250)
    created: datetime.datetime
    link_news: str = Field(max_length=200, description='The link is on the article')
    views: str = Field(max_length=10, description='It is the number of views of the article')


class NewsUpdate(NewsBase):
    pass


class NewsResponse(NewsBase):
    id: int

    class Config:
        orm_mode = True
