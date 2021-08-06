from rest_framework.test import APITestCase
from django.urls import reverse # takes a view name & gives a path to the route

# Run all methods on starting the test
class TestSetUp(APITestCase):
    
    def setUp(self):
        self.getClosestDistance_url = reverse('getClosestDistance')
        self.calculateClosestDistance_url = reverse('calcClosestDistance')
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()