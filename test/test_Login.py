import logging
from API_objects import Login_API
from API_objects.Login_API import *
from utility import Requests_Manager
from utility.Excel_Reader import *


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class TestFacebookLogin(Login_API, Requests_Manager):

    def test_valid_login_status_code(self):
        username, password = getAdminUserDetails("getAdminUser")
        verify_user_Login_status_code(username, password)

    def test_Invalid_login(self):
        username, password = getInvalidUserDetails()
        verify_user_invalid_login(username, password)

    def test_valid_login_response(self):
        username, password = getAdminUserDetails()
        verify_user_login_response(username, password)
