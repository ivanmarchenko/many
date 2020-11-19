from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def check_kn_login(kn_email, kn_password):
    """
    Тест для планировщика django-q
    """
    print(f'Начало {check_kn_login.__name__}')
    url = 'http://board.kerch.net/login.aspx'
    try:
        options = set_chrome_options()
        driver = webdriver.Chrome(chrome_options=options)
        
        driver.get(url)
        print('Текущий урл:', driver.current_url)
        driver.save_screenshot('1.png')
        sleep(1)

        print('Авторизация')
        element = driver.find_element_by_name('ctl00$ContentPlaceHolder1$TextBox1')
        element.send_keys(kn_email)
        element = driver.find_element_by_name('ctl00$ContentPlaceHolder1$TextBox2')
        element.send_keys(kn_password)
        driver.find_element_by_name('ctl00$ContentPlaceHolder1$Button1').click()
        print('Результат авторизации:', driver.current_url)
        driver.save_screenshot('2.png')

        
        
        return driver.current_url
    except Exception as e:
        print(e)
        return None
    finally:
        print('close test_browser')
        driver.quit()

def set_chrome_options():
    """
    Установка опций для Chrome webdriver
    """
    options = Options()
    options.add_argument('--headless')
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('disable-infobars')   
    return options

def test_browser():
    """
    Тест webdriver
    """
    print('start test_browser')
    url = 'http://board.kerch.net/Default.aspx'
    try:
        options = set_chrome_options()
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        sleep(4)
        print(driver.current_url)
        print('OK')
        return driver.current_url
    except Exception as e:
        print(e)
        return None
    finally:
        print('close test_browser')
        driver.quit()






# Selenium Browser
# class Browser():
#     def __init__ (self):
#         options = Options()
#         options.add_argument('--headless')
#         options.headless = True
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--disable-extensions')
#         options.add_argument('disable-infobars')
#         self.driver = webdriver.Chrome(chrome_options=options)
