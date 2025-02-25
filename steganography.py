import cv2
import numpy as np
from PIL import Image
from cryptography.fernet import Fernet
import argparse

# Generate a key for encryption (optional)
def generate_key():
    return Fernet.generate_key()

# Encrypt data (optional)
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data (optional)
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Embed data into an image using LSB method
def embed_data(image_path, data, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)

    data += "====="  # Adding a delimiter to mark the end of the data
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    data_len = len(binary_data)
    data_index = 0

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                if data_index < data_len:
                    pixels[i][j][k] = int(format(pixels[i][j][k], '08b')[:-1] + binary_data[data_index], 2)
                    data_index += 1

    output_img = Image.fromarray(pixels)
    output_img.save(output_path)
    print("Data embedded successfully!")

# Extract data from an image
def extract_data(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)

    binary_data = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                binary_data += format(pixels[i][j][k], '08b')[-1]

    delimiter = "====="
    data = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        data += chr(int(byte, 2))
        if delimiter in data:
            break

    data = data.split(delimiter)[0]
    print("Extracted data:", data)
    return data

# Main function
def main():
    parser = argparse.ArgumentParser(description="Secure Data Hiding in Image Using Steganography")
    parser.add_argument("--embed", action="store_true", help="Embed data into an image")
    parser.add_argument("--extract", action="store_true", help="Extract data from an image")
    parser.add_argument("--image", type=str, help="Path to the input image")
    parser.add_argument("--output", type=str, help="Path to save the output image")
    parser.add_argument("--data", type=str, help="Data to embed into the image")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the data before embedding")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the extracted data")
    args = parser.parse_args()

    if args.embed:
        if not args.image or not args.output or not args.data:
            print("Please provide input image, output path, and data to embed.")
            return

        data = args.data
        if args.encrypt:
            key = generate_key()
            print("Encryption Key:", key.decode())
            data = encrypt_data(data, key)

        embed_data(args.image, data, args.output)

    elif args.extract:
        if not args.image:
            print("Please provide the image to extract data from.")
            return

        extracted_data = extract_data(args.image)
        if args.decrypt:
            key = input("Enter the encryption key: ").encode()
            extracted_data = decrypt_data(extracted_data.encode(), key)

        print("Final Extracted Data:", extracted_data)

    else:
        print("Please specify --embed or --extract.")

if __name__ == "__main__":
    main()
