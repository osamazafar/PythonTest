from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# import unittest

class Demo():

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(chrome_options = chrome_options)




    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.dialpadbeta.com/app")
        elem = driver.find_element_by_id("google-login-button")
        elem.click()
        driver.implicitly_wait(10)
        elem = driver.find_element_by_id("identifierId")
        elem.click()
        elem.send_keys("osamazafar128@gmail.com")
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
        elem = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        elem.click()
        elem.send_keys("Bigbang@5670006")
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='submit_approve_access']/content").click()
        time.sleep(4)
        driver.find_element_by_class_name("icon-sm").click()
        assert "No results found." not in driver.page_source

    def test_Search_Number(self):
        print("Clicking on search button")
        driver = self.driver
        time.time()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//*[@id='hd-btn-search']")
        elem.click()
        driver.implicitly_wait(10)  # seconds
        driver.find_element_by_id("search-input").send_keys("4154804104")
        driver.find_element_by_css_selector("#contact-search-dialer > div.button.circle.iblock > svg").click()
        time.sleep(10)

    def test_Recording_During_Call(self):
        print("The recording is enabled")
        time.time()
        driver = self.driver
        elem = driver.find_element(By.XPATH, '//*[@id="call-view-container"]/div/div/div/div/div[7]/div/div/div[3]/div[1]/div[1]')
        time.sleep(10)
        elem.click()
        time.sleep(5)
        elem.click()
        time.sleep(5)

    def test_Mute_During_Call(self):
        print("The recording is enabled")
        time.time()
        driver = self.driver
        elem = driver.find_element(By.XPATH, '//*[@id=\"call-view-container\"]/div/div/div/div/div[7]/div/div/div[3]/div[2]/div[1]')
        time.sleep(1)
        elem.click()
        time.sleep(5)
        elem.click()
        time.sleep(5)

    def test_hold_During_Call(self):
        print("The Hold is enabled")
        time.time()
        driver = self.driver
        elem = driver.find_element(By.XPATH, '//*[@id=\"call-view-container\"]/div/div/div/div/div[7]/div/div/div[3]/div[5]/div[1]')
        time.sleep(1)
        elem.click()
        time.sleep(5)
        elem.click()
        time.sleep(5)


    def test_call_parking(self):
        print("The call is being parked")
        time.time()
        driver = self.driver
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id=\"call-view-container\"]/div/div/div/div/div[7]/div/div/div[3]/div[7]/div[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id=\"transfer\"]/div[1]/div[2]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id=\"navbar-groups-list-table\"]/tr[2]/td/div/div[2]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id=\"group-filter-bar\"]/div/div[1]/div[3]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id=\"cp-list\"]/tr/td[5]/a').click()

    def test_Adding_Oncall(self):
        print("Adding PSTN on call")
        time.sleep(7)
        time.time()
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id=\"call-view-container\"]/div/div/div/div/div[7]/div/div/div[3]/div[8]/div[1]').click()
        time.sleep(2)
        elem = driver.find_element(By.ID, 'add-caller-search-input')
        elem.click()
        elem.send_keys("2138106980")
        elem.send_keys(Keys.RETURN)
        elem1 = driver.find_element(By.XPATH, '//*[@id=\"add-caller\"]/div[2]/div[3]/div[2]/div')
        elem1.click()
        time.sleep(15)
        driver.find_element(By.XPATH, '//*[@id="add-caller"]/div[2]/div[3]/div[2]/div').click()


    def test_EndingCall(self):
        print("Ending the call")
        time.time()
        driver = self.driver
        time.sleep(7)
        driver.find_element(By.XPATH, '//*[@id=\"call-view-container\"]/div/div/div/div/div[7]/div/div/div[3]/div[12]/div[1]').click()
        print("Testcase ended")
        driver.quit()



if __name__ == "__main__":
    d1 = Demo()
    d1.setUp()
    d1.test_search_in_python_org()
    d1.test_Search_Number()
    d1.test_Recording_During_Call()
    d1.test_Mute_During_Call()
    d1.test_hold_During_Call()
    d1.test_call_parking()
    d1.test_Adding_Oncall()
    d1.test_EndingCall()