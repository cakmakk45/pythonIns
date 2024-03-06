from selenium.webdriver.common.by import By

class InsiderCareersLocator:

    clickCampany = (By.XPATH,"/html/body/nav/div[2]/div/ul[1]/li[6]/a")
    clickCareers = (By.XPATH,"//a[normalize-space()='Careers']")
    validateOurStoryy = (By.XPATH,"//h2[normalize-space()='Our story']")
    validateOurLocationsText = (By.XPATH,"//h3[normalize-space()='Our Locations']")
    validateSeeAllTeamsButton = (By.XPATH,"//a[normalize-space()='See all teams']")
    validateLİfeAtInsider = (By.XPATH,"//h2[normalize-space()='Life at Insider']")
    clickLoginButton = (By.XPATH, "//a[normalize-space()='Login']")
    
    