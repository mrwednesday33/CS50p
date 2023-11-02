def convert(time):
    if 'am' in time or 'pm' in time:
        hours, minutes, am_pm = re.findall(r'\d+|\w+', time)
        hours = int(hours)% 12 + (12 if am_pm.lower() == 'pm' else 0)
    else:
        hours, minutes = time.split(':')
        hours = int(hours)
    return hours + float(minutes) / 60

def main():
    time_str = input("What time is it? ")
    time = convert(time_str)

    if 7 <= time < 11:
        print("breakfast time")
    elif 11 <= time < 14:
        print("lunch time")
    elif 17 <= time < 21:
        print("dinner time")

if __name__ == '__main__':
    main()