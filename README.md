# Encrypt or Decrypt Files

This Python script provides a simple way to encrypt or decrypt files using the Fernet encryption algorithm. The script uses the cryptography library for encryption and decryption, and the alive_progress library for a progress bar.

## Getting Started

To use this script, you will need to have Python 3 installed on your computer. You can download and install Python from the official website: https://www.python.org/downloads/

You will also need to install the cryptography and alive_progress libraries. You can install them using the following commands:

```bash
pip install cryptography
pip install alive_progress

```

## Usage
To use the script, follow these steps:

Place the file you want to encrypt or decrypt in a directory named protect_file in the same directory as the script.
Run the script using the following command:

```python
python file_encrypt.py

```

Follow the on-screen instructions to either encrypt or decrypt the file.
The encrypted or decrypted file will be saved in the protect_file directory.

## Notes
This script uses the Fernet encryption algorithm, which is a symmetric encryption algorithm. This means that the same key is used for both encryption and decryption. The key is generated automatically by the script and saved in a file named encripted_text.key.
The encrypted file is saved in a file named encripted_text.txt.
The script checks if the file you want to encrypt or decrypt is the same as the previously encrypted or decrypted file. If it is, the script will delete the file and exit. If it is not, the script will encrypt or decrypt the file and save the result in a new file.
The script uses a progress bar to show the progress of the encryption or decryption process.
