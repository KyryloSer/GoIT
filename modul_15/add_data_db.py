from datetime import datetime
from db.connect import SessionLocal
from src.models import NewsOne
from get_data_from_sites import get_data

data_for_db = get_data()
db = SessionLocal()
for data in data_for_db:
    time_create = data['created']
    news = NewsOne(title=data['title'], created=datetime(*data['created']), link_news=data['link_news'],
                   views=data['views'])
    db.add(news)
    db.commit()
db.close()
