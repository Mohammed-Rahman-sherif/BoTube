from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files\Python310\chrome driver\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-922693519%3A1674834394585872&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=en&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHdk0Sq7O9Ms0wNL20O-vd7Bz3vt5Smi7RLaBJ8mwkZ70gvnV3-fp1I7T1lHc8gKQbP9E1O0ow")

email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("balasubramanianathi@gmail.com")
email_field.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    element.send_keys("balasubramanianathi")
    element.send_keys(Keys.RETURN)
finally:
    driver.quit()

'''
password_field = driver.find_element(By.NAME, "Passwd")
password_field.send_keys("balasubramanianathi")
password_field.send_keys(Keys.RETURN)'''
'''
profile_selection = driver.find_element(By.ID, "img")
profile_selection.click()

create_account = driver.find_element(By.ID, "endpoint")
create_account.click()'''

time.sleep(100)

driver.quit()