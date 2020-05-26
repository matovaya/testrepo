from selenium import webdriver
import time

from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/registration2.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Johny")
	browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Cage")
	browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("Holly@woo.d")
	browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
	time.sleep(2)
	mes = browser.find_element(By.TAG_NAME,"h1")
	assert mes.text == "Congratulations! You have successfully registered!"
finally:
	browser.quit()