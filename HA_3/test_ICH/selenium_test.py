import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Добавьте этот импорт
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_logo(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310155")
    assert element, "тест не успешен"

def test_programs(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Программы')
    assert element, "тест не успешен"

def test_payment(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
    assert element, "тест не успешен"

def test_news(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Новости')
    assert element, "тест не успешен"

def test_about_us(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'О нас')
    assert element, "успешен"

def test_reviews(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Отзывы')
    assert element, "тест не успешен"

def test_de(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'de')
    assert element, "тест не успешен"

def test_ru(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'ru')
    assert element, "тест не успешен"

def test_call(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310161")

    assert element, "Элемент трубка не найден"

    element.click()
    time.sleep(1)
    element1 = driver.find_element(By.XPATH, '''//*[text()="Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"]''')
