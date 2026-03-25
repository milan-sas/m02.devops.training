import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"city": "London", "temp": 25, "condition": "sunny", "humidity": 60}

        with patch("weather_service.api_client.requests.get", return_value=mock_response):
            result = weather_service.get_weather("London")
            self.assertEqual(result["temp"], 25)
            self.assertEqual(result["condition"], "sunny")

    def test_get_weather_api_error(self):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("500 Server Error")

        with patch("weather_service.api_client.requests.get", return_value=mock_response):
            with self.assertRaises(Exception):
                weather_service.get_weather("Paris")

    def test_get_weather_timeout(self):
        import requests as req
        with patch("weather_service.api_client.requests.get", side_effect=req.Timeout("Request timed out")):
            with self.assertRaises(req.Timeout):
                weather_service.get_weather("Berlin")

    @patch("weather_service.api_client.requests.get")
    def test_get_forecast_with_patch(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {"day": 1, "temperature": 21, "condition": "sunny"},
            {"day": 2, "temperature": 19, "condition": "rainy"},
        ]
        mock_get.return_value = mock_response

        result = weather_service.get_forecast("Madrid", days=2)

        mock_get.assert_called_once()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["condition"], "sunny")

    @patch("weather_service.api_client.datetime")
    def test_get_current_time_mocked(self, mock_datetime):
        mock_datetime.now.return_value.hour = 9
        self.assertEqual(weather_service.get_greeting_based_on_time(), "Good morning")

        mock_datetime.now.return_value.hour = 14
        self.assertEqual(weather_service.get_greeting_based_on_time(), "Good afternoon")

        mock_datetime.now.return_value.hour = 20
        self.assertEqual(weather_service.get_greeting_based_on_time(), "Good evening")


if __name__ == "__main__":
    unittest.main()
