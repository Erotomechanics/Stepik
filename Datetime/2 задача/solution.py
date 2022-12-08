from datetime import date, datetime


def date_to_int(d):
    return int(date.toordinal(datetime.strptime(d, '%d.%m.%Y')))


def is_available_date(booked_dates, date_for_booking):
    booked_dates_set = set()
    date_for_booking_set = set()
    for i in booked_dates:
        if '-' not in i:
            booked_dates_set.add(date_to_int(i))
        else:
            date1, date2 = i.split('-')
            for j in range(date_to_int(date1), date_to_int(date2) + 1):
                booked_dates_set.add(j)

    if '-' not in date_for_booking:
        date_for_booking_set.add(date_to_int(date_for_booking))
    else:
        date1, date2 = date_for_booking.split('-')
        for i in range(date_to_int(date1), date_to_int(date2) + 1):
            date_for_booking_set.add(i)

    return not bool(booked_dates_set & date_for_booking_set)
