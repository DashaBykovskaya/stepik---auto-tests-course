from selenium import webdriver
import os

link="http://suninjuly.github.io/file_input.html"
browser=webdriver.Chrome()
browser.get(link)

option1=browser.find_element_by_name("firstname")
option1.send_keys("Name")
option2=browser.find_element_by_name("lastname")
option2.send_keys("Last name")
option3=browser.find_element_by_name("email")
option3.send_keys("My email")

button1=browser.find_element_by_name("file")

current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'new.txt')            
element.send_keys(file_path)

button2=browser.find_element_by_css_selector("button.btn")
button2.click()


