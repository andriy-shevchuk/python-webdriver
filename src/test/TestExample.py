import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class TestWebdriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.ebay.com.au/b/Desserts/14310/bn_1617319")
        time.sleep(10)
        itemslist = driver.find_elements_by_xpath("//h3[@class='s-item__title']")
        for item in itemslist:
            print(item.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
