from locators.InsiderMainLocator import*
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

class InsiderPage(InsiderMainLocator):
        def __init__(self):
            self.pageName = "Insider Main Page"
            
            
        def setup_method(self):
                self.driver = webdriver.Chrome()
                self.driver.get(self.url)
                self.vars = {}
                
        def maximize_window(self):
            self.driver.maximize_window()
            print("Browser extended.")
                
        
        
        def validateInsiderMainPage(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.mainPageText)) 
                print("Insider home page loaded successfully.")
                return True
            except TimeoutException:
                print("Timeout hatası: Insider home page did not load successfully")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False
        
        def clickAcceptAllPopup(self):
            wait = WebDriverWait(self.driver, 30) 
            loginButton = wait.until(EC.presence_of_element_located(self.clickAcceptAllButton))
            actions = ActionChains(self.driver)
            actions.move_to_element(loginButton).click().perform()
            print("Cookies accepted.")
            
        def quit(self):
            sleep(10)
            self.driver.quit()
            print("Operations are completed and the browser is closed")
            
        def driver(self):
            return self.driver
        
        