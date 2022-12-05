from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Gform:
    def __init__(self, path):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def input_results(self, url, input_list):
        self.driver.get(url=url)
        for (address, price, link) in input_list:
            input_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
            input_fields[0].send_keys(address)
            input_fields[1].send_keys(price)
            input_fields[2].send_keys(link)
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, 'span[class="l4V7wb Fxmcue"]').click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, '.c2gzEf a').click()
            time.sleep(3)
