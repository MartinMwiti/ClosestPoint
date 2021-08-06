from . test_setup import TestSetUp
import pdb # python debugger

class TestViews(TestSetUp):
    
    def test_calcClosestPoints_with_incorrect_points(self):
        data = {
            "string_points": "John Doe"
        }
        # checks/assertions
        res = self.client.post(self.calculateClosestDistance_url, data)      
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)
        
    def test_calcClosestPoints_with_correct_points(self):
        data = {
            "string_points": "(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)"
        }
        # checks/assertions
        res = self.client.post(self.calculateClosestDistance_url, data)      
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)