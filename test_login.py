import time
import unittest
from selenium import webdriver
import os

path = 'E:\\selenium_work\\selenium_code\\drivers\\chromedriver.exe'   #--->chrome driver ka path
ORG_HRM_URL = 'http://opensource-demo.orangehrmlive.com/'   #--->selenium ke code se copy kiya url
class LoginTest(unittest.TestCase):
  #fixtures
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=path)   #--->selenium ke code se copy kiya maximize wala code
        self.browser.get(ORG_HRM_URL)                            #-----jab koi url enter krega to window open karega
        self.browser.maximize_window()                               #-----aur ye usko maximise kr ke dega
        time.sleep(3)


    def tearDown(self) -> None:
        print('B')
        self.browser.close()      #---->jaise hi uper wala code excecute hoga to ye method apply hogi
        time.sleep(3)

    @classmethod
    def setUpClass(cls) -> None:
        print('C')

    @classmethod
    def tearDownClass(cls) -> None:
        print('D')



  # test methods/ test cases
    def test_valid_login(self):
        usernameInput = self.browser.find_element_by_id('txtUsername')    #--->selenium ke code se copy kiya code
        passwordInput = self.browser.find_element_by_name('txtPassword')   #--->selenium ke code se copy kiya code
        usernameInput.send_keys('Admin')       #---->Oranfehrm ka username
        passwordInput.send_keys('admin123')     #---->orangehrm ka password
        self.browser.find_element_by_id(btnLogin).click()         #--->selenium ke code se copy kiya code

        #first assertion
        self.assertEqual(self.browser.current_url, 'http://oopensource-demo.orangehrmlive.com/index.php/dashboard')
                                                    #---> url open karte hi homepage open hona chahiye
        self.assertIsNone(self.browser.find_element_by_id('menu_dashboard_index'))
                    #---> other option verify karne ke liye..inspect krke dashboard wala copy kiya hai



    def test_invalid_login(self):
        usernameInput = self.browser.find_element_by_id('txtUsername')  # --->selenium ke code se copy kiya code
        passwordInput = self.browser.find_element_by_name('txtPassword')  # --->selenium ke code se copy kiya code
        usernameInput.send_keys('xxx')  # ---->Oranfehrm ka username glt rakhana hai
        passwordInput.send_keys('yyadmin123')  # ---->orangehrm ka password galata rakhana hai
        self.browser.find_element_by_id(btnLogin).click()  # --->selenium ke code se copy kiya code

        self.assertEqual(self.browser.find_element_by_id('spanMessage').text, 'Invalid Credentials')
                                                #--->spanmessge ye b site inspect krke locator copy krna hai




    def test_invalid_credentials(self):
        usernameInput = self.browser.find_element_by_id('txtUsername')  # --->selenium ke code se copy kiya code
        passwordInput = self.browser.find_element_by_name('txtPassword')  # --->selenium ke code se copy kiya code
        usernameInput.send_keys('xxx')  # ---->Oranfehrm ka username glt rakhana hai
        passwordInput.send_keys('yyadmin123')  # ---->orangehrm ka password galata rakhana hai
        self.browser.find_element_by_id(btnLogin).click()  # --->selenium ke code se copy kiya code

        self.assertEqual(self.browser.find_element_by_id('spanMessage').text, 'Invalid Credentials')
        # --->spanmessge ye b site inspect krke locator copy krna hai

    def test_empty_credentials(self):
        usernameInput = self.browser.find_element_by_id('txtUsername')  # --->selenium ke code se copy kiya code
        passwordInput = self.browser.find_element_by_name('txtPassword')  # --->selenium ke code se copy kiya code
        #usernameInput.send_keys('')  # ---->Oranfehrm ka username blank rakhana hai
        #passwordInput.send_keys('')  # ---->orangehrm ka password blank rakhana hai
        self.browser.find_element_by_id(btnLogin).click()  # --->selenium ke code se copy kiya code

        self.assertEqual(self.browser.find_element_by_id('spanMessage').text, 'Username cannot be enpty')
        # --->spanmessge ye b site inspect krke locator copy krna hai

if __name__ == '__main__':
    unittest.main()
