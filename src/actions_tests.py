import unittest

from actions import GetRssFromDailyUrl
from mockito import mock, when
from models import DailyRepository, DailyEntry, Daily


class GetRssFromDailyUrlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repository = mock(DailyRepository)

        cls.action = GetRssFromDailyUrl(cls.repository)

    def test_when_daily_is_not_found_returns_ko(self):
        when(self.repository).find_by('an url').thenReturn(None)

        status, message = self.action.execute('an url')

        self.assertEqual('ko', status)
        self.assertEqual('Unable to find a daily activity log for given URL: an url', message)

    def test_when_daily_is_found_returns_rss(self):
        daily = Daily(url='an url')
        daily_entry = DailyEntry(date='2015-12-30', type='reading', subject='a book about trees')
        daily_entry.add_reference(source='http://somewhere', type='source')
        daily.add_entry(daily_entry)

        when(self.repository).find_by('an url').thenReturn(daily)

        status, message = self.action.execute('an url')

        self.assertEqual('ok', status)
        self.assertTrue(message.startswith("<rss "))
