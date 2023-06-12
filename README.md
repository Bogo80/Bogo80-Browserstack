# Bogo80-Browserstack
Selenium automation testing with python leveraging Browserstack Platform 

# BrowserStack 
is a cloud-based platform that allows you to perform automated browser testing on various browsers, operating systems, and devices. This guide will provide instructions on how to configure your testing environment and execute automated tests using Selenium and Python.
# Set BrowserStack Credentials
To begin, you need to set your BrowserStack credentials. You can either provide your BrowserStack username and access key directly or set them as environment variables. Here are the credentials for reference:
userName: YourUser 
accessKey: YourPass
# BrowserStack Reporting
BrowserStack provides reporting capabilities for your test executions. To set up reporting, you need to configure the following parameters:

projectName: Set the name of your project. For example, "Marketing Website."
buildName: Specify the name of the job or testsuite being run. For instance, "browserstack build."
buildIdentifier: This is a unique identifier that differentiates each execution. It can be customized using expressions like ${BUILD_NUMBER} or ${DATE_TIME}. Read more about build identifiers here. The current configuration sets the buildIdentifier as '#${BUILD_NUMBER}', which appends the build number.
<img width="1081" alt="image" src="https://github.com/Bogo80/Browserstack-/assets/133137279/dffa2d09-db66-442b-a53d-53005788f79f">

# Platforms (Browsers / Devices to Test)
The platforms section specifies the browsers and devices you want to test on. You can choose from a wide range of configurations available on BrowserStack. The following are a few example configurations:

Testing on Chrome latest version on OS X Ventura:

plaintext
Copy code
- os: OS X
  osVersion: Ventura
  browserName: Chrome
  browserVersion: latest
Testing on Chrome latest version on Windows 10:

plaintext
Copy code
- os: Windows
  osVersion: 10
  browserName: Chrome
  browserVersion: latest
Testing on Samsung Galaxy S22 Ultra:

plaintext
Copy code
- deviceName: Samsung Galaxy S22 Ultra
  browserName: chrome
  osVersion: 12.0
  
# Python Test Script Description
The Python test script demonstrates an example test scenario using Selenium and BrowserStack. Here's an overview of the script:

1. Imports the necessary libraries for Selenium and WebDriver management.
2. Sets the email and password variables for logging into the BrowserStack platform
3. Navigates to the BrowserStack sign-in page, handles the cookie notification, and maximizes the window.
4. Fills in the email and password fields and clicks the login button.
5. Searches for the "invite user" field and retrieves its text.
6. If the "invite user" field is found, clicks on the link.
7. Captures the current URL after clicking the link.
8. Sets the test status as 'passed' or 'failed' based on the presence of the "invite user" field and URL.
9. Stops the WebDriver.

# Instructions 
1. Enter in the Yml file utpate the  BROWSERSTACK_ACCESS_KEY as env variables  with  username and the key availble from your Brosersstack account
2.          userName: yourUser
            accessKey: yourKey
3. In the Test.py enter login detail for the https://www.browserstack.com/ the script wil use this account to autjeticate and perform the atomativ test.
4.          EMAIL_ID = "SomeEmail.com"
            PASSWORD = "Pass"


