from rest_framework import serializers
from .models import Provider, Client, Transaction, Category

class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Client
        fields = ('id', 'username', 'number')

class ProviderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Provider
        fields = ('id', 'firstname', 'lastname', 'email')

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transaction
        fields = ('id', 'start_time', 'finish_time', 'service_cost')
        read_only_fields = ('date_created', 'date_modified')

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'name')
