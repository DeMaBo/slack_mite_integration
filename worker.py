from app.actions import Actions
from app.slackhelper import SlackHelper


def main():
    slackhelper = SlackHelper()
    actions = Actions(slackhelper)
    actions.notify_channel()


if __name__ == '__main__':
    main()
