def convert_to_bytes(size, uoi):
    if uoi == 'KB':
        return int(size) * 1024
    elif uoi == 'MB':
        return int(size) * 1048576
    elif uoi == 'GB':
        return int(size) * 1073741824
    return int(size)


def convert_from_bytes(x):
    if x > 1023:
        x = round(x / 1024)
        uoi = ' KB'
        if x > 1023:
            x = round(x / 1024)
            uoi = ' MB'
            if x > 1023:
                x = round(x / 1024)
                uoi = ' GB'
    return str(x) + uoi


with open('files.txt', encoding='utf-8') as f:
    list_f = []
    for line in f:
        name_ext, size, uoi = line.strip().split()
        name, ext = name_ext.split('.')
        list_f.append([name, ext, convert_to_bytes(size, uoi)])

list_f.sort(key=lambda x: x[0])
list_f.sort(key=lambda x: x[1])

prev_line = list_f[0]
print(f'{prev_line[0]}.{prev_line[1]}')
sum_of_bytes = prev_line[2]
for i in range(1, len(list_f)):
    if prev_line[1] == list_f[i][1]:
        sum_of_bytes += list_f[i][2]
        print(f'{list_f[i][0]}.{list_f[i][1]}')
        prev_line = list_f[i]
    else:
        print('----------')
        print(f'Summary: {convert_from_bytes(sum_of_bytes)}')
        print()
        print(f'{list_f[i][0]}.{list_f[i][1]}')
        prev_line = list_f[i]
        sum_of_bytes = prev_line[2]
else:
    print('----------')
    print(f'Summary: {convert_from_bytes(sum_of_bytes)}')
    print()
