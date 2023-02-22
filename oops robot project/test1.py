import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class chumbak():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.chumbak.com/")
    driver.find_element(By.ID, "user_6_").click()
    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    driver.find_element(By.XPATH, "//a[text()='Create one']").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='customer[first_name]'] ").send_keys("anusha")
    driver.find_element(By.CSS_SELECTOR,"input[name='customer[last_name]'] ").send_keys("ragavan")
    driver.find_element(By.CSS_SELECTOR,"input[name='customer[email]']  ").send_keys("anusha@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"input[name='customer[password]'] ").send_keys("anu")
    element=driver.find_element(By.XPATH,"//button[text()='Create my account']")
    driver.execute_script("arguments[0].click()",element)
    actual_error=driver.find_element(By.XPATH,"//li[contains(text(),' is too short ')]" ).text
    print(actual_error)

class addtocart(chumbak):

