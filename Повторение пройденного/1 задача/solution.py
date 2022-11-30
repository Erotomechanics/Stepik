names = []
for _ in range(int(input())):                          # Создание списка имён уже занятых ящиков
    names.append(input().split('@')[0])
for _ in range(int(input())):                          # Добавление нового имени для ящика
    s = input()
    if s not in names:                                 # Если имени нет в списке
        names.append(s)
        print(f'{s}@beegeek.bzz')
    elif not names[names.index(s)][-1].isdigit():      # Если имя есть в списке и в конце имени отсутствует цифра
        index = 0
        while True:
            index += 1
            if s+str(index) in names:
                continue
            else:
                names.append(s + str(index))
                print(f'{s + str(index)}@beegeek.bzz')
                break
    else:                                             # Если имя есть в списке и в конце имени присутствует цифра
        index = 1
        while s+str(index) not in names:
            names.append(s+str(index))
            print(f'{s+str(index)}@beegeek.bzz')
            index += 1