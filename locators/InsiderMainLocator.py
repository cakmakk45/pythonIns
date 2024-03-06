from selenium.webdriver.common.by import By

class InsiderMainLocator:
    url = "https://useinsider.com/"
    
    mainPageText = (By.XPATH, "//a[@class='navbar-brand d-flex flex-row align-items-center']//img")
    clickAcceptAllButton = (By.XPATH,"//a[@id='wt-cli-accept-all-btn']")
