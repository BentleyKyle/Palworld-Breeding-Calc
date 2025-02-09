import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

#url for project
url = 'https://palbreed.com/breeding-tree'

#create a web session
driver = webdriver.Firefox()
driver.implicitly_wait(1)
driver.get(url)

#click button
#Nyafia = driver.find_element(By.CLASS_NAME, "pal")
#Nyafia.click()
#find a parent from the list
#NyafiaFirstParent =  driver.find_element(By.CLASS_NAME, "name")
#bob = NyafiaFirstParent.get_attribute('innerHTML')
#print(bob)
#clear the page and return to original list of pals
#clearBttnEl = driver.find_element(By.CLASS_NAME, "clear-btn")
#clearBttnEl.click()

#list of all initial pals
pals = driver.find_elements(By.CLASS_NAME, "name")
x = 0
while (x < len(pals)):
    name = pals[x].get_attribute('innerHTML')
    if name != "":
        print("Breeding Combos for: ", name)
        pals[x].click()
        Breeders = driver.find_elements(By.CLASS_NAME, "name")
        i = 0
        while (i < len(Breeders)):
            Parent1 = Breeders[i].get_attribute('innerHTML')
            print("     Parent 1:", Parent1)
            i += 1
            Parent2 = Breeders[i].get_attribute('innerHTML')
            print("     Parent 2:", Parent2)
            i += 1
            Child = Breeders[i].get_attribute('innerHTML')
            print("     Child:", Child)
            i += 1
        clearBttnEl = driver.find_element(By.CLASS_NAME, "clear-btn")
        clearBttnEl.click()
        x += 1
        pals = driver.find_elements(By.CLASS_NAME, "name")
    elif name == "":
        x += 1

