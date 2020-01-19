import configparser
import slack
from app.models import Mite
import os

from config import get_env

cfg_slack = configparser.ConfigParser()

cfg_slack.read('app/slack.conf')

slack_token = cfg_slack['DEFAULT']['SLACK_TOKEN']
slack_channel = cfg_slack['DEFAULT']['SLACK_CHANNEL']
slack_username = cfg_slack['DEFAULT']['SLACK_USER']

# cfg_mite = configparser.ConfigParser()
# cfg_mite.read('app/mite.conf')
#
# mite_team_url = cfg_mite['DEFAULT']['TEAM_URL']
# mite_api_key = cfg_mite['DEFAULT']['API_KEY']
#
# mite = Mite(mite_team_url, mite_api_key)


# client = slack.WebClient(token=slack_token)
#
# response = client.chat_postMessage(
#     channel="#{}".format(slack_channel),
#     text="Hello from your app! :tada: OIDA! {}".format(mite.get_me())
#     # user=slack_username
# )
# assert response["ok"]
# assert response["message"]["text"] == "Hello from your app! :tada: OIDA!"


class SlackHelper:

    def __init__(self):
        self.slack_token = slack_token  # get_env('SLACK_TOKEN')
        self.slack_client = slack.WebClient(self.slack_token)
        self.slack_channel = slack_channel  # get_env('SLACK_CHANNEL')

    def post_message(self, msg, recipient):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=recipient,
            test=msg,
            as_user=True
        )

    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
            username='miteintegration',
            parse='full',
            as_user=False
        )

    # def user_info(self, uid):
    #     return self.slack_client.api_call(
    #         "users.info",
    #         user=uid,
    #         token=self.slack_token
    #     )
