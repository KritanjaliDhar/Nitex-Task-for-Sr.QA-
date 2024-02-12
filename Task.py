#Install Python & Selenium WebDriver for Python
#Make a sample web page with the following requirements 
#Execute the script Opens the HTML file containing the form in a Chrome browser window.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("file://C:/xampp/htdocs/test.php") 


event_name_input = driver.find_element_by_id("eventName")
event_name_input.send_keys("Falgun Celebration")

event_date_input = driver.find_element_by_id("eventDate")
event_date_input.send_keys("2024-02-12")

participant_emails_input = driver.find_element_by_id("participantEmails")
participant_emails_input.send_keys("kdhar223@gmail.com, kritanjalisynesis123@gmail.com")

submit_button = driver.find_element_by_css_selector("input[type='submit']")
submit_button.click()

time.sleep(10)  

event_items = driver.find_elements_by_css_selector(".event-item")
if len(event_items) > 0:
    print("Test Passed: Event item is successfully added.")
else:
    print("Test Failed: Event item is not added.")

driver.quit()
