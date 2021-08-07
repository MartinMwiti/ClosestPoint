from . test_setup import TestSetUp
import pdb # python debugger

class TestViews(TestSetUp):
    
    def test_calcClosestPoints_with_incorrect_points(self):
        data = {
            "string_points": "John Doe"
        }
        # checks/assertions
        res = self.client.post(self.calculateClosestDistance_url, data, format="json")      
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)
        
    def test_calcClosestPoints_with_correct_points(self):
        data = {
            "string_points": "(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)"
        }
        # checks/assertions
        res = self.client.post(self.calculateClosestDistance_url, data, format="json")      
        # pdb.set_trace()
        self.assertEqual(res.data['point'], data['string_points']) # whatever is coming back from DB is same as the keyed points
        self.assertEqual(res.status_code, 200)
        
    def test_getClosestPoints_list(self):
        # checks/assertions
        res = self.client.get(self.getClosestDistance_url, format="json")      
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)