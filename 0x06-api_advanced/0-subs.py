#!/usr/bin/python3

"""[SUBREDDIT]
"""


def number_of_subscribers(subreddit):
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url,
                       headers={'User-Agent': 'Omar'},
                       allow_redirects=False)

    if req.status_code != 200:
        return 0
    return req.json()['data']['subscribers']
