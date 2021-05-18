import pickle
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://messages.google.com/web/conversations')


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)


foo = input()

save_cookie(driver, 'C:/WebDriver/cookie')

try:
    cookie = {"name": "foo",
          "value": "bar",
          "domain": "https://messages.google.com/web/conversations"}
    session.add_cookie(cookie)
except exceptions.InvalidCookieDomainException as e:
    print(e.message)
