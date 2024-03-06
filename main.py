from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.InsiderPage import *
from pages.InsiderCareersPage import *
from pages.InsiderQualityAssurancePage import *

insiderPage = InsiderPage()
insiderPage.setup_method()
insiderPage.maximize_window()

def controlMainPage(): 
    insiderPage.validateInsiderMainPage()
    insiderPage.clickAcceptAllPopup()  
controlMainPage()

def validateCompanyPage():
    print(insiderPage.driver)
    insiderCareerPage = InsiderCareersPage(driver=insiderPage.driver)
    insiderCareerPage.clickToCompany()
    sleep(10)
    insiderCareerPage.clickToCareers()
    insiderCareerPage.validateOurStory()
    insiderCareerPage.validateSeeAllTeams()
    insiderCareerPage.validateOurLocation()
    insiderCareerPage.validateLifeAtInsider()
    sleep(3)
    insiderCareerPage.toUp()
sleep(3)
validateCompanyPage()

def listOpenPozitions():
    print(insiderPage.driver)
    insiderQualitAssurancePage = InsiderQualityAssurancePage(driver = insiderPage.driver)
    insiderQualitAssurancePage.clickSeeAllButton()
    insiderQualitAssurancePage.validateFilterByLocation()
    insiderQualitAssurancePage.selectToLocationMenu()
    insiderQualitAssurancePage.selectToRemove()
    insiderQualitAssurancePage.selectFirstOption()
    insiderQualitAssurancePage.validateFilterByDepartman()
    insiderQualitAssurancePage.validateSelectedDepartmanQA()
    insiderQualitAssurancePage.validateShowing()
    insiderQualitAssurancePage.validateFirstContent()
    insiderQualitAssurancePage.validateSecondContent()
    insiderQualitAssurancePage.validateThirdContent()
    insiderQualitAssurancePage.validateLocationFirst()
    insiderQualitAssurancePage.validateLocationForSecond()
    insiderQualitAssurancePage.validateLocationForThird()
    insiderQualitAssurancePage.selectFirstPozition()
    current_window_handle = insiderPage.driver.window_handles[0] #current tab
    insiderQualitAssurancePage.selectviewRole()
    insiderPage.driver.switch_to.window(insiderPage.driver.window_handles[1])  #new tab opened
    insiderQualitAssurancePage.validateApplyForThisJob()
listOpenPozitions()


insiderPage.quit()   


    










