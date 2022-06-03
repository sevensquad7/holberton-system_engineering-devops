#!/usr/bin/python3
""" Recursive function that queries the Reddit API """
import requests


def f_after(subreddit, hot_list=[], after=""):
    """initialization"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after is not None:
        with requests.Session() as res:
            data = res.get(url,
                           headers={'User-Agent': 'AgentMEGO'},
                           params={'after': after})
            if data.status_code != 200:
                return None
            after = data.json().get('data').get('after')
        hot_list += data.json().get('data').get('children')
        f_after(subreddit, hot_list, after)
    return (hot_list)


def recurse(subreddit, hot_list=[]):
    """initialization"""
    if subreddit is None or type(subreddit) is not str:
        return None

    return f_after(subreddit, hot_list, "")
