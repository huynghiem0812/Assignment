import os
import csv
import json
import yaml
import pandas as pd

directory = 'C:/Users/Admin/PycharmProjects/Assignment/Convert'

def convert_to_csv(file_path_1):
    df = pd.read_json(file_path_1)
    file_name_1 = os.path.splitext(file_path_1)[0] + ".csv"
    df.to_csv(file_name_1)
    print(f"{file_path_1} converted to {file_name_1}")

def convert_to_json(file_path_2, data_2):
    file_name_2 = os.path.splitext(file_path_2)[0]
    json_file = f"{file_name_2}.json"

    with open(json_file, 'w') as f_json:
        json.dump(data_2, f_json)

    print(f"{file_path_2} converted to {json_file}")

folder_path = input("Enter the folder path: ")

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if file_path.endswith(".json"):
        with open(file_path, "r") as f:
            convert_to_csv(file_path)
    elif file_path.endswith(".yaml"):
        with open(file_path, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            convert_to_csv(file_path)
    elif file_path.endswith('.csv'):
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            convert_to_json(file_path, data)
    else:
        print(f"{file_path} is not a json, yaml or csv file.")
