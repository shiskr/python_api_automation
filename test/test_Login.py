from API_objects.Login_API import *
from utility.Requests_Manager import Requests_Manager
from utility.Excel_Reader import *


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class TestLogin(Requests_Manager):

    def test_valid_login_status_code(self):
        user_details = getUserDetails("getAdminUser")
        login_api = Login_API()
        login_api.verify_user_Login_status_code(user_details)

    def test_Invalid_login(self):
        user_details = getUserDetails("getUserwithWrongPassword")
        login_api = Login_API()
        login_api.verify_user_invalid_login(user_details)

    def test_valid_login_response(self):
        user_details = getUserDetails("getAdminUser")
        login_api = Login_API()
        login_api.verify_user_login_response(user_details)
