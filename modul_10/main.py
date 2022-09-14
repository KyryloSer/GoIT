from faker import Faker
from models.models import Info
import connect


def data_in_db():
    fake = Faker()

    for _ in range(10):
        info = Info(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_birth=fake.date_of_birth(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            adress=fake.street_address()
        ).save()


def data_from_db():
    info_all = Info.objects()
    for i in info_all:
        print(i.id, i.first_name, i.last_name)


if __name__ == "__main__":
    # data_in_db()
    data_from_db()
