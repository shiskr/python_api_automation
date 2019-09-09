import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter
import os


def getAdminUserDetails(user_type):
    df = pd.read_excel(r"../Assets/PCM_Excel.xlsx", sheet_name="users")
    facility_listy = []

    for i in df.index:
        facility_listy.append(df['FACILITY ID'][i])
        facilitynames_listy.append(df['FACILITY NAME'][i])
    return facility_listy, facilitynames_listy


if __name__ == '__main__':
    getAdminUserDetails("getAdminUser")