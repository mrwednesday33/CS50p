import qrcode

def main():
    print("Welcome to the QR Code Generator!")
    print("1. Generate URL QR Code")
    print("2. Generate Text QR Code")
    print("3. Generate Contact QR Code")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        url = input("Enter the URL: ")
        qr_img = generate_url_qr(url)
        qr_img.show()  # Display the QR code
        qr_img.save("url_qr.png")  # Save the QR code to a file
        print("QR Code generated and saved as 'url_qr.png'")
    elif choice == "2":
        text = input("Enter the TEXT: ")
        qr_img = generate_text_qr(text)
        qr_img.show()  # Display the QR code
        qr_img.save("text_qr.png")  # Save the QR code to a file
        print("QR Code generated and saved as 'text_qr.png'")
    elif choice == "3":
        contact = {
            "first_name": input("Enter First Name: "),
            "last_name": input("Enter Last Name: "),
            "phone": input("Enter Phone Number: "),
            "email": input("Enter Email: ")
        }
        qr_img = generate_contact_qr(contact)
        qr_img.show()  # Display the QR code
        qr_img.save("contact_qr.png")  # Save the QR code to a file
        print("QR Code generated and saved as 'contact_qr.png'")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

def generate_url_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def generate_text_qr(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def generate_contact_qr(contact):
    vcard = f"BEGIN:VCARD\n" \
            f"VERSION:3.0\n" \
            f"N:{contact['last_name']};{contact['first_name']}\n" \
            f"TEL:{contact['phone']}\n" \
            f"EMAIL:{contact['email']}\n" \
            f"END:VCARD"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(vcard)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

if __name__ == "__main__":
    main()
