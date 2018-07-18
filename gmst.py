# _*_ coding: UTF-8 _*_
import re

import slackweb
import gmail

GMAIL_USERNAME = 'xxx@xxx.com'
GMAIL_PASSWORD = 'xxxx'

MY_EMAIL = 'xxx@xxx.com'
KEYWORDS_REGEX = re.compile(r"ping", re.IGNORECASE)
#match = KEYWORDS_REGEX.search(mail.body)

slack = slackweb.Slack(url="https://hooks.slack.com/services/xxxxxxxxxxxxxxxx")

def main():
    g = gmail.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    for mail in g.inbox().mail(unread=True, prefetch=True):
        match = KEYWORDS_REGEX.search(mail.subject)
        if match:
            #print match
            slack.notify(text="PING_NG")
        else:
            slack.notify(text="Tails")

if __name__ == '__main__':
    main()

