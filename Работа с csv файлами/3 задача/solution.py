import csv

with open('student_counts.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = ['year'] + sorted(reader.fieldnames[1:], key=lambda x: (int(x.split('-')[0]), (x.split('-')[1])))
    columns = list(reader)
with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(columns)