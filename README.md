# Secure Data Hiding in Image Using Steganography

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project demonstrates how to securely hide data within an image using steganography. The Least Significant Bit (LSB) method is used to embed data into the image, ensuring that the changes are invisible to the naked eye. Optionally, the data can be encrypted for added security.

## Features
- **Data Embedding**: Hide text or files within an image.
- **Data Extraction**: Extract hidden data from the image.
- **Encryption**: Optional encryption for enhanced security.
- **Invisibility**: No visible changes to the image after embedding data.

## Requirements
To run this project, you need the following Python libraries:
- `opencv-python` (for image processing)
- `numpy` (for numerical operations)
- `pillow` (for image manipulation)
- `cryptography` (for optional data encryption)

### Installation
You can install all the required libraries using `pip`. Run the following command:

```bash
pip install opencv-python numpy pillow cryptography

## Technologies Used
- **Python**: Programming language.
- **OpenCV**: Image processing.
- **NumPy**: Numerical operations.
- **PIL (Python Imaging Library)**: Image manipulation.
- **Cryptography**: Optional data encryption.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DineshR-45/secure-image-steganography.git
   cd secure-image-steganography
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python numpy pillow cryptography
   ```

## Usage
1. **Embed Data into an Image**:
   - Place the image you want to use in the project directory (e.g., `input_image.png`).
   - Run the following command to embed data:
     ```bash
     python steganography.py --embed --image input_image.png --output output_image.png --data "This is a secret message!"
     ```

2. **Extract Data from an Image**:
   - Run the following command to extract data:
     ```bash
     python steganography.py --extract --image output_image.png
     ```

3. **Optional Encryption**:
   - To encrypt the data before embedding, use the `--encrypt` flag:
     ```bash
     python steganography.py --embed --image input_image.png --output output_image.png --data "This is a secret message!" --encrypt
     ```
   - To decrypt the extracted data, use the `--decrypt` flag:
     ```bash
     python steganography.py --extract --image output_image.png --decrypt
     ```
## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/DineshR-45/secure-image-steganography/commit/b2286e77fdc0413e3df8302e23457833533f9796) file for details.

## Future Scope
- Support for audio and video steganography.
- Advanced encryption algorithms (e.g., AES).
- User-friendly GUI or web application.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.


## Acknowledgments
- Thanks to [OpenCV](https://opencv.org/) for image processing tools.
- Inspired by [this steganography tutorial](https://www.geeksforgeeks.org/image-based-steganography-using-python/).

## Contact
For questions or feedback, feel free to reach out:  
- **Dinesh R**: [dineshrc1024@gmail.com](dineshrc1024@gmail.com)  
- **GitHub**: [DineshR-45](https://github.com/DineshR-45)  
```

