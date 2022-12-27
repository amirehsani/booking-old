from django.test import SimpleTestCase, override_settings
from django.urls import resolve, reverse
from air.views import *


class TestURLs(SimpleTestCase):

    @override_settings(URL='airlines/')
    def test_airline_url_is_resolved(self):
        url = reverse('Airlines List')
        print(resolve(url))
        self.assertEquals(resolve(url).func, AirLineDisplay)

    @override_settings(URL='airports/')
    def test_airport_url_is_resolved(self):
        url = reverse('Airports List')
        print(resolve(url))
        self.assertEquals(resolve(url).func, AirportDisplay)
