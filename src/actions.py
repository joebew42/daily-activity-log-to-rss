from utils import daily_to_rss


class GetRssFromDailyUrl(object):
    def __init__(self, repository=None):
        self.__repository = repository

    def execute(self, url):
        daily = self.__repository.find_by(url)

        if daily is None:
            return 'ko', 'Unable to find a daily activity log for given URL: {}'.format(url)

        return 'ok', daily_to_rss(daily)
