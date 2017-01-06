import requests
import pytz
import datetime

API = 'https://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    data_response = requests.get(API, params={'page': 1})
    pages = data_response.json()['number_of_pages']
    for page in range(2, pages+1):
        parameters = {'page': page}
        for record in data_response.json()['records']:
            yield record
        data_response = requests.get(API, params=parameters)


def get_midnighters(devman_adepts):
    for adept in devman_adepts:
        correct_date_time = get_correct_time(adept['timestamp'], adept['timezone'])
        if correct_date_time and correct_date_time.hour in (0, 5):
            yield adept['username']


def get_correct_time(timestamp, timezone):
    if timestamp is None or timezone is None:
        return None
    else:
        correct_time = datetime.datetime.fromtimestamp(timestamp, pytz.timezone(timezone))
        return correct_time


if __name__ == '__main__':
    print('Midnighters list: ')
    # for midnighter, submit_time in get_midnighters(load_attempts()):
        # print('Devman adept {} submits challenge at {}'.format(midnighter, submit_time.strftime('%d-%m-%Y %H:%M:%S')))

    for midnighter in set(get_midnighters(load_attempts())):
        print("Devman adept '{}' is an owl".format(midnighter))

