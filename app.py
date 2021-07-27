import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site_url = 'http://app-myproject.192.168.99.100.nip.io/'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome()
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--headless')
        chrome_opt.add_argument('--no-sandbox')

        self.driver =  webdriver.Chrome('./chromedriver', options=chrome_opt)
        self.url = site_url

    def test_temp_celsius(self):
        driver = self.driver
        driver.get(self.url)
        elem = driver.find_element_by_name("celsius")
        elem.send_keys("32")
        elem.send_keys(Keys.RETURN)
        elem2 = driver.find_element_by_id("fahrenheit")
        elem2.is_displayed()


    def test_run_script(self):
        driver = self.driver
        driver.get(self.url+"/script")
        elem = driver.find_element_by_name("script")
        elem.send_keys("test")
        elem.send_keys(Keys.RETURN)
        elem2 = driver.find_element_by_id("script")
        elem2.is_displayed()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

