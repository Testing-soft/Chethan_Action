from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get(r"https://www.makemytrip.com/")
time.sleep(5)
# sign = driver.find_element("xpath", "//iframe[@title='Sign in with Google Button']")
# driver.switch_to.frame(sign)
# time.sleep(5)
# driver.find_element("xpath","//div[@class='nsm7Bb-HzV7m-LgbsSe-Bz112c']").click()
# time.sleep(5)
# handles=driver.window_handles
# driver.switch_to.window(handles[1])
# time.sleep(5)
# driver.find_element("xpath","//input[@type='email']").send_keys("chethanchethubc1995@gmail.com")
# driver.find_element("xpath",'//span[.="Next"]').click()
# driver.switch_to.default_content()
# log = driver.find_element("xpath",'//p[@data-cy="LoginHeaderText"]')
# act = ActionChains(driver)
# act.double_click(log).perform()


wait_=WebDriverWait(driver,3)

new_frame=driver.find_element("xpath",'//img[@class="slide"]')
wait_.until(EC.visibility_of(new_frame))
driver.switch_to.frame(new_frame)

element=driver.find_element("xpath",'//a[@class="close"]')
wait_.until(EC.visibility_of_element_located(element))
driver.find_element("xpath",'//a[@class="close"]').click()
