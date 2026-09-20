# Hands-On Assignment 2: Construct AI QR Code Generator with Python

Course: MSCS-633-M20 – Advanced Artificial Intelligence

Student: Ashish Bhanudas Mahajan

## 1. Objective

The application accepts a URL and produces a machine-readable QR code that can be displayed and saved as a PNG. The assignment uses the title “AI QR Code Generator”; the implementation performs deterministic QR encoding and does not use a machine-learning model.

## 2. Implementation

Python provides the application logic, while Tkinter supplies the URL field, Generate QR Code button, image preview, and status messages. URL validation uses urllib.parse with hostname and port checks. It accepts HTTP and HTTPS addresses, trims surrounding whitespace, and rejects empty or malformed input. Validation does not check website availability.

The qrcode library uses an automatically fitted QR version, medium error correction, box size 10, and border 4. Pillow supports the preview. pathlib creates the output directory and saves output/qr_code.png relative to the script. The GUI retains its PhotoImage reference so the image remains visible. Invalid input, oversized data, and saving/display errors produce messages instead of terminating the application.

## 3. Application Output

![QR Code Generator application output](../screenshots/application_output.png)

Figure 1. QR Code Generator application successfully generating a QR code from the GitHub repository URL.

## 4. Runtime Verification

Validation was performed on macOS using Python 3.11.1, Tk 8.6, qrcode 8.2, and Pillow 11.3.0. Dependency installation and pip check succeeded. The actual Tkinter window launched and its Generate button callback was exercised with valid, empty, malformed, and oversized input. The valid repository URL produced a visible preview and a non-empty saved PNG. Invalid input and oversized data displayed errors without closing the app.

The saved PNG was independently decoded with the built-in macOS Vision framework, which returned the exact repository URL. All 14 unittest tests passed, including checks that invalid or oversized input preserves a previously generated PNG. Python compilation and Ruff style/import checks passed. The GUI smoke check was automated. Figure 1 is a genuine application screenshot supplied by the student, showing the repository URL, generated QR code, success message, and saved file path. No phone-scanning verification is claimed.

## 5. GitHub Repository

https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen

## 6. Conclusion

This implementation demonstrates URL validation, QR generation, modular Python functions, GUI event handling, and machine-readable output. The tests and setup instructions support reproducibility. The source code, dependency manifest, example PNG, and Word report with application screenshot provide the required submission artifacts.
