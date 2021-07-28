from rest_framework.test import APIClient

class TestPointsApi(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_calculate_point(self):
        url = reverse('/api/getClosestPath/')
        data = {
                    "string_points": "(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Points.objects.count(), 1)
        self.assertEqual(Points.objects.get().closestPoint, 1.4142135623730951)
