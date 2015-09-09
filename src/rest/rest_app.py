from actions import GetRssFromDailyUrl
from infrastructure import HTTPDailyRepository
from rest import resources
from rest.utils import AppBuilder


def create():
    repository = HTTPDailyRepository()
    return create_with(GetRssFromDailyUrl(repository=repository))


def create_with(get_rss_from_daily_url=None):
    return AppBuilder().with_url_rule('/rss/', None, resources.rss(get_rss_from_daily_url), methods=['GET']).build()
