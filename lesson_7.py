'''
Вариант II
Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД. Магазины можно
выбрать свои. Главный критерий выбора: динамически загружаемые товары
'''
 # Пока оставляю заглушку, задание будет сделано до конца дня 27.09.2021.

  from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('https://www.mvideo.ru')
