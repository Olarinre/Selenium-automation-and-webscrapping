from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.environ['PATH'] += r"C:/Users/USER/Documents/Selenium python/chromedriver-win64/chromedriver-win64"

driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/")
driver.implicitly_wait(10)

#get data from the table on the same page
table = driver.find_element(By.XPATH, "//table[@id='desktop-streaks-table']")
table_data = table.find_elements(By.TAG_NAME, "tr")

league_data = []
stat_data = []
next_match_data = []
odds_data = []
date =[  ]

for row in table_data:
    print(row.text)

#dump all these in a .txt file
with open("football_data.txt", "w") as file:
    for row in table_data:
        file.write(row.text + "\n")
    



