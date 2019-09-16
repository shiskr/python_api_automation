from utility.PropertyReader import *
import requests
import logging
from Assets.APIs import *
import json
import pytest
import allure

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]


class Login_API(Singleton):

    def verify_user_Login_status_code(self, user_details):
        headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
        payload = {'userName': user_details['username'], 'password': user_details['password']}
        logging.info("Payload is : " + str(payload))
        logging.info("Calling Login API with user details : " + str(user_details))
        response = requests.post(getURL()+postLoginApi, headers=headers, data=payload)
        json_data = json.loads(response.text)
        logging.info("Json Data is : " + str(json_data))
        try:
            assert response.status_code == 200, "Logged In"
            assert json_data['Status'] == "SUCCESS"
            logging.info("Verified")
        except AssertionError:
            logging.exception("Cannot Log In")
            raise

    def verify_user_invalid_login(self, user_details):
        headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
        payload = {'userName': user_details['username'], 'password': user_details['password']}
        logging.info("Payload is : " + str(payload))
        logging.info("Calling Login API with user details : " + str(user_details))
        response = requests.post(getURL()+postLoginApi, headers=headers, data=payload)
        json_data = json.loads(response.text)
        logging.info("Json Data is : " + str(json_data))
        try:
            assert response.status_code == 401
            assert json_data['Status'] == "Unauthorized"
            assert json_data['Error'] == "The login credentials you entered do not match our record."
            logging.info("Verified")
        except AssertionError:
            logging.exception("Error")
            raise

    def verify_user_login_response(self, user_details):
        headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
        payload = {'userName': user_details['username'], 'password': user_details['password']}
        logging.info("Payload is : " + str(payload))
        logging.info("Calling Login API with user details : " + str(user_details))
        response = requests.post(getURL()+postLoginApi, headers=headers, data=payload)
        json_data = json.loads(response.text)
        logging.info("Json Data is : " + str(json_data))
        try:
            assert response.status_code == 200
            assert json_data['Data']['UserFullName'] == user_details["firstName"]+" "+user_details["lastName"]
            logging.info("Verified")
        except AssertionError:
            logging.exception("Error")
            raise

    def get_user_token(self, user_details):
        headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
        payload = {'userName': user_details['username'], 'password': user_details['password']}
        logging.info("Payload is : " + str(payload))
        logging.info("Calling Login API with user details : " + str(user_details))
        response = requests.post(getURL()+postLoginApi, headers=headers, data=payload)
        json_data = json.loads(response.text)
        logging.info("Json Data is : " + str(json_data))
        token = json_data["Data"]["Token"]
        logging.info("Token is : "+ token)
        return token
