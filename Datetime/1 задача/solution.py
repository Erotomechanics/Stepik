from datetime import datetime

with open('diary.txt', encoding='utf-8') as f:
    diary = f.read().split('\n\n')
diary.sort(key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))
for note in diary:
    print(note + '\n')
