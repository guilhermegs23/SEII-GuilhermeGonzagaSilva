#Guilherme Gonzaga Silva 11621EMT021 
#prog16.py

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    #csv_data = csv.reader(data_file)
    csv_data = csv.DictReader(data_file)

    # tirando a primeira linha do arquivo csv
    next(csv_data)
    #next(csv_data)

    for line in csv_data:
        #if line['0'] == 'No Reward':
        if line['FirstName'] == 'No Reward':
            break
        #names.append(f"{line['0']} {line['1']}")
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)