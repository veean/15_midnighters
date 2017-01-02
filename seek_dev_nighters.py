import requests
import pytz
import datetime

API = 'https://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    pages = requests.get(API).json()['number_of_pages']
    for page in range(pages):
        parameters_ = {'pages': page}
        data_response = requests.get(API, params=parameters_).json()
        for record in data_response:
            yield record


def get_midnighters(devman_adepts):
    for adept in devman_adepts:
        correct_date_time = get_correct_time(adept['timestamp'], adept['timezone'])
        if correct_date_time.hour in (0, 5):
            yield adept['username']


def get_correct_time(timestamp, timezone):
    if timestamp is None and timezone is None:
        return None
    else:
        correct_time = datetime.datetime.fromtimestamp(timestamp, pytz.timezone(timezone))
        return correct_time


if __name__ == '__main__':
    parameters = {'pages': 2}
    req = requests.get(API, params=parameters).json()['records']
    print(req[1])
