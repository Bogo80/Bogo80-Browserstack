import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, ChromeOptions
# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!

driver = webdriver.Chrome()

#Log in details under teh script will execute
EMAIL_ID = "email "
PASSWORD = "yourpass"

username = os.environ.get('BROWSERSTACK_USERNAME')
accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
buildName = os.environ.get('JENKINS_LABEL')

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
}
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)

try:
    driver.get('https://www.browserstack.com/users/sign_in')
    driver.implicitly_wait(10) # seconds to load page 
    driver.maximize_window()   #maximize_window issues seen in windows 10 
    driver.implicitly_wait(15)
    
    #Accept cookie notification seems to interfer on android  browser
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, 'accept-cookie-notification'))).click()
    
    # Navigate to SignIn Page and seach username/email 
    driver.find_element("id", "user_email_login").send_keys(EMAIL_ID)

    #serch Password Field and fill the pasword 
    driver.find_element("id", "user_password").send_keys(PASSWORD)

    # Find and click login button
    driver.find_element("name", "commit").click()
    
    # Search for "invite user"  fileld in the webpage uing Class.ID
    item_on_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "invite-link"))).text
        
    print("The link :", item_on_page)
    
    if item_on_page != None:
        # If "invite user" fild found click the link..using XPATH Class
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, 'html/body/div[1]/header/div[2]/div/nav/ul[1]/li[2]/a'))).click()
        
    inviteURL = driver.current_url ## get Curent Url 
    
    if (item_on_page!= None) & (inviteURL != None):
        # Set the status of test as 'passed' if item is added to cart
       driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Authetication paseed and invite URL found !"}}')
    else:
        # Set the status of test as 'failed' if Invite Url not found 
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Url not found "}}')
            
finally:
    # Stop the driver
    driver.quit()
