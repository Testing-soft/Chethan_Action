# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time



# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)

# url=r"http://the-internet.herokuapp.com/upload"
# driver.get(url)
# driver.maximize_window()

# new_frame=driver.find_element("xpath",'//form[@method="POST"]')
# driver.switch_to.frame(new_frame)
# driver.find_element_by_id("file-upload").send_keys("C://Users/latha/Pictures/SCREEN SHOT/screen.jpg")
###################################################################################


# import xlrd
# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\PYTHON_SELENIUM\Excel_file\Excel1.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# # rows=ws.get_rows()
# rows=ws.get_rows()

# # print(rows)

# d={row[0].value:row[1].value for row in rows}
# print(d)

############################################################################
# from selenium import webdriver
# import time

# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)
# url=r"https://demowebshop.tricentis.com/"
# driver.get(url)
# driver.maximize_window()

# driver.implicitly_wait(10)
# driver.find_element_by_link_text("Facebook").click()
# driver.find_element_by_link_text('YouTube').click()

# handles=driver.window_handles
# # driver.switch_to.window(handles[1])

# for handle in handles[1:]:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     driver.close()
#     time.sleep(3)
# driver.switch_to.window(handles[0])
# print(driver.title)
# driver.close()
#############################################################################
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)
# url=r"https://demowebshop.tricentis.com/"
# driver.get(url)
# driver.maximize_window()

# wait_=WebDriverWait(driver,3)
# element=driver.find_element("xpath",'//div[@class="header-logo"]')
# wait_.until(EC.visibility_of(element))
# print(driver.title)
###############################################################################
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time


# path1=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path1)

# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\PYTHON_SELENIUM\demo1.html"
# driver.get(path)
# driver.maximize_window()


# element=driver.find_element("xpath",'//select[@id="standard_cars"]')


# sel_obj=Select(element)

# print(sel_obj.is_multiple)

# all_opt=sel_obj.options
# for opt in all_opt:
#     print(opt.text)

# sel_obj.select_by_visible_text("Audi")
# time.sleep(1)

# sel_obj.select_by_visible_text("Honda")
# time.sleep(1)

# sel_obj.select_by_visible_text("BMW")

#########################################################################
# from selenium import webdriver 
# from selenium.webdriver.support.select import Select
# import time

# path1=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path1)

# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\PYTHON_SELENIUM\demo1.html"
# driver.get(path)
# driver.maximize_window()

# element=driver.find_element("xpath",'//select[@id="multiple_cars"]')
# s_obj=Select(element)

# s_obj.select_by_visible_text("Audi")
# time.sleep(2)
# s_obj.select_by_visible_text("Mercedes")
# time.sleep(2)
# s_obj.select_by_visible_text("Land Rover")
# print(s_obj.is_multiple)
# all_opt=s_obj.options
# for opt in all_opt:
#     print(opt.text)

# driver.close()
#########################################################################

# from selenium import webdriver
# import time
# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=path)
# url=r"https://demowebshop.tricentis.com/"
# driver.get(url)
# time.sleep(2)
# path1=r"C:\Users\latha\Desktop\Selenium_python_RMG\PYTHON_SELENIUM\screec_shot\\"
# driver.save_screenshot(path+"srceenshot.png")

# driver.close()

###############################################################
# from selenium import webdriver

# opts=webdriver.ChromeOptions()
# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\PYTHON_SELENIUM"
# opts.add_experimental_option("prefs",{"download.default_dictionary":path,"safebrowsing.enable":True})

# path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
# opts=webdriver.ChromeOptions()
# opts.add_argument("--disable-notification")
# driver=webdriver.Chrome(executable_path=path)


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path=r"C:\Users\latha\Desktop\Selenium_python_RMG\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
act_obj=ActionChains(driver)
# url=r"https://www.myntra.com/"
# driver.get(url)

# element=driver.find_element("xpath",'(//div[@class="desktop-navLink"])[1]')
# act_obj.move_to_element(element).perform()

#################################################################
#Double_click
# clk=driver.find_element("xpath",'(//div[@class="desktop-navLink"])[5]')
# act_obj.double_click(clk).perform()

# check_box=driver.find_element("xpath",'//input[@value="Nail Polish"]')
# act_obj.double_click(check_box).perform()

# url=r"https://crossbrowsertesting.github.io/drag-and-drop.html"
# driver.get(url)

# drag=driver.find_element("xpath",'//div[@id="draggable"]')
# drop=driver.find_element('id',"droppable")
# act_obj.drag_and_drop(drag,drop).perform()


#####################################################
url=r"https://testautomationpractice.blogspot.com/"
driver.get(url)

new_frame=driver.find_element('xpath','//form[@method="post"]')
driver.switch_to.frame(new_frame)
driver.find_element('xpath','//input[@type="file"]').send_keys("C://Users/latha/Pictures/SCREEN SHOT/pic")
