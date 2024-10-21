from datetime import datetime

'''
print("What year do you want to check?")
year_input = int(input())
current_year = datetime.now().year
'''

def leap_year_check(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
        raise SystemExit(0)
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

'''
if year_input < current_year:
    print("Twas a " + ("leap" if leap_year_check(year_input) else "common") + " year")
elif year_input == current_year:
    print("Twis a " + ("leap" if leap_year_check(year_input) else "common") + " year")
else:
    print("Twill be a " + ("leap" if leap_year_check(year_input) else "common") + " year")
'''