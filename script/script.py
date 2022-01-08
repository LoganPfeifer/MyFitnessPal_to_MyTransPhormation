from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from datetime import datetime, timedelta
import time
import configuration

driver = webdriver.Chrome(executable_path=configuration.CHROMEDRIVER_PATH)

driver.get()

print(driver.title)

password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys(configuration.MFP_PIN)
password_field.send_keys(Keys.RETURN)

time.sleep(3)

date = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
driver.get(configuration.MFP_URL + "?date=" + date)

time.sleep(1)

table_data = driver.find_elements_by_tag_name("td")

Macros = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
foo = 0
i = 0

while i < len(table_data):
  if table_data[i].text == "Quick Tools":
    try:
      Macros[foo][0] = int(table_data[i+1].text)
    except:
      Macros[foo][0] = int(0)
    
    try:
      Macros[foo][1] = int(table_data[i+2].text)
    except:
      Macros[foo][1] = int(0)

    try:
      Macros[foo][2] = int(table_data[i+3].text)
    except:
      Macros[foo][2] = int(0)
    try:
      Macros[foo][3] = int(table_data[i+4].text)
    except:
      Macros[foo][3] = int(0)
    try:
      Macros[foo][4] = int(table_data[i+5].text)
    except:
      Macros[foo][4] = int(0)

    foo = foo + 1
    i = i + 5
  else: i = i + 1

print(Macros[0])
print(Macros[1])
print(Macros[2])
print(Macros[3])

time.sleep(1)

###############################################

driver.get("https://app.mytransphormation.com/login")

time.sleep(3)

inputFields = driver.find_elements(By.TAG_NAME,"input")

#print(inputFields)

email_field = inputFields[0]
email_field.clear()
email_field.send_keys(configuration.FP_EMAIL)

password_field = inputFields[1]
password_field.clear()
password_field.send_keys(configuration.FP_PASSWORD)

password_field.send_keys(Keys.RETURN)

time.sleep(3)

navigation_elements = driver.find_elements(By.CLASS_NAME, "nav-item")
navigation_elements[2].click()

time.sleep(1)

buttons = driver.find_elements(By.CLASS_NAME, "button-clear")
buttons[2].click()

time.sleep(1)

### Enter Meal 1 ###

if(Macros[0][0] > 0):
  meals_add = driver.find_elements(By.CLASS_NAME, "dim")
  meals_add[1].click()

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "button")
  buttons[1].click()

  time.sleep(1)

  inputs = driver.find_elements(By.TAG_NAME, "input")
  inputs[2].send_keys(Macros[0][1])
  inputs[3].send_keys(Macros[0][2])
  inputs[4].send_keys(Macros[0][3])
  inputs[5].send_keys(Macros[0][4])
  inputs[1].clear()
  inputs[1].send_keys(Macros[0][0])

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "ion-button")
  buttons[14].click()

time.sleep(1)

### Enter Meal 2 ###

if(Macros[1][0] > 0):
  meals_add = driver.find_elements(By.CLASS_NAME, "dim")
  meals_add[4].click()

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "button")
  buttons[1].click()

  time.sleep(1)

  inputs = driver.find_elements(By.TAG_NAME, "input")
  inputs[2].send_keys(Macros[1][1])
  inputs[3].send_keys(Macros[1][2])
  inputs[4].send_keys(Macros[1][3])
  inputs[5].send_keys(Macros[1][4])
  inputs[1].clear()
  inputs[1].send_keys(Macros[1][0])

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "ion-button")
  buttons[14].click()

time.sleep(1)

### Enter Meal 3 ###
if(Macros[2][0] > 0):
  meals_add = driver.find_elements(By.CLASS_NAME, "dim")
  meals_add[7].click()

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "button")
  buttons[1].click()

  time.sleep(1)

  inputs = driver.find_elements(By.TAG_NAME, "input")
  inputs[2].send_keys(Macros[2][1])
  inputs[3].send_keys(Macros[2][2])
  inputs[4].send_keys(Macros[2][3])
  inputs[5].send_keys(Macros[2][4])
  inputs[1].clear()
  inputs[1].send_keys(Macros[2][0])

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "ion-button")
  buttons[14].click()

time.sleep(1)

### Enter Meal 4 ###
if(Macros[3][0] > 0):
  meals_add = driver.find_elements(By.CLASS_NAME, "dim")
  print(meals_add)
  meals_add[10].click()

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "button")
  buttons[1].click()

  time.sleep(1)

  inputs = driver.find_elements(By.TAG_NAME, "input")
  inputs[2].send_keys(Macros[3][1])
  inputs[3].send_keys(Macros[3][2])
  inputs[4].send_keys(Macros[3][3])
  inputs[5].send_keys(Macros[3][4])
  inputs[1].clear()
  inputs[1].send_keys(Macros[3][0])

  time.sleep(1)

  buttons = driver.find_elements(By.TAG_NAME, "ion-button")
  buttons[14].click()

time.sleep(5)

driver.quit()