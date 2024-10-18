# Steganography Tool

A simple Python-based steganography tool that allows users to hide messages within image files using the Least Significant Bit (LSB) method. This tool is designed for educational purposes and demonstrates the basic principles of steganography.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

## Features

- Hide messages in PNG images
- Retrieve hidden messages from encoded images
- User-friendly command-line interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shreyasaraf01/Steganography.git
   cd Steganography
   
2. Create a virtual environment:
```bash
python -m venv env
```
3. Activate the virtual environment:

-> On Windows:
```bash
.\env\Scripts\activate
```
-> On macOS/Linux:
```bash
source env/bin/activate
```
4. Install required packages:

```bash
pip install pillow
```
## Usage
* Run the tool:
```bash
python steganography_tool.py
```
* Follow the prompts to enter the image path and the message you want to hide.

* To retrieve the hidden message, run the tool again and select the option to decode an image.

## How It Works
The tool uses the Least Significant Bit (LSB) method to encode messages within the pixel data of an image. By modifying the least significant bit of the color values of the image, the message is hidden without significantly altering the image's appearance.

Example
* Encoding a message:
 Enter the path to the image.
 Input the message to hide.

* Decoding a message:
 Enter the path to the encoded image.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please feel free to create a pull request or open an issue.
