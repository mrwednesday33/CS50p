def calculate(expression):
    x, op, z = expression.split()
    x, z = int(x), int(z)
    if op == '+':
        result = x + z
    elif op == '-':
        result = x - z
    elif op == '*':
        result = x * z
    elif op == '/':
        result = x / z
    return round(result, 1)

expression = input("Expression: ")
result = calculate(expression)
print(f"{result:.1f}")