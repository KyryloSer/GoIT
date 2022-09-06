from sqlalchemy.orm import joinedload

from src.db import session
from models import Adress, Person


def get_persons() -> None:
    p = session.query(Person).all()
    for i in p:
        print(i.id, i.last_name, i.first_name, i.date_birth)


def get_adress() -> None:
    ad = session.query(Adress).all()
    for a in ad:
        print(f'id: {a.id} email: {a.email} a.phone: {a.phone} address: {a.address}  person_id: {a.person_id}')


def get_adress_person() -> None:
    ap = session.query(Adress).options(joinedload('person')).all()
    for a in ap:
        print(f"{a.id} {a.email} {a.person.first_name}")

if __name__ == '__main__':
    # get_persons()
    # get_adress()
    get_adress_person()
