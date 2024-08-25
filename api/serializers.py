from rest_framework import serializers


class ContactSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    is_spam = serializers.BooleanField()
