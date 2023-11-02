text = input("Input: ")
vowels = "AEIOUaeiou"
new_text = ""

for char in text:
    if char not in vowels:
        new_text += char

print(new_text)