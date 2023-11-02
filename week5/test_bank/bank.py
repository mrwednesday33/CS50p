def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    user_greeting = input("Please input a greeting: ")
    print(f"${value(user_greeting)}")

if __name__ == "__main__":
    main()