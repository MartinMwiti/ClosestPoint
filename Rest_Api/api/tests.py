from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from . models import Points

class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('/api/getClosestPath/')
        data = {
                    "string_points": "(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Points.objects.get().closestPoint, 1.4142135623730951)