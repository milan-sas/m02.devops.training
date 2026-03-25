import unittest
from app import app


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.data.decode())

    def test_add_endpoint(self):
        response = self.client.post("/add", json={"a": 5, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 8)

    def test_subtract_endpoint(self):
        response = self.client.post("/subtract", json={"a": 10, "b": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 6)

    def test_multiply_endpoint(self):
        response = self.client.post("/multiply", json={"a": 3, "b": 7})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 21)

    def test_divide_endpoint(self):
        response = self.client.post("/divide", json={"a": 20, "b": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 5)

    def test_divide_by_zero(self):
        response = self.client.post("/divide", json={"a": 10, "b": 0})
        self.assertEqual(response.status_code, 400)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_history_endpoint(self):
        self.client.post("/add", json={"a": 1, "b": 2})
        response = self.client.get("/history")
        self.assertEqual(response.status_code, 200)
        history = response.get_json()
        self.assertIsInstance(history, list)
        self.assertGreater(len(history), 0)
        last = history[-1]
        self.assertIn("operation", last)
        self.assertIn("result", last)


if __name__ == "__main__":
    unittest.main()
