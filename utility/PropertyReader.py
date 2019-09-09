import configparser

rawconfigparser = configparser.RawConfigParser()
rawconfigparser.read('../Assets/config.properties')
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
