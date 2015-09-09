import unittest

from actions import GetRssFromDailyUrl
from mockito import mock, when
from rest import rest_app


class RestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = mock(GetRssFromDailyUrl)

        app = rest_app.create_with(cls.action)

        cls.client = app.test_client()

    def test_when_get_called_with_no_parameters_returns_bad_request(self):
        when(self.action).execute(None).thenReturn(('ko', 'ko message'))

        response = self.client.get('/rss/')

        self.assertEqual(400, response.status_code)
        self.assertEqual('ko message', response.data)

    def test_when_get_fails_returns_bad_request(self):
        when(self.action).execute('an_url').thenReturn(('ko', 'ko message'))

        response = self.client.get('/rss/?url=an_url')

        self.assertEqual(400, response.status_code)
        self.assertEqual('ko message', response.data)

    def test_when_get_succeeds_returns_rss(self):
        when(self.action).execute('an_url').thenReturn(('ok', 'xml+rss data'))

        response = self.client.get('/rss/?url=an_url')

        self.assertEqual('application/rss+xml', response.content_type)
        self.assertEqual(200, response.status_code)
        self.assertEqual('xml+rss data', response.data)

