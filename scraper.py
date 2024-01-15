# import time
# import os
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# # Загрузка переменных окружения
# # load_dotenv()
#
# # Настройка опций Chrome
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск Chrome в режиме без графического интерфейса
# chrome_options.add_argument("--disable-gpu")
#
# # Укажите путь к вашему драйверу ChromeDriver здесь
# chrome_driver_path = ""
#
# # Настройка службы Chrome
# chrome_service = ChromeService(chrome_driver_path)
#
# # Запуск браузера Chrome
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
#
# # Определение URL-адреса
# url = "https://4pda.to/"
#
# # Открытие URL в браузере
# driver.get(url)
#
# # Дождитесь, пока пользователь вручную решит задачу CAPTCHA
# input("Пожалуйста, решите проверку CAPTCHA в браузере. Нажмите Enter, когда закончите.")
#
# # Подождите некоторое время, чтобы страница полностью загрузилась
# time.sleep(5)
#
# # Теперь вы можете продолжить с вашим кодом BeautifulSoup
# src = driver.page_source
# print(src)
#
# # Продолжите с разбора BeautifulSoup
# soup = BeautifulSoup(src, "lxml")
#
# # Остальная часть вашего кода...
#
# # Закройте браузер по завершении
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
# url = "https://4pda.to/"
#
# # Используем опции браузера, чтобы скрыть отображение окна браузера
# chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# # Запускаем браузер
# driver = webdriver.Chrome(options=chrome_options)
#
# # Открываем страницу
# driver.get(url)
#
# # Подождем, чтобы страница полностью загрузилась (вы можете увеличить время, если необходимо)
# time.sleep(5)
#
# # Получим HTML-код страницы
# src = driver.page_source
# print(src)
#
# # Закрываем браузер
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
#
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
#
# s = Service(executable_path='C:\\Users\\A1\\PycharmProjects\\NewsBot\\chromedriver\\chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=options)
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#   '''
# })
#
# try:
#     driver.maximize_window()
#     driver.get('https://4pda.to')
#     time.sleep(10)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
#
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
#
# s = Service(executable_path='C:\\Users\\A1\\PycharmProjects\\NewsBot\\chromedriver\\chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=options)
#
# try:
#     driver.maximize_window()
#     driver.get('https://4pda.to')
#
#     # Ваш код веб-скрапинга здесь
#     time.sleep(10)
#
# except Exception as ex:
#     print(ex)
#
# finally:
#     # Ожидание 10 секунд перед закрытием браузера
#     time.sleep(10)
#     driver.close()
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # Режим без графического интерфейса
#
# s = Service(executable_path='C:\\Users\\A1\\PycharmProjects\\NewsBot\\chromedriver\\chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=options)
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#   '''
# })
#
# try:
#     driver.maximize_window()
#     driver.get('https://4pda.to')
#
#     # Добавим ожидание загрузки элемента, который обычно отображается после пройденной проверки CloudFlare
#     WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#
#     # Получаем HTML-код страницы и выводим его в консоль
#     html_code = driver.page_source
#     print(html_code)
#
# except Exception as ex:
#     print(ex)
#
# finally:
#     driver.close()
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")  # Режим без графического интерфейса

    s = Service(executable_path='C:\\Users\\A1\\PycharmProjects\\NewsBot\\chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)

    return driver


def scrape_website(url):
    driver = setup_driver()

    try:
        driver.maximize_window()
        driver.get(url)

        # Добавим ожидание загрузки элемента, который обычно отображается после пройденной проверки CloudFlare
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Получаем HTML-код страницы и выводим его в консоль
        html_code = driver.page_source
        return html_code

    except Exception as ex:
        print(ex)
        return None

    finally:
        driver.quit()


# Пример использования
url_to_scrape = 'https://4pda.to'
html_result = scrape_website(url_to_scrape)

if html_result:
    print(html_result)
else:
    print("Что-то пошло не так при скрапинге.")