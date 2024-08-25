from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Contact
from api.serializers import ContactSerializers
from api.sqlalchemy import get_db

# Create your views here.


class ContactListView(generics.ListCreateAPIView):
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db = next(get_db())
        return db.query(Contact).all()

    def perform_create(self, serializer):
        db = next(get_db())
        contact = Contact(**serializer.validated_data)
        db.add(contact)
        db.commit()


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        db = next(get_db())
        return db.query(Contact).filter(Contact.id == self.kwargs["pk"]).first()

    def perform_update(self, serializer):
        db = next(get_db())
        db.query(Contact).filter(Contact.id == serializer.instance.id).update(
            serializer.validated_data
        )
        db.commit()

    def perform_destroy(self, instance):
        db = next(get_db())
        db.query(Contact).filter(Contact.id == instance.id).delete()
        db.commit()
