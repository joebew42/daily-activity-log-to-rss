from flask import request, Response


def rss(get_rss_from_daily_url=None):
    def handler():
        url = request.args.get('url')

        status, data = get_rss_from_daily_url.execute(url)

        if status == 'ko':
            return Response(data, status=400)

        return Response(data, content_type='application/rss+xml')

    return handler
