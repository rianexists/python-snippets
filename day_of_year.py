from how_many_days import days_in_month

def day_of_year(day, month, year):
    total = 0
    for i in range(1, month):
        total += days_in_month(i+1, year)
    total += day
    return total