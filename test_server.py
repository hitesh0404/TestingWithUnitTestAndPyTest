import unittest
import server
import requests
from fastapi.testclient import TestClient
from server import app
# class TestServer(unittest.TestCase):
#     def setUp(self):
#         print("before each test case")
#     def test_server(self):
#         d = server.get_data(1)
#         assert 200 == requests.get("http://localhost:8000/get_data/1").status_code

#     #     assert d == {
#     #     "id":1,
#     #     "name":"Rupam",
#     #     "subject":"AI"
#     # }
#     '''def test_post(self):
#         d = server.post_data()
#         assert 200 == requests.status_codes'''
class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client=TestClient(app)
    def test_get(self):
        assert 200 == requests.get("http://localhost:8000/get_data/1").status_code

    def test_post(self):
        data = {
                "id": "1",
                "name":"Rupam",
            }
        request=requests.post("http://localhost:8000/post_data",json=data)
        print(request.json())
        data = request.json()
        assert data["id"]=="1"
        assert data["name"]=="Rupam"

        
if __name__ == "__main__":
    unittest.main()
        
        