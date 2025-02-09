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

#list of all initial pals
pals = driver.find_elements(By.CLASS_NAME, "name")
x = 0
while (x < len(pals)):
    name = pals[x].get_attribute('innerHTML')
    #DOM contains a blank entry that must be skipped
    if name != "":
        print("Breeding Combos for:", name)
        #click pal entry to load page with breeding combos for that pal
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
        #return to list of all pals
        clearBttnEl = driver.find_element(By.CLASS_NAME, "clear-btn")
        clearBttnEl.click()
        #next element in list of all pals and reload DOM
        x += 1
        pals = driver.find_elements(By.CLASS_NAME, "name")
    elif name == "":
        x += 1

