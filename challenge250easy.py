#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 250 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/41hp6u/20160118_challenge_250_easy_scraping/
#
# 28 June 2016

from collections import defaultdict
from datetime import datetime, timedelta

import praw


def week_start(date):
    monday = date - timedelta(days=date.weekday())
    return monday.date()

def main():
    reddit = praw.Reddit(user_agent='Daily Programmer 250 Easy')
    dailyprogrammer = reddit.get_subreddit('dailyprogrammer')

    # download posts and sort by weeks
    week_posts = defaultdict(lambda: [])
    for post in dailyprogrammer.get_new(limit=50):
        post_date = datetime.utcfromtimestamp(int(post.created_utc))
        post.week_start = week_start(post_date)
        week_posts[post.week_start].append(post)

    # print header
    header =  'Easy | Intermediate | Hard | Weekly/Bonus\n'
    header += '-----|--------------|------|-------------\n'
    header += '| []() | []() | []() | **-** |'
    print header

    # print the posts
    row_template = '| [{easy_title}]({easy_url}) | [{interm_title}]({interm_url}) | [{hard_title}]({hard_url}) | **-** |'
    for week in sorted(week_posts.keys(), reverse=True):
        posts = week_posts[week]
        template_values = {
            'easy_title': '',
            'easy_url': '',
            'interm_title': '',
            'interm_url': '',
            'hard_title': '',
            'hard_url': ''
        }

        for post in posts:
            if '[easy]' in post.title.lower():
                template_values['easy_title'] = post.title.encode('ascii', 'replace')
                template_values['easy_url'] = post.url
            if '[intermediate]' in post.title.lower():
                template_values['interm_title'] = post.title.encode('ascii', 'replace')
                template_values['interm_url'] = post.url
            if '[hard]' in post.title.lower() or '[difficult]' in post.title.lower():
                template_values['hard_title'] = post.title.encode('ascii', 'replace')
                template_values['hard_url'] = post.url

        print row_template.format(**template_values)

main()
