import os
import json
from collections import ChainMap

def read_data(data_folder, file_name1, file_name2):

    data_read = {}

    # Read the first name-days file
    file_path1 = os.path.join(data_folder, file_name1)
    with open(file_path1, 'r', encoding="utf-8") as file1:
        name_days1 = json.load(file1)

    # Read the second name-days file
    file_path2 = os.path.join(data_folder, file_name2)
    with open(file_path2, 'r', encoding="utf-8") as file2:
        name_days2 = json.load(file2)

    # Merge them together
    for name_day in name_days1:
        data_read[name_day] = name_days1[name_day] + name_days2[name_day]

    return data_read
