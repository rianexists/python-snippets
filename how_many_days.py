from leap_year import leap_year_check

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(month, year):
    if month == 2 and leap_year_check(year):
        return 29
    else:
        return days[month-1]