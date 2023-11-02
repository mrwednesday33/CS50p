import datetime

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Rnter a date in MM/DD/YYYY order or in the form of a string like 'September 15, 1990': ")

    try:
        month, day, year = map(int, date_input.split("/"))
    except ValueError:
        month, day, year = None, None, None

    if month is None or day is None or year is None:
        try:
            date_parts = date_input.split()
            if len(date_parts) == 3:
                month_str, day_str, year_str = date_parts
                month = MONTHS.index(month_str) + 1
                day = int(day_str.strip(","))
                year = int(year_str)
            else:
                month_str, day_str, year_str = date_parts
                month = MONTHS.index(month_str) + 1
                day = 1
                year = int(year_str)
        except (ValueError, IndexError):
            month, day, year = None, None, None

    if month is None or day is None or year is None:
        print("Invalid date format. Please try again.")
        continue

    try:
        date = datetime.date(year, month, day)
    except ValueError:
        print("Invalid date. Please try again.")
        continue

    print(date.strftime("%Y-%m-%d"))
    break