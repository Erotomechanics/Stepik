from datetime import datetime, timedelta

plural = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}


def choose_plural(x):
    if x % 10 == 1 and x % 100 != 11:
        return 0
    elif x % 10 >= 2 and x % 10 <= 4 and (x % 100 < 10 or x % 100 >= 20):
        return 1
    return 2


dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if datetime(2022, 11, 8, 12, 0) <= dt:
    print('Курс уже вышел!')
else:
    time_left = datetime(2022, 11, 8, 12, 0) - dt
    days = time_left.days
    hrs = time_left.seconds // 3600
    mnts = (time_left.seconds // 60) % 60
    if days > 0 and hrs > 0:
        print(f'До выхода курса осталось: {days} {plural[0][choose_plural(days)]} '
              f'и {hrs} {plural[1][choose_plural(hrs)]}')
    elif days > 0 and hrs == 0:
        print(f'До выхода курса осталось: {days} {plural[0][choose_plural(days)]}')
    elif hrs > 0 and mnts > 0:
        print(f'До выхода курса осталось: {hrs} {plural[1][choose_plural(hrs)]} '
              f'и {mnts} {plural[2][choose_plural(mnts)]}')
    elif hrs > 0 and mnts == 0:
        print(f'До выхода курса осталось: {hrs} {plural[1][choose_plural(hrs)]}')
    else:
        print(f'До выхода курса осталось: {mnts} {plural[2][choose_plural(mnts)]}')