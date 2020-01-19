from flask import Flask
from flask import request
from app.models import Mite
import requests
import json

app = Flask(__name__)

import configparser

config = configparser.ConfigParser()
config.read('mite.conf')

mite_team_url = config['DEFAULT']['TEAM_URL']
mite_api_key = config['DEFAULT']['API_KEY']

mite = Mite(mite_team_url, mite_api_key)


@app.route('/', methods=['POST'])
def get_user():
    data = request.json
    if data['event']['type'] == "app_mention":
        user_text = data['event']['text']
    user = data['event']['user']
    webhook_url = 'https://{}'.format('test')
    slack_data = {"text": "How can I help you ?"}
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    return ('', 204)
    # return mite.get_account()


if __name__ == '__main__':
    app.run()
