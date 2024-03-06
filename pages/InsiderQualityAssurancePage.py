from locators.InsiderQualityAssuranceLocator import*
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
from selenium.common.exceptions import NoSuchElementException

class InsiderQualityAssurancePage(InsiderQualityAssuranceLocator):
        def __init__(self, driver):
            self.pageName = "Insider Quality Assurance Page"
            self.driver = driver
            self.driver.get(self.url)
            
        def scroll_down(self, pixels):
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            
        def clickSeeAllButton(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickSeeAllQAJobs))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("See All button was clicked")
            
        
        def validateFilterByLocation(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateFilterByLocationText)) 
                print("Filter by location text has been validated.")
                return True
            except TimeoutException:
                print("Filter by location text is not validated")
                return False
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                return False 
            
        def selectToLocationMenu(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickLocationDropdownMenu))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()  
            print("Clicked on the first dropdown menu.") 
        
            
        #def selectToLocationMenu(self):
            #wait = WebDriverWait(self.driver, 30) 
            #self.driver.execute_script(f"var elementOrder = document.evaluate('/html/body/section[2]/div/div/div[2]/div/form/div[1]/select', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;if (elementOrder) "+"{var currentOptions = elementOrder.getElementsByTagName('option');for (var j = 0; j < currentOptions.length; j++) { var opt = currentOptions[j];if (opt.className == 'job-location istanbul-turkey') { elementOrder.selectedIndex = j; // Use j instead of i var event = new Event('change', { bubbles: true }); elementOrder.dispatchEvent(event); } } }")
            
        # button = wait.until(EC.presence_of_all_elements_located(self.clickLocationDropdownMenu))
            #self.driver.execute_script('var event = new MouseEvent("mousedown", { bubbles: true, cancelable: true, view: window }); arguments[0].dispatchEvent(event);', button)
            
        def selectToRemove(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickRemove))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("The cross sign(x) was pressed and the list of locations opened") 
            
        def selectFirstOption(self):
            try:
                wait = WebDriverWait(self.driver, 30) 
                button = wait.until(EC.presence_of_element_located(self.clickFirstOption))
                actions = ActionChains(self.driver)
                if button.is_displayed():
                    actions.move_to_element(button).click().perform()
                    print("Istanbul, Türkiye option was chosen") 
                else:
                    raise NoSuchElementException("Location not found")
            except NoSuchElementException as e:
                print(e)
            
            
        def validateFilterByDepartman(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateFilterByDepartmanText)) 
                print("filter by department text has been validated.")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False  
            
            
        def validateSelectedDepartmanQA(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateDepartmanQA)) 
                print("QA option is already selected")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False  
            
        def validateShowing(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateShowingCounter)) 
                print("Open pozitions have been listed successfully")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False  
            
        def validateFirstContent(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateFirstPozitionContentLike)) 
                print("The phrase 'Quality Assurance' is used in this position")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False  
        
        def validateSecondContent(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateSecondPozitionContentLike)) 
                print("The phrase 'Quality Assurance' is used in this position")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
            
        def validateThirdContent(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validatethreePozitionContentLike)) 
                print("The phrase 'Quality Assurance' is used in this position")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
            
        def validateLocationFirst(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateLocationsFirst)) 
                print("The location includes the phrase 'Istanbul, Turkey'")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
            
        def validateLocationForSecond(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateLocationSecond)) 
                print("The location includes the phrase 'Istanbul, Turkey'")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
        
        def validateLocationForThird(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateLocationThird)) 
                print("The location includes the phrase 'Istanbul, Turkey'")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
            
        def selectFirstPozition(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickFirstPozition))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("Clicked on first position detail.")
        
        def selectviewRole(self):
            wait = WebDriverWait(self.driver, 30) 
            button = wait.until(EC.presence_of_element_located(self.clickViewRoleButton))
            actions = ActionChains(self.driver)
            actions.move_to_element(button).click().perform()
            print("View role button clicked")
            
        def validateApplyForThisJob(self):
            try:
                wait = WebDriverWait(self.driver, 10)  
                element = wait.until(EC.presence_of_element_located(self.validateApplyForThisJobs)) 
                print("The page is opened and the Apply for this job button is validated.")
                return True
            except TimeoutException:
                return False
            except Exception as e:
                return False
            
        