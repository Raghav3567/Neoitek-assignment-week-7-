from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (assumes chromedriver is in your PATH)
driver = webdriver.Chrome()

# Load your local HTML file or a test URL
driver.get("file:///path/to/your/button_test.html")  # Replace with your actual file path

# Give it a moment to load
time.sleep(2)

# Locate button by ID
button_by_id = driver.find_element(By.ID, "btn1")
print("Button text (by ID):", button_by_id.text)

# Locate button by Name
button_by_name = driver.find_element(By.NAME, "submitButton")
print("Button text (by Name):", button_by_name.text)

# Locate button by XPath
button_by_xpath = driver.find_element(By.XPATH, "//button[@id='btn1']")
print("Button text (by XPath):", button_by_xpath.text)

# Close the browser
driver.quit()
