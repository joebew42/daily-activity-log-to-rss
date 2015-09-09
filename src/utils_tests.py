import unittest

from models import Daily, DailyEntry
from utils import exclude_tag, daily_to_rss


class DailyToRssTest(unittest.TestCase):
    def test_daily_to_rss_feed(self):
        daily = Daily(url='an url')

        daily_entry = DailyEntry(date='2015-12-28', type='reading', subject='a book about bonsai')
        daily.add_entry(daily_entry)

        daily_entry = DailyEntry(date='2015-12-30', type='studying', subject='a book about trees')
        daily_entry.add_reference(source='http://somewhere', type='source')
        daily_entry.add_reference(source='http://somewhere/blog.html', type='blog')
        daily.add_entry(daily_entry)

        expected_rss = '''<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title>Daily Activity Log: an url</title>
    <link>an url</link>
    <description>RSS feed generated from: an url</description>
    <docs>http://www.rssboard.org/rss-specification</docs>
    <generator>python-feedgen</generator>
    <language>en</language>
    <item>
      <title>studying: a book about trees</title>
      <description>&lt;a href=\'http://somewhere\'&gt;source&lt;/a&gt;&lt;br/&gt;&lt;a href=\'http://somewhere/blog.html\'&gt;blog&lt;/a&gt;&lt;br/&gt;</description>
      <pubDate>Wed, 30 Dec 2015 00:00:00 +0000</pubDate>
    </item>
    <item>
      <title>reading: a book about bonsai</title>
      <pubDate>Mon, 28 Dec 2015 00:00:00 +0000</pubDate>
    </item>
  </channel>
</rss>
'''

        rss = daily_to_rss(daily)

        self.assertEqual(expected_rss, exclude_tag('lastBuildDate', rss))
