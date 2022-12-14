from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""""""""""Student Info"""""""""""

student_language = "Roumain"
student_level = "L1"
student_UE3_1 = "ECOA130d"
student_UE3_2 = "ECOA130g"

##################################

DRIVER_PATH = 'chromedriver'

options = Options()
options.headless = False    # flag to decide if the page is displayed (False) or not (True)
options.add_argument("--window-size=1920,1200")
# options.add_argument("--window-size=970,600") #bad dimensions

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://planning.inalco.fr/public")

with open("source_code.html", "w") as file:
    file.write(driver.page_source)
# print(driver.page_source)

delay = 3 # timeout delay in seconds

#WEBPAGE
try: # wait for the page to load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[1].bouton_Edit')))
    print("Page is ready!")
except TimeoutException:
    print("Loading of page took too much time!")

#MAIN PLANNING
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_language + " " + student_level)
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)

try: # wait for the table to load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
    print("Table is ready!")
except TimeoutException:
    print("Loading of table took too much time!")

edt = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
edt.screenshot(student_language + student_level + "_edt.png")
print("=> Main planning saved")

#SWITCH TO "MATIERES" SECTION
driver.find_element(By.ID, "GInterface.Instances[0].Instances[1]_Combo2").click()
driver.find_element(By.ID, "GInterface.Instances[1].Instances[0].bouton_Edit").click()
time.sleep(0.5)
driver.find_element(By.ID, "GInterface.Instances[1].Instances[0]_Liste").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.ID, "GInterface.Instances[1].Instances[0]_Liste").send_keys(Keys.RETURN)


#LOAD UE3 PLANNINGS
try: # wait for the table to load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[1].bouton_Edit')))
    print("Matieres section is ready!")
except TimeoutException:
    print("Loading of matieres section took too much time!")

#FIRST UE3
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_UE3_1)
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)
try: # wait for the ue3_1 to load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
    print("First UE3 is ready!")
except TimeoutException:
    print("Loading of first UE3 took too much time!")
edt_ue3_1 = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
time.sleep(0.5)
edt_ue3_1.screenshot(student_UE3_1 + "_edt.png")
print("=> First UE3 planning saved")

#SECOND UE3
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").clear()
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_UE3_2)
driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)
try: # wait for the ue3_1 to load
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
    print("Second UE3 is ready!")
except TimeoutException:
    print("Loading of second UE3 took too much time!")
edt_ue3_2 = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
time.sleep(0.5)
edt_ue3_2.screenshot(student_UE3_2 + "_edt.png")
print("=> Second UE3 planning saved")


########################
if not options.headless:
    time.sleep(3)
driver.quit()
print("Page closed.")