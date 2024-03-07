from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Open the website
driver.get("https://formy-project.herokuapp.com/form")

# Complete a form
## Complete a first name field
first_name = driver.find_element(By.ID, "first-name")
first_name.click()
first_name.send_keys("Chidchanok")

## Complete a last name field
last_name = driver.find_element(By.ID, "last-name")
last_name.click()
last_name.send_keys("Sattayavinit")

## Complete a job title field
job_title = driver.find_element(By.ID, "job-title")
job_title.click()
job_title.send_keys("Software tester")

## Select highest level of education using radio button
education = driver.find_element(By.ID, "radio-button-2")
education.click()

## Select gender using checkbox
gender = driver.find_element(By.ID, "checkbox-2")
gender.click()

## Select years of experience in dropdown
exp_years_element = driver.find_element(By.ID, "select-menu")
exp_years = Select(exp_years_element)
exp_years.select_by_value("1")

## Select date in datepicker
date = driver.find_element(By.ID, "datepicker")
date.click()
date.send_keys("03/05/2024")
date.send_keys(Keys.ENTER)

## Submit a form
submit_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary")
submit_button.click()

## Checking if a form is submitted
assert "https://formy-project.herokuapp.com/thanks" in driver.current_url, "Form submission failed: didn't navigate to the expected page"

# Close the WebDriver
driver.quit()