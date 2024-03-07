from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the wbsite
driver.get("https://formy-project.herokuapp.com/switch-window")

# Open and switch to a new tab
new_tab = driver.find_element(By.ID, "new-tab-button")
new_tab.click()

wait = WebDriverWait(driver, 5)
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

## Check if a new tab is opened

assert "https://formy-project.herokuapp.com/" in driver.current_url, "The new tab is not open."

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

# Open alert
alert = driver.find_element(By.ID, "alert-button")
alert.click()

# Switch to the alert and accept it
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

# Close the WebDriver
driver.quit()