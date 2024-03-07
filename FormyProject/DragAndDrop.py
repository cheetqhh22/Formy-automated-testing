from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# Open the website
driver.get("https://formy-project.herokuapp.com/dragdrop")

# Drag and Drop an image in a box
image = driver.find_element(By.ID, "image")
box = driver.find_element(By.ID, "box")

action = ActionChains(driver)
action.drag_and_drop(image, box).perform()

# Close the WebDriver
driver.quit()