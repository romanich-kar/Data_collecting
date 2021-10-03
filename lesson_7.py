'''
Вариант II
Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД. Магазины можно
выбрать свои. Главный критерий выбора: динамически загружаемые товары
'''
 
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

db = MongoClient('localhost', 27017)['mvideo']
collection = db['products']

driver = webdriver.Chrome()
driver.get('https://www.mvideo.ru/promo/luchshie-predlojeniya')

while True:
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a.next-btn.c-btn.c-btn_scroll-horizontal.c-btn_icon.i-icon-fl-arrow-right.hidden.disabled')
            )
        )

        driver.execute_script("$(arguments[0]).click();", next_button)
    except exceptions.TimeoutException:
        print('Сбор данных окончен')
        break

products = driver.find_elements_by_class_name('accessories-product-list')

item = {}
for product in products:
    item['title'] = product.find_element_by_class_name(
        'fl-product-tile-title__link sel-product-tile-title') \
        .get_attribute('title')

    item['link'] = product.find_element_by_css_selector(
        'a.fl-product-tile-title__link sel-product-tile-title') \
        .get_attribute('href')

    item['price'] = float(
        product.find_element_by_css_selector(
            'span.fl-product-tile-price__current').get_attribute('innerHTML').replace(
                '&nbsp;', '').replace('¤', ''))

    item['image_link'] = product.find_element_by_css_selector(
        'img[class="lazy product-tile-picture__image"]') \
        .get_attribute('src')

    collection.update_one({'$set': item}, upsert=True)
driver.quit()
