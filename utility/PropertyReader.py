import configparser
import os

rawconfigparser = configparser.RawConfigParser()
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path + '/../Assets/config.properties'
rawconfigparser.read(file_path)
ApiURL = None
XAPIKey = None


#URL
def getURL():
    if rawconfigparser.get("Environment", "env") == "QA":
        ApiURL = getQAURL()
    elif rawconfigparser.get("Environment", "env") == "Stag":
        ApiURL = getStagingURL()
    elif rawconfigparser.get("Environment", "env") == "Prod":
        ApiURL = getProductionURL()
    return ApiURL


def getQAURL():
    return rawconfigparser.get("HostDetails", "qa_base_host")


def getStagingURL():
    return rawconfigparser.get("HostDetails", "stag_base_host")


def getProductionURL():
    return rawconfigparser.get("HostDetails", "prod_base_host")


#XAPIKEY
def getXAPIKey():
    if rawconfigparser.get("Environment", "env") == "QA":
        XAPIKey = getQAXAPIKey()
    elif rawconfigparser.get("Environment", "env") == "Stag":
        XAPIKey = getProductionXAPIKey()
    elif rawconfigparser.get("Environment", "env") == "Prod":
        XAPIKey = getProductionXAPIKey()
    return XAPIKey


def getQAXAPIKey():
    return rawconfigparser.get("HostDetails", "qa_api_key_admin")


def getProductionXAPIKey():
    return rawconfigparser.get("HostDetails", "stag_api_key_admin")


def getProductionXAPIKey():
    return rawconfigparser.get("HostDetails", "prod_api_key_admin")
