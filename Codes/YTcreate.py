from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files\Python310\chrome driver\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("balasubramanianathi@gmail.com")
#email_field.send_keys(Keys.RETURN)
email_field.send_keys(Keys.RETURN)


password_field = driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf")
password_field.send_keys("balasubramanianathi")
password_field.send_keys(Keys.RETURN)
'''
profile_selection = driver.find_element(By.ID, "img")
profile_selection.click()

create_account = driver.find_element(By.ID, "endpoint")
create_account.click()'''

time.sleep(100)

driver.quit()