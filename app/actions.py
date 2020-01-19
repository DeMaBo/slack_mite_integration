from config import get_env
import time
from datetime import datetime, date, timedelta


class Actions:

    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper

    def help(self):
        """
        Return the Available commands in the system and their usage format
        """
        return {
            'text': 'Available Commands: \n `/mite-integration show-entries e.g. /mite-integration show-entries \n To show Mite entries already booked.\n'
                    ' \n `/mite-integration create-entry [date][Project][Service_Number][Minutes][Description] \n'
                    '\n `/mite-integration help` \n This help information \n \n DeMabo Ver: 1.0'}

    def __convert_to_date(self, date_string):
        today = date.today()
        if date_string == 'today':
            return today
        elif date_string == 'yesterday':
            return today - timedelta(days=1)
        elif date_string == 'tomorrow':
            return today + timedelta(days=1)
        else:
            return today

    def _perform_send_action(self, task_cells):
        recipient = self.user_info['user']['id']
        for index, row in enumerate(task_cells):
            text_detail = (
                '*Task #{} for {}:* \n\n'
                '*Hey {},* Today is the check-in day for your writeup titled\n'
                '`{}`.\n\n'
                'Whats the status of the article?\n'
                'PS: Please reply to this thread, the managers will review and reply you ASAP').format(
                str(index + 1), row['Next Check-In'], row['Name'],
                row['Most Recent Learning Experience you\'d like to write about'])
            self.slackhelper.post_message(text_detail, recipient)
        return None

    def __num_suffix(self, check_in_date):
        """
        Strip the date suffix and return the date
        Before comparing the date
        """
        date_value = str(check_in_date).split(' ')
        day_value = date_value[0][:-2]
        date_value[0] = day_value
        return ' '.join(date_value)

    def __perform_send_action(self, task_cells):
        recipient = self.user_info['user']['id']
        for index, row in enumerate(task_cells):
            text_detail = (
                '*Task #{} for {}:* \n\n'
                '*Hey {},* Today is the check-in day for your writeup titled\n'
                '`{}`.\n\n'
                'Whats the status of the article?\n'
                'PS: Please reply to this thread, the managers will review and reply you ASAP').format(
                str(index + 1), row['Next Check-In'], row['Name'],
                row['Most Recent Learning Experience you\'d like to write about'])
            self.slackhelper.post_message(text_detail, recipient)
        return None

    def notiy_channel(self):
        while True:
            current_time = datetime.now()
            current_hour = current_time.hour
            current_minute = current_time.minute

            if current_hour - 8 > 0:
                sleep_time = 24 - current_hour + 8 - (current_minute / 60)
            elif current_hour - 8 < 0:
                sleep_time = 8 - current_hour - (current_minute / 60)
            elif current_hour == 8:
                if current_minute == 0:
                    sleep_time = 0
                else:
                    sleep_time = 24 - current_hour + 8 - (current_minute / 60)
            time.sleep(sleep_time * 3600)
