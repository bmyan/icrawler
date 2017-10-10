import json
import os
import csv
all_data = {}
keywordspath = '../keywords'
with open(os.path.join(keywordspath,'keywords_20170907.csv'), 'r') as f:
    lines = csv.reader(f)
    for line in lines:
        temp = []
        for keyword in line[1:]:
            if keyword != '':
                temp.append(keyword)
        all_data[line[0]] = temp
with open(os.path.join(keywordspath,'keywords_20170907.json'), 'w') as f:
    json.dump(all_data, f)
