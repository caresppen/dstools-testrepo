from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r"C:\Downloads\Tools\selenium\geckodriver\geckodriver.exe")

browser.get('http://www.seleniumhq.org')

elem = browser.find_element_by_link_text('Downloads')
elem.click()
searchBar = browser.find_element_by_name("search")
searchBar.send_keys('download')

# Using Keys to interact with the elements: searchBar
searchBar.send_keys(Keys.ENTER)
