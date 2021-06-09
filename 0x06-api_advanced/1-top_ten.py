#!/usr/bin/python3

"""[TOP TEN]
"""


def top_ten(subreddit):
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url,
                       headers={'User-Agent': 'Omar'},
                       allow_redirects=False)

    if req.status_code != 200:
        print('None')
    else:
        [print(child['data']['title'])
         for child in req.json()['data']['children']]
