import re

def validate(ip_address):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(pattern, ip_address):
        octets = ip_address.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True
    return False

def main():
    ip_address = input("Enter an IPv4 address: ")
    if validate(ip_address):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
