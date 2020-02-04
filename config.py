import praw

from os import environ
from twilio.rest import Client


def reddit_config():
    reddit_client_id = environ.get('REDDIT_CLIENT_ID')
    reddit_client_secret = environ.get('REDDIT_CLIENT_SECRET')
    reddit_user_agent = environ.get('REDDIT_USER_AGENT')
    reddit_username = environ.get('REDDIT_USERNAME')
    reddit_password = environ.get('REDDIT_PASSWORD')
    return praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent,
                         username=reddit_username,
                         password=reddit_password)


def twilio_config():
    twilio_account_sid = environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = environ.get('TWILIO_AUTH_TOKEN')
    return Client(twilio_account_sid, twilio_auth_token)
