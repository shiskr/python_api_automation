import pandas as pd
import os


def getUserDetails(user_type):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + '/../Assets/PCM_Excel.xlsx'
    df = pd.read_excel(file_path, sheet_name="users")
    all_columns = list(df.columns.values)
    all_row_values = []
    for i in df.index:
        if df['user_type'][i]==user_type:
            all_row_values = list(df.iloc[i, :])
    all_details = dict(zip(all_columns, all_row_values))
    return all_details
