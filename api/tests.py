from django.test import TestCase

# Create your tests here.
from .models import Provider, Client, Transaction, Category

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client_name = "Martin"
        self.client_phone = "0726377489"
        self.client = Client(username=self.client_name, number=self.client_phone)

    def test_model_can_create_objects(self):
        """Test the  models can create a objects."""
        old_count = Client.objects.count()
        self.client.save()
        new_count = Client.objects.count()
        self.assertNotEqual(old_count, new_count)
