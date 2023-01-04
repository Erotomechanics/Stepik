import csv

n = int(input()) - 1

with open('deniro.csv', encoding='utf-8') as f:
    rows = list(csv.reader(f))

rows.sort(key=lambda x: int(x[n]) if x[n].isdigit() else x[n])
for row in rows:
    print(','.join(row))