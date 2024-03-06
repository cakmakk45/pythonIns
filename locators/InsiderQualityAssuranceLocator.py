from selenium.webdriver.common.by import By

class InsiderQualityAssuranceLocator:
    url = "https://useinsider.com/careers/quality-assurance/"
    clickSeeAllQAJobs = (By.XPATH,"//a[normalize-space()='See all QA jobs']")
    validateFilterByLocationText = (By.XPATH,"//label[normalize-space()='Filter by Location']")
    clickLocationDropdownMenu = (By.XPATH,"(//span[@role='presentation'])[1]")
    clickRemove = (By.XPATH,"//span[@id='select2-filter-by-location-container']//span[@title='Remove all items'][normalize-space()='×']")
    clickFirstOption = (By.XPATH, "//*[@class='select2-results__option select2-results__option--highlighted']")
    validateFilterByDepartmanText = (By.XPATH,"//label[normalize-space()='Filter by Department']")
    clickDepartmanDropdownMenu = (By.XPATH,"//span[@class='select2 select2-container select2-container--default']//b[@role='presentation']")
    validateDepartmanQA = (By.XPATH, "//*[@id='select2-filter-by-department-container']")
    clickQualityAssurenceOption = (By.XPATH,"//li[@id='select2-filter-by-department-result-tqdq-Quality Assurance']")
    validateShowingCounter = (By.XPATH,"//p[@id='resultCounter']")
    validateFirstPozitionContentLike = (By.XPATH,"//section[@id='career-position-list']//div[@class='row']//div[1]//div[1]//span[1]")
    validateSecondPozitionContentLike = (By.XPATH,"//section[@id='career-position-list']//div[@class='row']//div[2]//div[2]//span[1]")
    validatethreePozitionContentLike = (By.XPATH,"//section[@id='career-position-list']//div[3]//div[1]//span[1]")
    validateLocationsFirst = (By.XPATH,"(//div[@class='position-location text-large'][normalize-space()='Istanbul, Turkey'])[1]")
    validateLocationSecond = (By.XPATH,"(//div[@class='position-location text-large'][normalize-space()='Istanbul, Turkey'])[2]")
    validateLocationThird = (By.XPATH,"(//div[@class='position-location text-large'][normalize-space()='Istanbul, Turkey'])[3]")
    clickFirstPozition = (By.XPATH,"//body/section[@id='career-position-list']/div[@class='container']/div[@class='row']/div[@id='jobs-list']/div[1]/div[1]")
    clickViewRoleButton = (By.XPATH,"/html[1]/body[1]/section[3]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]")
    validateApplyForThisJobs = (By.XPATH,"(//a[@class='postings-btn template-btn-submit shamrock'][normalize-space()='Apply for this job'])[1]")

