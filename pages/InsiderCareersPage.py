from locators.InsiderCareersLocator import*
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pathlib import Path
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class InsiderCareersPage(InsiderCareersLocator):
        def __init__(self, driver):
            self.pageName = "Insider Careers Page"
            self.driver = driver
            
        def scroll_down(self, pixels):
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        
        def clickToCompany(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickCampany))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("Clicked on the company tab.")
            
        def clickToCareers(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickCareers))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("Careers option selected.")
            
            
        def validateOurStory(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateOurStoryy)) 
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print("'Our Story' text has been validated.")
                return True
            except TimeoutException:
                print("Timeout hatası: Our story article could not be validated.")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False
        
        def validateOurLocation(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateOurLocationsText))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element) 
                print("'Our Locations' text has been validated.")
                return True
            except TimeoutException:
                print("Timeout hatası: Our Locations article could not be validated.")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False
            
        def validateSeeAllTeams(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateSeeAllTeamsButton)) 
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print("'See All Teams' text has been validated.")
                return True
            except TimeoutException:
                print("Timeout hatası: See All Teams article could not be validated.")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False
            
        def validateLifeAtInsider(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateLİfeAtInsider)) 
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)            
                print("'Life at Insider' text has been validated.")
                return True
            except TimeoutException:
                print("Timeout hatası: Lİfe at Insider article could not be validated.")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False
            
        def toUp(self):
            self.driver.execute_script("window.scrollTo(0, 0);")
            
        
            
            