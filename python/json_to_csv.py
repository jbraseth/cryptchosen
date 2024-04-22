import json
import datetime as dt
import calendar

with open('crypt_chosen.json') as file:
    json_data = json.load(file)

num_rows = len(json_data['Data']['Data'])
num_cols = len(json_data['Data']['Data'][0])

columns = []

# build header row
for field in json_data['Data']['Data'][0]:
    column = []
    column.append(field)
    columns.append(column)

# populate columns
for entry in json_data['Data']['Data']:
    col_index = 0
    for field in entry:
        columns[col_index].append(entry[field])
        col_index += 1



# convert timestamp
timestamps = columns.pop(0)
timestamps.pop(0)

columns.insert(0, ['year'])
columns.insert(1, ['month'])
columns.insert(2, ['day'])

for timestamp in timestamps:
    date = dt.datetime.fromtimestamp(int(timestamp))
    columns[0].append(str(date.year))
    columns[1].append(str(calendar.month_name[date.month]))
    columns[2].append(str(date.day))



with open("crypt_chosen.csv", "w") as file:
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            file.write(str(columns[col_index][row_index]))
            if col_index != (num_cols - 1): file.write(',')
        file.write('\n')
