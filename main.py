from hwswap_notifier import notify_keywords
from os import environ

def main():
    notify_keywords(environ.get('TWILIO_NUMBER'), environ.get('PERSONAL_NUMBER'))

if __name__ == '__main__':
    main()
