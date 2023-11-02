import validators

def validate_email(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

email = input("Enter an email address: ")
validate_email(email)
