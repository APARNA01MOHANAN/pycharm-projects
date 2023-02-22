from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

def test_add_to_cart_and_checkout():
    driver.get("http://www.chumbak.com/")
    driver.find_element(By.ID, "user_6_").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.NAME, "customer[email]").send_keys("aparnamohanan@gmail.com")
    driver.find_element(By.NAME, "customer[password]").send_keys("aparna_123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    driver.find_element(By.ID, "mm-homepage-search").send_keys("watch")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Sort by : ']")))
    sort_by_element = driver.find_element(By.XPATH, "//span[text()='Sort by : ']")
    driver.execute_script("arguments[0].scrollIntoView();", sort_by_element)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Price, low to high")))
    driver.find_element(By.LINK_TEXT, "Price, low to high").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Makeup Buff Pouch-Blue & Green')]").click()
    add_to_cart_element = driver.find_element(By.XPATH, "//*[text()='Add to cart']")
    driver.execute_script("arguments[0].click();", add_to_cart_element)
    driver.find_element(By.XPATH, "//a[@aria-label='Open cart']").click()
    checkout_element = driver.find_element(By.XPATH, "//*[text()='Checkout']")
    driver.execute_script("arguments[0].click();", checkout_element)
    driver.find_element(By.ID, "checkout_reduction_code").send_keys("adsg456")
    apply_element = driver.find_element(By.XPATH, "//*[text()='Apply']")
    driver.execute_script("arguments[0].click();", apply_element)
    error_message_element = driver.find_element(By.XPATH, "//p[contains(text(),'Enter a valid discount')]")
    assert error_message_element.text == "Enter a valid discount code or gift card"

if __name__ == '__main__':
    test_add_to_cart_and_checkout()
    driver.quit()
