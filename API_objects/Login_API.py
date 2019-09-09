from utility.PropertyReader import *
import requests
from utility import Requests_Manager



def verify_user_Login_status_code(self, username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
    payload = {'username': username, 'password': password}
    response = requests.get(getURL(), headers=headers, body=payload)

def verify_user_invalid_login(self, username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
    payload = {'username': username, 'password': password}
    response = requests.get(getURL(), headers=headers, body=payload)

def verify_user_login_response(self, username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded", "api-key": getXAPIKey()}
    payload = {'username': username, 'password': password}
    response = requests.get(getURL(), headers=headers, body=payload)