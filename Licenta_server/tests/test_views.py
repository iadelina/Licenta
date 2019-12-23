from django.test import TestCase
from interface.views import render_info_page
from django.urls import reverse
import datetime
import unittest
import mock

class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    #def test_view_url_accessible_by_name(self):
     #   response = self.client.get(reverse('authors'))
      #  self.assertEqual(response.status_code, 200)

    def test_view_info_page_url_exists_at_desired_location(self):
        response = self.client.get('/interface/render_info_page')
        self.assertEqual(response.status_code, 302)

    def test_view_control_page_url_exists_at_desired_location(self):
        response = self.client.get('/interface/render_control_page')
        self.assertEqual(response.status_code, 302)

   # @mock.patch('interface.led.IndoorLed.get_current_state', return_value='STINS')
   # def test_view_control_page_returns_expected_led_state(self):
   #     response = self.client.get('/interface/render_control_page')
 # with mock.patch("interface.led.IndoorLed.get_current_state") as mock_object:
       #     mock_object.return_value = 'STINS'

