from selenium import webdriver

browser = webdriver.Chrome('/Users/Matthew_Round/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title