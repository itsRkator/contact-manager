from sqlalchemy import Column, Integer, String, Boolean
from .sqlalchemy import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    is_spam = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"<Contact(name={self.name}, phone_number={self.phone_number})>"
        )
