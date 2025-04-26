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


for txt in table_data:
    stat_data.append(txt.find_elements(By.XPATH, "//td[@ng-bind-html='team-stat']")[0].text)

print(stat_data)




