import os
import pytest
from PIL import Image
from project import generate_url_qr

def test_generate_url_qr():
    # Test generating a QR code for a URL
    url = "https://www.example.com"
    qr_img = generate_url_qr(url)

    # Check if the generated QR code image is not None
    assert qr_img is not None

    # Check if the generated QR code image has valid dimensions (you can adjust these as per your requirement)
    assert qr_img.size[0] > 100
    assert qr_img.size[1] > 100

    # You can also check the content of the QR code if you want (optional)
    # For example, if you have a known image of a QR code with the same URL,
    # you can compare the pixel content to check if they are similar.

if __name__ == "__main__":
    pytest.main()
