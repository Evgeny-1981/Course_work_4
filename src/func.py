import requests
import os
import csv
import json
from datetime import datetime

def get_vacancy():
    t_date = datetime.now().strftime('%d-%m-%Y')
    response = requests.get(url='https://api.hh.ru/vacancies')
    with open(f'info_{t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    vacancy = response.json()

def main():
    get_vacancy()

if __name__ == '__func__':
    func()
