import requests
import pytz
import datetime

API = 'https://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    data_response = requests.get(API, params={'page': 1})
    pages = data_response.json()['number_of_pages']
    for page in range(2, pages+1):
        parameters = {'page': page}
        yield from data_response.json()['records']
        data_response = requests.get(API, params=parameters)


def get_midnighters(devman_adepts):
    midnighters_set = set()
    for adept in devman_adepts:
        correct_date_time = get_correct_time(adept['timestamp'], adept['timezone'])
        if correct_date_time and correct_date_time.hour in range(0, 5):
            midnighters_set.add(adept['username'])
    return midnighters_set


def get_correct_time(timestamp, timezone):
    if timestamp is None or timezone is None:
        return None
    else:
        correct_time = datetime.datetime.fromtimestamp(timestamp, pytz.timezone(timezone))
        return correct_time


if __name__ == '__main__':
    print('Midnighters list: ')
    for midnighter in get_midnighters(load_attempts()):
        print("Devman adept '{}' is an owl".format(midnighter))
