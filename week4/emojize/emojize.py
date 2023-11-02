import emoji

text = input("Enter a text in English: ")

emojized_text = emoji.emojize(text, delimiters=(":", ":"))

print(emojized_text)