from mongoengine import *


class Info(Document):
    first_name = StringField(max_length=120, min_length=1, required=True)
    last_name = StringField(max_length=120, min_length=1, required=True)
    date_birth = DateTimeField(required=True)
    email = StringField(required=False)
    phone = StringField(required=True)
    adress = StringField(required=True)
