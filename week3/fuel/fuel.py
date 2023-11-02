while True:
    try:
        fraction = input("Enter fuel fraction (X/Y): ")
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        if y == 0 or x > y:
            raise ValueError
        percentage = round(x / y * 100)
        if percentage <= 1:
            print('E')
        elif percentage >= 99:
            print('F')
        else:
            print(f'{percentage}%')
        break
    except ValueError:
        print('Invalid Input. Please enter fraction in the format X/Y where X and Y are integers and X ≤ Y (Y ≠ 0)')
