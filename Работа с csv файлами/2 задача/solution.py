import csv

def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as f1, open('condensed.csv', 'w', encoding='utf-8', newline='') as f2:
        d = {}
        columns = [id_name]
        rows = csv.reader(f1)
        for row in rows:
            d[row[0]] = d.setdefault(row[0], []) + [row[2]]
            if row[1] not in columns:
                columns.append(row[1])
        writer = csv.writer(f2)
        writer.writerow(columns)
        for k, v in d.items():
            writer.writerow([k] + v)
