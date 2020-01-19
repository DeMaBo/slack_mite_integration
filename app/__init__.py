from flask_api import FlaskAPI
from config.env import app_env
from app.slackhelper import SlackHelper

from flask import request, jsonify
from re import match
from app.actions import Actions

allowed_commands = [
    'show-entries',
    'show-entry',
    'create-entry',
    'delete-entry',
    'help',
]


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)

    # app.config.from_object(app_env[config_name])
    # app.config.from_pyfile('../../config/env.py')

    @app.route("/mite-integration", methods=["POST"])
    def mite_bot():
        """This route renders a hello world text"""
        command_text = request.args.get('text')
        print(command_text)
        print(type(command_text))
        slack_uid = request.data.get('user_id')
        print(allowed_commands[4])
        slackhelper = SlackHelper()
        # slack_user_info = slackhelper.user_info(slack_uid)
        actions = Actions(slackhelper)

        if command_text == 'help':
            response_body = actions.help()

        if command_text == ["show-entries", "show-entry"]:
            response_body = actions.my_entries()

        if command_text == 'create-entry':
            response_body = actions.create_entry()

        if command_text == 'delete-entry':
            response_body = actions.delete_entry()

        # if command_text not in allowed_commands:
        #     response_body = {'text': 'Invalid Command Sent - `/miteintegration help` for available commands'}

        response = jsonify(response_body)
        response.status_code = 200
        return response

    return app
