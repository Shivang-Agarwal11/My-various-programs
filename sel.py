import selenium
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.implicitly_wait(8)
#browser.execute_script("window.scrollBy(0,2000)","")
browser.find_element_by_xpath("//*[@id='search']").send_keys('bad guy')
browser.find_element_by_xpath("//*[@id='search-icon-legacy']").click()