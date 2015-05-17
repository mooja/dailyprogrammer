#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 112 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/137f7t/11142012_challenge_112_easyget_that_url/
#
# May.16.2015


import re
import argparse

from urlparse import urlparse


def is_wellformed(url):
    # copied from django's url validation regex
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    m = re.match(regex, url)
    return bool(m)


def iter_query_items(urlstring):
    url_obj = urlparse(urlstring, allow_fragments=False)

    for key, val in (query.split('=', 1)
                     for query in url_obj.query.split('&')
                         if query):
        yield key, val


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('url', help='URL ')
    args = arg_parser.parse_args()

    if not is_wellformed(args.url):
        print 'The given URL is invalid'
        return

    if urlparse(args.url).query:
        for query_key, query_val in iter_query_items(args.url):
            print '{}: "{}"'.format(query_key, query_val)


if __name__ == '__main__':
    main()
