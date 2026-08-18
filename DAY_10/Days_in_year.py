def is_leap(user_year):
    """Takes input the year and returns true if year is a leap year and false if its not a leap year"""
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_months(enter_year, enter_month):
    """Returns the number of days in a month correctly, taking in accout leap year or not"""
    if enter_year<0 or month < 1 or month > 12:
        return "Invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(enter_year) and enter_month == 2:
        return 29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)