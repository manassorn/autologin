from selenium import webdriver
from time import gmtime, strftime


def login(username, password):
	driver = webdriver.PhantomJS()
	driver.get('https://wifi.ais.co.th')
	try:
		driver.find_element_by_id('ctl00_Content_txtUsername').send_keys(username)
		driver.find_element_by_id('ctl00_Content_txtPassword').send_keys(password)
		driver.find_element_by_id('ctl00_Content_btnSubmit').click()
		__save_screenshot(driver, 'login_ok')
	except Exception as e:
		__save_screenshot(driver, 'login_error')
		raise e
		
	driver.close()

	
def status():
	driver = webdriver.PhantomJS()
	#driver.get('https://wifi.ais.co.th')
	#driver.get('file:///login.html')
	driver.get('file:///d:/python/login.html')
	try:
		is_logout = driver.find_element_by_id('ctl00_Content_Divafterlogcon').is_displayed()
		if is_logout: return False
		is_login = driver.find_element_by_id('ctl00_Content_txtUsername').is_displayed()
		if is_login: return True
		raise Exception('We are doomed!')
	except Exception as e:
		__save_screenshot(driver, 'status_error')
		raise e
	driver.close()

	
def logout():
	driver = webdriver.PhantomJS()
	driver.get('https://wifi.ais.co.th')
	
	try:
		driver.find_element_by_id('ctl00_Content_btnLogout').click()
		__save_screenshot(driver, 'logout_ok')
	except Exception as e:
		__save_screenshot(driver, 'logout_error')
		raise e
	driver.close()

def __save_screenshot(driver, suffix):
	now = strftime("%Y%m%d_%H%M%S", gmtime())
	file_name = '{}_{}.png'.format(now, suffix)
	driver.save_screenshot(file_name) # {datetime}_login_ok.png
	return file_name