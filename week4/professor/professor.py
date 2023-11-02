import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        prompt = f"{x} + {y} = "
        attempts = 0
        while True:
            user_input = input(prompt)
            try:
                user_answer = eval(user_input)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    attempts += 1
                    if attempts == 3:
                        print(correct_answer)
                        break
                    else:
                        print("EEE")
            except ValueError:
                print("EEE")

        print(f"Your score is {score}/10")
        break

def get_level():
    while True:
        level_input = input("Level: ")
        if level_input in ("1", "2", "3"):
            return int(level_input)

def generate_integer(level):
     if level == 1:
         return random.randint(0, 9)
     elif level == 2:
         return random.randint(10, 99)
     elif level == 3:
         return random.randint(100, 999)
     else:
         raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
