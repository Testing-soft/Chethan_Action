from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
driver =webdriver.Chrome(executable_path=path)
url=r"https://www.amazon.in/"
driver.get(url)
driver.maximize_window()

act_obj=ActionChains(driver)
element=driver.find_element("xpath",'//a[@id="nav-link-accountList"]')
act_obj.double_click(element).perform()
# new_frame=driver.find_element("xpath",'//form[@name="signIn"]')
# driver.switch_to.frame(new_frame)
time.sleep(5)
driver.find_element("xpath",'//input[@name="email"]').send_keys("chethanchethubc1995@gmail.com")
driver.find_element("xpath",'//input[@id="continue"]').click()

# wait_=WebDriverWait(driver,5)
# element1=driver.find_element("xpath",'//input[@type="password"]')
# wait_.until(EC.visibility_of_element_located(element1))
driver.find_element("xpath",'//input[@type="password"]').send_keys(8197757732)
driver.find_element("xpath",'//input[@id="signInSubmit"]').click()
# driver.back()
# driver.back()
# driver.back()