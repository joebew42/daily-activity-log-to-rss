import unittest

import httpretty
from infrastructure import HTTPDailyRepository
from models import Daily, DailyEntry


class HTTPDailyRepositoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repository = HTTPDailyRepository()

    @httpretty.activate
    def test_pass(self):
        httpretty.register_uri(httpretty.GET, AN_URL, body=A_VALID_XML)

        daily = self.repository.find_by(AN_URL)

        self.assertEqual(self.full_daily(), daily)

    @httpretty.activate
    def test_fail_with_not_valid_xml(self):
        httpretty.register_uri(httpretty.GET, AN_URL, body=A_NOT_VALID_XML)

        daily = self.repository.find_by(AN_URL)

        self.assertEqual(None, daily)

    def test_fail_with_connection_timeout_exception(self):
        daily = self.repository.find_by(AN_URL)

        self.assertEqual(None, daily)

    def full_daily(self):
        daily = Daily(url=AN_URL)
        first_entry = DailyEntry("2015-06-23", "trying", "My daily activity log")
        first_entry.add_reference("http://somewhere.internet/page.html", "source")
        second_entry = DailyEntry("2015-06-20", "reading", "A new book")
        second_entry.add_reference("http://somewhere.internet/page2.html", "source")
        second_entry.add_reference("http://somewhere.internet/page2.html", "other source")
        third_entry = DailyEntry("2015-06-18", "watching", "A movie")
        daily.add_entry(first_entry)
        daily.add_entry(second_entry)
        daily.add_entry(third_entry)
        return daily


AN_URL = 'http://whatever-daily-log-url.somewhere'

A_VALID_XML = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="events.xsl"?>
<events>
  <event date="2015-06-23">
    <action type="trying">My daily activity log</action>
    <references>
      <reference src="http://somewhere.internet/page.html" type="source" />
    </references>
  </event>
  <event date="2015-06-20">
    <action type="reading">A new book</action>
    <references>
      <reference src="http://somewhere.internet/page2.html" type="source" />
      <reference src="http://somewhere.internet/page2.html" type="other source" />
    </references>
  </event>
  <event date="2015-06-18">
    <action type="watching">A movie</action>
  </event>
</events>
"""

A_NOT_VALID_XML = "<asd"
