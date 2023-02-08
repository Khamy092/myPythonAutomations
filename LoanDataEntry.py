from selenium import webdriver
import time

# Start a new instance of Chrome
driver = webdriver.Chrome()

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Fill in the username and password fields
username_field = driver.find_element_by_id("username")
username_field.send_keys("iamtaqi10")
password_field = driver.find_element_by_name("password")
password_field.send_keys("WAFAWAFA214865")
password_field.submit()

# Wait for the page to load after logging in
time.sleep(10)

# Navigate to the profile page of the recipient
driver.get("https://www.instagram.com/ahmadi._fatah/")
time.sleep(5)

# Click the message button
message_button = driver.find_element_by_xpath("//button[contains(text(), 'Message')]")
message_button.click()
time.sleep(2)

# Fill in the message text
message_field = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
message_field.send_keys("Hi bro, did the guys send the money?")

# Send the message
send_button = driver.find_element_by_xpath("//button[contains(text(), 'Send')]")
send_button.click()
