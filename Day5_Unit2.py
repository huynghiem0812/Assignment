import argparse
import csv
import json
import pandas as pd
import pathlib

parser = argparse.ArgumentParser(description='File format convert')
parser.add_argument('-i', '--input', type=str, help='File input to convert')
parser.add_argument('-o', '--output', type=str, help='File output to convert')
args = parser.parse_args()


def json_to_csv(file_path, csv_name):       
    json_file = open(file_path, 'r')     
    csv_file = open(csv_name, 'w')     
    json_data = json.load(json_file)
    write = csv.writer(csv_file)
    write.writerow(json_data.keys())        
    write.writerow(json_data.values())  
    json_file.close()
    csv_file.close()


def csv_to_json(csv_file, json_file):          
    jsonDict = {}
    with open(csv_file) as csvfile:
        csv_data = csv.DictReader(csvfile)  
        jsonDict['data'] = []
        for rows in csv_data:
            jsonDict['data'].append(rows)  
    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(jsonDict, indent=4))  


def json_to_xlsx(json_file, xlsx_file):
    pd.read_json(json_file).to_excel(xlsx_file)


def xlsx_to_json(xlsx_file, json_file):
    pd.read_excel(xlsx_file).to_json(json_file)


with pathlib.Path(args.input) as f:
    if f.is_file():
        if args.input.find('json') != -1:
            if args.output.find('csv') != -1:
                json_to_csv(args.input, args.output)
            else:
                json_to_xlsx(args.input, args.output)
        elif args.input.find('csv') != -1:
            csv_to_json(args.input, args.output)
        else:
            xlsx_to_json(args.input, args.output)
    else:
        print(f'Did not find {args.input}')