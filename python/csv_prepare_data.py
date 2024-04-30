import csv
import datetime as dt
import calendar
import pytz

input_filename = 'crypt_chosen.csv'
output_filename = 'crypt_transformed.csv'

with open(input_filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)

    data = [row for row in reader]

new_data = []
new_header = ['year', 'month', 'day'] + header[1:]

for row in data:
    timestamp = int(row[0])
    date = dt.datetime.fromtimestamp(timestamp, pytz.utc)
    year = date.year
    month = calendar.month_name[date.month]
    day = date.day

    new_data.append([year, month, day] + row[1:])

with open(output_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_header)
    writer.writerows(new_data)
