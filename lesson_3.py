"""1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
записывающую собранные вакансии в созданную БД."""

from pymongo import MongoClient
from lesson_2 import hh, superjob

db = MongoClient('localhost', 27017)['vacancies']
jobs_hh = lesson_2.hh('https://petrozavodsk.hh.ru', 'Python', 10)
jobs_superjob = lesson_2.superjob('https://www.superjob.ru', 'Python', 10)

def jobs_insert():
    db.hh.insert_many(jobs_hh)
    db.superjob.insert_many(jobs_superjob)

"""2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы."""

def big_salary(collection, multiple=True):
    s = int(input('Введите величину зарплаты: '))
    if multiple:
        results = collection.find({'salary': {$gt: s}})
        return [r for r in results]
    else:
        return collection.find_one({'salary': {$gt: s}})


"""3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта."""

def add_new_vacancy(collection, jobs):
    for job in jobs:
        if job['link'] not in collection.find({'link': 1}):
            db.collection.insert_one(job)
        else:
            continue
    