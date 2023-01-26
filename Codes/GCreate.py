from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files\Python310\chrome driver\chromedriver.exe"

# Start a new Chrome browser instance
driver = webdriver.Chrome(path)

link1 = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
link2 = "https://accounts.google.com/signup"

# Navigate to the Gmail sign-up page
driver.get(link1)

# Find the elements for the form fields
first_name_field = driver.find_element(By.ID, "firstName")
last_name_field = driver.find_element(By.ID, "lastName")
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.NAME, "Passwd")
password_confirm_field = driver.find_element(By.NAME, "ConfirmPasswd")

# Enter the form field values
first_name_field.send_keys("tdzr")
last_name_field.send_keys("nwfg")
username_field.send_keys("tdzravnwfguzet")
password_field.send_keys("tdzruzet@098")
password_confirm_field.send_keys("tdzruzet@098")

# Find the submit button and click it
#submit_button = driver.find_element(By.XPATH, "//*[@id='accountDetailsNext']/content/span")
#submit_button.click()

password_confirm_field.send_keys(Keys().RETURN)

time.sleep(70)

# Close the browser
driver.quit()