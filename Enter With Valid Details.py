'''
Authour by : Tamer Samara
Emails : samaratamer2312@gmail.com
Phone : 050-8615913
Date : 05/12/2020
Enter The FaceBook With Valid Details And Writing To Log And A Result FIle Log
'''

# import relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import datetime, time

# Define new Test Class
class ValidDetails:
    def __init__(self): #Function that print when the test start
        print("The First Test was started...")

    def WriteToLog(self, fileName, textToWrite):
        f = open(fileName, 'a')  # opening file for adding text
        timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
        f.write(timeStamp + " " + textToWrite + '\n')  # writing timestamp + text + \n in order to start a new line!
        f.close()  # Closing file

    def PrintValidDetails(self):
        self.fileName = "FirstTest.txt" #Write the test result to file
        self.resultsFile = "TestsResults.txt" # contain all the results for all tests
        self.WriteToLog(self.fileName,"Starting with FB Test : - Try To Login With valid User Name Details.")
        self.WriteToLog(self.resultsFile, "Starting with First FB Test : - Try To Login With valid User Name Details.")

        try:
            option = Options()  # Use this 3 lines in order to add option to send or disable facebook notifications.
            option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 1})  # 1 yes 2 No
            self.driver = webdriver.Chrome(options=option,executable_path='C:\\driversp\\chromedriver.exe')# Start chrome with the option. chrome will not pop up message
            self.driver.get("http://www.facebook.com") # log in the website facebook by chrome browser
            self.driver.maximize_window() # maximize the window to the fit
            self.WriteToLog(self.fileName, "The Chrome browser Got maximized") #Write the test result to file
            time.sleep(3)
        except:
            self.WriteToLog(self.fileName,"ERROR - error occurred during facebook home page upload")#Write the test result to file - Firsttest.txt
            self.WriteToLog(self.resultsFile, "ERROR - error occurred during facebook home page upload")#Write the test result to file - Testresults.txt

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).clear() # wait until 10 seconds till the email field appears and clear the field
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys('tamer5678@hotmail.com') # fill the email field with the details
            self.WriteToLog(self.fileName,"The Email was entered successfully") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "The Email was entered successfully") #opening file for adding text for Result file log
            time.sleep(3)
        except:
            self.WriteToLog(self.fileName, "Can't find the Email Field--Test failed") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "Can't find the Email Field--Test failed") #opening file for adding text for Result file log

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys('312311004tetoo') # wait until 10 seconds till the email field appears and fill the password
            self.WriteToLog(self.fileName,"The Password was entered successfully") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile,"The Password was entered successfully") #opening file for adding text for Result file log
            time.sleep(3)

        except:
            self.WriteToLog(self.fileName,"Can't find the Password Field--Test failed") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "Can't find the Password Field--Test failed") #opening file for adding text for Result file log

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "login"))).click() # click on the login button
            self.WriteToLog(self.fileName, "The login button was clicked!") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "The login button was clicked!") #opening file for adding text for Result file log
            self.WriteToLog(self.fileName, "The Web Page is Reloading...") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "The Web Page is Reloading...") #opening file for adding text for Result file log
            time.sleep(20)
        except:
            self.WriteToLog(self.fileName,"The login button was not FOUND!") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile,"The login button was not FOUND!") #opening file for adding text for Result file log

        if ' Tamer' in str(self.driver.page_source): # Searching in the page source if he found the sentences so...
            self.WriteToLog(self.fileName, "The facebook was successfully logged in with valid details- Test PASS ") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "The facebook was successfully logged in with valid details- Test PASS ") #opening file for adding text for Result file log
        else:
            self.WriteToLog(self.fileName, "The facebook was not logged in with valid details- Test FAIL ") #opening file for adding text for first test log
            self.WriteToLog(self.resultsFile, "The facebook was not logged in with valid details- Test FAIL ") #opening file for adding text for Result file log
        self.driver.get_screenshot_as_file("FB Login With Valid Details.png") # taking a screen shot
        self.driver.quit()# quit the chrome


# Needed if you would like to run this plan within this file
#because all the plan is coded under class type
if __name__=='__main__':
    ValidDetails().PrintValidDetails()

