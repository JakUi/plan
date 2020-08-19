import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMain():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_main(self):
    self.driver.get("https://temp-mail.org/ru")
    time.sleep(20)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-rds:nth-child(1) > svg").click()
    time.sleep(2)
    self.driver.execute_script("window.open('','_blank');")
    self.driver.switch_to.window(self.driver.window_handles[1])
    self.driver.get("https://planoplan.com/")
    self.driver.set_window_size(1307, 1000)
    time.sleep(10)

    self.driver.find_element(By.LINK_TEXT, "Войти").click() 
    time.sleep(4)

    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"button_signup\"]").click()
    self.driver.find_element(By.NAME, "username").send_keys(Keys.CONTROL + "v")
    self.driver.find_element(By.CSS_SELECTOR, ".ipRijx").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ipRijx").send_keys("SlozhnyParol19")

    time.sleep(3)
    self.driver.find_element_by_xpath("//*[@class='buttonLoader__View-hkgzw7-0 iWHvdP']").click()
    self.driver.switch_to.window(self.driver.window_handles[0])
    time.sleep(35)

    target =  self.driver.find_element_by_xpath("/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[1]")
    target.location_once_scrolled_into_view
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .inboxSenderName").click()
    code = self.driver.find_element_by_xpath('/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div[4]').text
    time.sleep(3)
 
    self.driver.switch_to.window(self.driver.window_handles[1])   
    time.sleep(3)
 
    self.driver.find_element_by_xpath("//*[@id='form-entry']/div/form/fieldset/label/div[2]/input").send_keys(code)
    self.driver.find_element_by_xpath("//*[@class='buttonLoader__View-hkgzw7-0 iWHvdP']").click()
    time.sleep(5)
    assert self.driver.find_element_by_xpath("//*[@class='button__View-sc-1yof2fx-0 lpQcr']"), 'не верная регистрация'

    