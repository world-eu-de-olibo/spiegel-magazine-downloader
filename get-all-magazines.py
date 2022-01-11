# The downloader works only if you have a valid subscription from www.spiegel.de

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
#chrome_options.add_argument('--headless')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
ser = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=ser)

year = 1947
week = 1
driver.get("https://gruppenkonto.spiegel.de/download/download.html?heft=SP%2F"+str(year)+"%2F"+str(week)+"")
driver.find_element(By.ID, "loginname").send_keys("your-email-address")
driver.find_element(By.ID, "password").send_keys("your-password")
driver.find_element(By.ID, "submit").click()
week = week + 1
while (year <= 2022):   
    while (week <=52):
        driver.get("https://gruppenkonto.spiegel.de/download/download.html?heft=SP%2F"+str(year)+"%2F"+str(week)+"")
        print("Download",year,week,"gestartet...")        
        time.sleep(9)        
        week = week + 1
    week = 1
    year = year + 1
driver.quit()
