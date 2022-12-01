names = []
# Создание списка имён уже занятых ящиков
for _ in range(int(input())):
    names.append(input().split('@')[0])
# Добавление нового имени для ящика
for _ in range(int(input())):
    s = input()
    if s not in names:
        names.append(s)
        print(f'{s}@beegeek.bzz')
# Если имя есть в списке и в конце имени отсутствует цифра
    elif not names[names.index(s)][-1].isdigit():
        index = 0
        while True:
            index += 1
            if s + str(index) in names:
                continue
            else:
                names.append(s + str(index))
                print(f'{s + str(index)}@beegeek.bzz')
                break
# Если имя есть в списке и в конце имени присутствует цифра
    else:
        index = 1
        while s + str(index) not in names:
            names.append(s + str(index))
            print(f'{s + str(index)}@beegeek.bzz')
            index += 1
