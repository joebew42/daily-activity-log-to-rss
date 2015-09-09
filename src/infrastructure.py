import xml.etree.ElementTree as et

from models import DailyRepository, Daily, DailyEntry
import requests


class HTTPDailyRepository(DailyRepository):
    def find_by(self, url):
        body = self.__body_from(url)
        events = self.__xml_from(body)

        if events is None:
            return None

        daily = Daily(url=url)

        for event in events:
            daily.add_entry(self.__daily_entry_from(event))

        return daily

    def __daily_entry_from(self, event):
        action = event.find('action')
        entry = DailyEntry(date=event.attrib['date'], type=action.attrib['type'], subject=action.text)
        references = event.find('references')
        if references is not None:
            for reference in references:
                entry.add_reference(source=reference.attrib['src'], type=reference.attrib['type'])
        return entry

    def __body_from(self, url):
        try:
            response = requests.get(url)
            return response.text.encode('utf-8')
        except Exception:
            return None

    def __xml_from(self, body):
        try:
            return et.fromstring(body)
        except Exception:
            return None
