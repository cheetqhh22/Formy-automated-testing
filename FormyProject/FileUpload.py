from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open the website
driver.get("https://formy-project.herokuapp.com/fileupload")

# Upload a File
file_upload_field = driver.find_element(By.ID, "file-upload-field")
file_upload = "C:/Users/armua/OneDrive/เดสก์ท็อป/Test Automation Project/FormyProject/File-to-Test/Cinnamoroll-image.jpg"

file_upload_field.send_keys(file_upload)
time.sleep(2)

# Reset
reset_button = driver.find_element(By.XPATH, "//button[@class='btn btn-warning btn-reset']")
reset_button.click()
time.sleep(2)

# Close the WebDriver
driver.quit()