import sys
import random
from pyfiglet import Figlet

def print_usage():
    print("Invalid usage")
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        f = Figlet(font=random.choice(Figlet().getFonts()))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font_name = sys.argv[2]
            if font_name not in Figlet().getFonts():
                print_usage()
            f= Figlet(font=font_name)
        else:
            print_usage()
    else:
        print_usage()

    text = input("Enter text: ")

    print(f.renderText(text))

if __name__ == "__main__":
    main()
