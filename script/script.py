from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with

from datetime import datetime, timedelta

import time
import configuration

##### Functions #####

def EnterMeals(mealNum):
  meals_add = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.CLASS_NAME, "dim"))
  meals_add[1 + mealNum*3].click()

  # Wait here for elements to appear
  time.sleep(1)
  buttons = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.TAG_NAME, "button"))
  buttons[1].click()

  time.sleep(1)

  inputs = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.TAG_NAME, "input"))
  inputs[2].send_keys(Macros[mealNum][1])
  inputs[3].send_keys(Macros[mealNum][2])
  inputs[4].send_keys(Macros[mealNum][3])
  inputs[5].send_keys(Macros[mealNum][4])
  inputs[1].clear()
  inputs[1].send_keys(Macros[mealNum][0])

  buttons = driver.find_elements(By.TAG_NAME, "ion-button")
  buttons[14].click()






# Get the correct webdriver (Chrome in our case)
driver = webdriver.Chrome(executable_path=configuration.CHROMEDRIVER_PATH)

##### MyFitnessPal Data Colleciton #####

# Navigate to MyFitnessPal
driver.get(configuration.MFP_URL)

# Login to your MyFitnessPal
try:
  passwordField = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.NAME, "password"))
  passwordField.clear()
  passwordField.send_keys(configuration.MFP_PIN)
  time.sleep(1)
  passwordField.send_keys(Keys.RETURN)
except:
  print("Failed to log into MyFitnessPal.....abort")
  driver.quit()
  exit()

time.sleep(3)

# Navigate to the correct date (yesterday)
date = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
driver.get(configuration.MFP_URL + "?date=" + date)

# Wait for specific data to load
table_data = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.TAG_NAME, "td"))

Macros = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
meal = 0
i = 0

# Look through the data for "Quick Tools". The following data will be what we want.
while i < len(table_data):

  if table_data[i].text == "Quick Tools":
    
    # Calories
    try:
      Macros[meal][0] = int(table_data[i+1].text.replace(',',''))
    except:
      Macros[meal][0] = int(0)

    # Protein
    try:
      Macros[meal][1] = int(table_data[i+2].text.replace(',',''))
    except:
      Macros[meal][1] = int(0)

    # Carbs
    try:
      Macros[meal][2] = int(table_data[i+3].text.replace(',',''))
    except:
      Macros[meal][2] = int(0)
    
    # Fats
    try:
      Macros[meal][3] = int(table_data[i+4].text.replace(',',''))
    except:
      Macros[meal][3] = int(0)
    
    # Fiber
    try:
      Macros[meal][4] = int(table_data[i+5].text.replace(',',''))
    except:
      Macros[meal][4] = int(0)
    
    meal = meal + 1
    i = i + 5
  else: i = i + 1

##### Upload Data to MyTransPhormation #####

driver.get("https://app.mytransphormation.com/login")

# Input Email
inputFields = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.TAG_NAME,"input"))
email_field = inputFields[0]
email_field.clear()
email_field.send_keys(configuration.FP_EMAIL)

# Input Password
passwordField = inputFields[1]
passwordField.clear()
passwordField.send_keys(configuration.FP_PASSWORD)
passwordField.send_keys(Keys.RETURN)

time.sleep(3)

navigation_elements = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.CLASS_NAME, "nav-item"))
navigation_elements[2].click()

time.sleep(1)

buttons = WebDriverWait(driver, timeout=30).until(lambda d: d.find_elements(By.CLASS_NAME, "button-clear"))
buttons[2].click()

### Enter Meal 1 ###
for x in range(len(Macros)):
  if(Macros[x][0] > 0):
    EnterMeals(x)

time.sleep(5)

driver.quit()