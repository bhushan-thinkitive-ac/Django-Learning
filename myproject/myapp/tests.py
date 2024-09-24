from django.test import TestCase
from .models import Person

class PersonModelTest(TestCase):

    def setUp(self):
        """Create a Person instance for testing."""
        self.first_name = ''
        self.last_name = ''
        self.person = Person.objects.create(first_name=self.first_name, last_name=self.last_name)

    def test_person_values(self):
        """Test if the values in the database match the instance variables."""
        person_from_db = Person.objects.get(id=self.person.id)  # Retrieve the person from the database
        self.assertEqual(person_from_db.first_name, self.first_name)
        self.assertEqual(person_from_db.last_name, self.last_name)
