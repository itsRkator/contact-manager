from django.urls import path
from api.views import ContactListView, ContactDetailView

urlpatterns = [
    path("contacts/", ContactListView.as_view(), name="contact-list"),
    path("contacts/<int:pk>", ContactDetailView.as_view(), name="contact-detail"),
]
