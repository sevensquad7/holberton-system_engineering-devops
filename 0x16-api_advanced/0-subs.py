#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """initialization"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    User_Agent = 'AgentMEGO'
    header = {'User-Agent': User_Agent}
    with requests.Session() as res:
        data = res.get(url, headers=header)
        if data.status_code != 200:
            return 0
    return data.json().get('data', {}).get('subscribers', 0)
