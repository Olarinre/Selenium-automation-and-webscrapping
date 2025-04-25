
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https:/geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(10)  #  seconds

#seach for the element using the class name
search_box = driver.find_element(By.XPATH, "//input[@type='text']")
search_box.send_keys("computer architecture and design")
search_box.send_keys(Keys.RETURN)


driver.implicitly_wait(10)  # seconds

input("Press Enter to close...")
driver.quit()