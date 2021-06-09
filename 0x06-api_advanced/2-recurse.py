#!/usr/bin/python3

"""[RECURSE IT]
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url,
                       params={"count": count, "after": after},
                       headers={"User-Agent": "Omar"},
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    hot_ls = hot_list + [child['data']['title']
                         for child in req.json()['data']['children']]

    info = req.json()
    if not info.get("data").get("after"):
        return hot_ls

    return recurse(subreddit, hot_ls, info.get("data").get("count"),
                   info.get("data").get("after"))
