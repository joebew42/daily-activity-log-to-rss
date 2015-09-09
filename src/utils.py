from feedgen.feed import FeedGenerator
import re


def exclude_tag(tag, message):
    return re.sub(r"\s+<{0}>.+</{0}>".format(tag), '', message)


def daily_to_rss(daily):
    feed_generator = FeedGenerator()
    feed_generator.id(daily.url)
    feed_generator.link(href=daily.url, rel='alternate')
    feed_generator.description(u'RSS feed generated from: {}'.format(daily.url))
    feed_generator.title(u'Daily Activity Log: {}'.format(daily.url))
    feed_generator.language('en')

    for entry in daily.entries():
        feed_entry = feed_generator.add_entry()
        feed_entry.title(u'{}: {}'.format(entry.type, entry.subject))
        feed_entry.description(description=rss_description_from(entry))
        feed_entry.pubdate(entry.date_rfc2822())

    return feed_generator.rss_str(pretty=True)


def rss_description_from(daily_entry):
    if not len(daily_entry.references):
        return None

    content = ""
    for reference in daily_entry.references:
        content += "<a href='{}'>{}</a><br/>".format(reference.source, reference.type)

    return content
