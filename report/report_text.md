# Hands-On Assignment 2: Construct AI QR Code Generator with Python

Course: MSCS-633-M20 – Advanced Artificial Intelligence

Student: Ashish Bhanudas Mahajan

## 1. Objective

The application accepts a URL, displays its QR code, and saves it as a PNG. QR encoding is deterministic; no machine-learning model is required.

## 2. Implementation

The Python application uses Tkinter for URL entry, image display, and status messages. Validation checks HTTP/HTTPS syntax, hostnames, and ports, and rejects empty or malformed input without contacting the website.

The qrcode library uses automatic version fitting, medium error correction, 10-pixel modules, and a four-module border. Pillow supports the image preview, and pathlib saves output/qr_code.png relative to the script. Functions, type hints, docstrings, and focused comments keep the code readable. Input, capacity, and file errors produce clear messages.

## 3. Application Output

![QR Code Generator application output](../screenshots/application_output.png)

Figure 1. QR Code Generator application successfully generating a QR code from the GitHub repository URL.

## 4. Runtime Verification

Verified on macOS with Python 3.11.1, Tk 8.6, qrcode 8.2, and Pillow 11.3.0. Automated GUI checks confirmed that valid input displays and saves a QR code, while empty, malformed, and oversized input produces an error without closing the app.

All 14 unit tests, compilation, Ruff checks, and dependency checks passed. macOS Vision decoded the saved PNG to the exact repository URL. Figure 1 is the genuine application screenshot supplied by the student.

## 5. GitHub Repository

https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen

## 6. Conclusion

The project demonstrates URL validation, QR generation, GUI event handling, and modular Python development. The source code, dependency manifest, tests, and setup instructions are available in the repository.
