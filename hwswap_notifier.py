import config
import datetime
import requests

from constants import KEYWORDS

REDDIT = config.reddit_config()
TWILIO = config.twilio_config()

def check_new_posts(sub, limit=25, flair=None, timeframe=datetime.timedelta(minutes=10)):
    if flair:
        return {post for post in REDDIT.subreddit(sub).new(limit=limit)
                if post.link_flair_text == flair
                and datetime.datetime.now() - datetime.datetime.fromtimestamp(post.created_utc) < timeframe}
    else:
        return {post for post in REDDIT.subreddit(sub).new(limit=limit)
                if datetime.datetime.now() - datetime.datetime.fromtimestamp(post.created_utc) < timeframe}


def notify_keywords(twilio_number, recipient):
    new_posts = check_new_posts('hardwareswap', flair='SELLING', timeframe=datetime.timedelta(hours=48))
    matches = {}
    for post in new_posts:
        for key in set(KEYWORDS.keys()):
            if key in post.title.lower():
                keyword = matches.setdefault(KEYWORDS[key], set())
                keyword.add(post.url)

    if len(matches) > 0:
        info = "We have found a match!\n"
        for keyword, posts in matches.items():
            info += f'{keyword}: '
            for link in posts:
                info += f'{link}\n'
        message = TWILIO.messages.create(body=info,
                                         from_=twilio_number,
                                         to=recipient)
        requests.post(f"https://api.twilio.com/2010-04-01/Accounts/{message.account_sid}/Messages.json")
    else:
        print("No keywords found")
