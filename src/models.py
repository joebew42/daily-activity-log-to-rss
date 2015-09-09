from datetime import datetime


class DailyRepository(object):
    def find_by(self, url):
        raise NotImplementedError


class Daily(object):
    def __init__(self, url):
        self.url = url
        self.__entries = []

    def add_entry(self, daily_entry):
        self.__entries.append(daily_entry)

    def entries(self):
        return sorted(self.__entries, key=lambda entry: entry.date, reverse=True)

    def __eq__(self, other):
        return self.url == other.url and \
            self.entries() == other.entries()


class DailyEntry(object):
    def __init__(self, date, type, subject):
        self.date = date
        self.type = type
        self.subject = subject
        self.references = []

    def add_reference(self, source, type):
        self.references.append(DailyEntryReference(source, type))

    def date_rfc2822(self):
        try:
            date = datetime.strptime(self.date, "%Y-%m-%d").date()
            return date.strftime("%a, %d %b %Y %H:%M:%S +0000")
        except ValueError:
            return None

    def __str__(self):
        return "{} {}: {}".format(self.date, self.type, self.subject)

    def __eq__(self, other):
        return self.date == other.date and \
            self.type == other.type and \
            self.subject == other.subject and \
            self.references == other.references


class DailyEntryReference(object):
    def __init__(self, source, type):
        self.source = source
        self.type = type

    def __eq__(self, other):
        return self.source == other.source and \
            self.type == other.type
