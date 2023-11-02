# QR Code Generator

#### Video Demo: <https://youtube.com/shorts/qgEtjSC9g1M>

#### Description:

The QR Code Generator is a Python program that allows users to create various types of QR codes, including URLs, plain text, and contact information. The program provides an easy-to-use command-line interface, making it simple for users to generate and save QR codes for different purposes.

#### Features:

- Generate QR codes for URLs, plain text, and contact information (vCard format).
- Save the generated QR codes as image files (PNG) for future use.
- Clean and straightforward command-line interface for easy interaction.
- Tests to ensure the correctness of the QR code generation functions.

#### Installation:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/qr-code-generator.git

2. Navigate to the project directory:
    ```bash
    cd qr-code-generator

3. Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt

3. To generate a QR code, run the project.py script:
    ```bash
    python project.py

#### Instructions
Follow the on-screen instructions to choose the type of QR code you want to generate, enter the relevant information, and the program will create the QR code and display it. The generated QR code will also be saved as a PNG image file in the project directory.

#### Custom Functions
- generate_url_qr(url): Generates a QR code for a given URL.
- generate_text_qr(text): Generates a QR code for plain text.
- generate_contact_qr(contact): Generates a QR code for contact information in vCard format.

#### Dependencies
The project relies on the qrcode library for generating QR codes. The required dependencies are listed in the requirements.txt file.

#### Contributing
Contributions to the QR Code Generator project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to create a pull request or open an issue.