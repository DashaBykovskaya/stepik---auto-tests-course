from selenium.webdriver.support.ui import Select
from selenium import webdriver

link=" http://suninjuly.github.io/selects2.html"
browser=webdriver.Chrome()
browser.get(link)

x=browser.find_element_by_id("num1").text
y=browser.find_element_by_id("num2").text
z=int(x)+int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(z)) 
button=browser.find_element_by_css_selector("button.btn")
button.click()
