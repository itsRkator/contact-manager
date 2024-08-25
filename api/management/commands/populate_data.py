from django.core.management.base import BaseCommand
from faker import Faker
from sqlalchemy.orm import sessionmaker
from api.sqlalchemy import engine
from api.models import Contact


class Command(BaseCommand):
    help = "Populate the database with dummy data"

    def handle(self, *args, **kwargs):
        db_session = sessionmaker(bind=engine)()
        fake = Faker()

        for _ in range(100):
            contact = Contact(
                name=fake.name(),
                phone_number=fake.phone_number(),
                is_spam=fake.boolean(),
            )
            db_session.add(contact)

        db_session.commit()
        self.stdout.write(self.style.SUCCESS("Successfully populate the database"))
