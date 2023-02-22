import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
#action = webdriver.ActionChains(driver)
driver.get("http://www.chumbak.com/")
driver.find_element(By.ID, "user_6_").click()
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.NAME, "customer[email]").send_keys("aparnamohanan@gmail.com")
driver.find_element(By.NAME, "customer[password]").send_keys("aparna_123")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
driver.find_element(By.XPATH, "//a[@class='Button Button--primary']").click()
driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Add a new address')]").click()
driver.find_element(By.NAME, "address[first_name]").send_keys("Aparna")
driver.find_element(By.NAME, "address[last_name]").send_keys("Mohanan")
driver.find_element(By.NAME, "address[company]").send_keys("APMO")
driver.find_element(By.NAME, "address[phone]").send_keys("9087654395")
driver.find_element(By.NAME, "address[address1]").send_keys("Peruvilai")
driver.find_element(By.NAME, "address[address2]").send_keys("kanyakumari")
driver.find_element(By.NAME, "address[city]").send_keys("Nagercoil")
select_con=Select(driver.find_element(By.CSS_SELECTOR,"select[name='address[country]']"))
select_con.select_by_visible_text("India")
driver.find_element(By.NAME, "address[zip]").send_keys("629008")
select_pro=Select(driver.find_element(By.CSS_SELECTOR,"select[name='address[province]']"))
select_pro.select_by_visible_text("Tamil Nadu")
driver.find_element(By.XPATH, "//input[@class='Form__Checkbox']").click()
driver.find_element(By.XPATH, "//button[@class='Form__Submit Button Button--primary Button--full']").click()
driver.find_element(By.ID, "mm-homepage-search").send_keys("watch")
time.sleep(6)
driver.find_element(By.XPATH, "//a[contains(normalize-space(),'Mother of Pearl Tropical Beads Watch & Bracelet Set')]").click()
element=driver.find_element(By.CSS_SELECTOR,"button[class='ProductForm__AddToCart Button Button--primary Button--full']")
driver.execute_script("arguments[0].click()",element)
time.sleep(15)






