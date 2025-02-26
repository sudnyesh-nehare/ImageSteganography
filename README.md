# Secure Data Hiding in Images Using Steganography

This project hides secret messages in images using steganography techniques.

## Description
A Python-based tool to embed and extract data in images securely.

## How to Install
1. Install Python 3.x.
2. Run: `pip install opencv-python pycryptodome`

## How to Use
- To hide data: `python hide_message.py --image host.png --message "secret text"`
- To extract data: `python extract_message.py --image host.png`

## Requirements
- Python 3.8+
- Libraries: OpenCV, PyCryptoDome

#Test Your Project
Hide the Message:
  Open a terminal in your stego_project folder.
  Run: python hide_message.py.
  Check for output.png and note the key printed (e.g., 1a2b3c...).
Extract the Message:
  Edit extract_message.py and replace "your_key_here" with the key from the last step.
  Run: python extract_message.py.
  You should see “Hello, this is secret!” printed.

## License
MIT License
