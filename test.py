from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import click
import os.path

from valid_path import is_pathname_valid


driver = webdriver.Chrome(
    "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
)
driver.get("https://www.google.com/")
box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
)
box.send_keys("giraffe")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()


down_path_and_name = "C:\\Users\\miste\\Pictures\\Saved Pictures\\tierlist\\giraffe.png"
driver.find_element_by_xpath(
    '//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img'
).screenshot(down_path_and_name)


driver.get("https://www.google.com/")
box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
)
box.send_keys("wolf")
box.send_keys(Keys.ENTER)
