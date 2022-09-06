import random
from faker import Faker
from src.db import session
from models import Adress, Person


fake = Faker()

def create_preson():
    for _ in range(1, 6):
        person = Person(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(person)
    session.commit()


def create_adress():
    for _ in range(1, 7):
        adress = Adress(
            email=fake.ascii_email(),
            phone=fake.phone_number(),
            address=fake.street_address(),
            added_at=fake.date_of_birth(),
            person_id=random.randrange(1,5)
        )
        session.add(adress)
    session.commit()


if __name__ == '__main__':
    # create_preson()
    # create_adress()
    p = session.query(Person).all()
    for i in p:
        print(i.id, i.last_name, i.first_name)

