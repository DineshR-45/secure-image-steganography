# Secure Data Hiding in Image Using Steganography

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates how to securely hide data within an image using steganography. The Least Significant Bit (LSB) method is used to embed data into the image, ensuring that the changes are invisible to the naked eye. Optionally, the data can be encrypted for added security.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Running Tests](#running-tests)
- [Future Scope](#future-scope)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Data Embedding**: Hide text or files within an image.
- **Data Extraction**: Extract hidden data from the image.
- **Encryption**: Optional encryption for enhanced security.
- **Invisibility**: No visible changes to the image after embedding data.

## Technologies Used
- **Python**: The primary programming language used for implementing the steganography algorithm.
- **OpenCV**: Used for image processing tasks such as reading and manipulating image pixels.
- **NumPy**: Used for numerical operations and handling multi-dimensional arrays (e.g., image pixel data).
- **PIL (Python Imaging Library)**: Used for image manipulation tasks like opening, saving, and converting image formats.
- **Cryptography**: Used for optional data encryption to enhance the security of the hidden data.

## Requirements
To run this project, you need the following Python libraries:
- `opencv-python` (for image processing)
- `numpy` (for numerical operations)
- `pillow` (for image manipulation)
- `cryptography` (for optional data encryption)

## Installation
You can install all the required libraries using `pip`. Run the following command:

```bash
pip install opencv-python numpy pillow cryptography
```

## Usage

1.Embed Data into an Image:

```bash
python steganography.py --embed --image input_image.png --output output_image.png --data "This is a secret message!"
```
2.Extract Data from an Image:

```bash
python steganography.py --extract --image output_image.png
```
3.Optional Encryption:

To encrypt the data before embedding:

```bash
python steganography.py --embed --image input_image.png --output output_image.png --data "This is a secret message!" --encrypt
```

To decrypt the extracted data:
```bash
python steganography.py --extract --image output_image.png --decrypt
```

## Screenshots

Original Image:
[Original Image]([Screenshots/Original_image.png](https://github.com/DineshR-45/secure-image-steganography/blob/main/input_image.png))

Image with Embedded Data:
Embedded Image

Extracted Data:
Extracted Data

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest tests/test_steganography.py
```

###Future Scope

Support for audio and video steganography.

Advanced encryption algorithms (e.g., AES).

User-friendly GUI or web application.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

For more details, read our Contribution Guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/DineshR-45/secure-image-steganography/blob/main/LICENSE) file for details.

## Acknowledgments
Thanks to [OpenCV](https://opencv.org/) for image processing tools.

Inspired by this [steganography tutorial](https://www.geeksforgeeks.org/image-steganography-using-opencv-in-python/)
