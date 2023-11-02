camel_case = input("Enter variable name in camel case: ")
snake_case = ""
for i, char in enumerate(camel_case):
    if i == 0:
        snake_case += char.lower()
    elif char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

        print("Snake case variable name:", snake_case)