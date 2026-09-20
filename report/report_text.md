# Hands-On Assignment 2: Construct AI QR Code Generator with Python

Course: MSCS-633-M20 – Advanced Artificial Intelligence

Student: Ashish Bhanudas Mahajan

## 1. Objective

The application accepts a URL and produces a machine-readable QR code that can be displayed and saved as a PNG. The assignment uses the title “AI QR Code Generator”; the implementation performs deterministic QR encoding and does not use a machine-learning model.

## 2. Implementation

Python provides the application logic, while Tkinter supplies the URL field, Generate QR Code button, image preview, and status messages. URL validation uses urllib.parse with hostname and port checks. It accepts HTTP and HTTPS addresses, trims surrounding whitespace, and rejects empty or malformed input. Validation does not check website availability.

The qrcode library uses an automatically fitted QR version, medium error correction, box size 10, and border 4. Pillow supports the preview. pathlib creates the output directory and saves output/qr_code.png relative to the script. The GUI retains its PhotoImage reference so the image remains visible. Invalid input, oversized data, and saving/display errors produce messages instead of terminating the application.

## 3. Application Output

SCREENSHOT REQUIRED — Insert the genuine running-application screenshot here before submission.

Launch the app, enter the repository URL shown in section 5, and click Generate QR Code. Capture the window with the URL, QR code, and success message visible. Save it as screenshots/application_output.png and replace this placeholder in Word.

Figure 1. QR Code Generator application successfully generating a QR code from the GitHub repository URL. (Caption prepared; screenshot pending.)

## 4. Runtime Verification

Validation was performed on macOS using Python 3.11.1, Tk 8.6, qrcode 8.2, and Pillow 11.3.0. Dependency installation and pip check succeeded. The actual Tkinter window launched and its Generate button callback was exercised with valid, empty, malformed, and oversized input. The valid repository URL produced a visible preview and a non-empty saved PNG. Invalid input and oversized data displayed errors without closing the app.

The saved PNG was independently decoded with the built-in macOS Vision framework, which returned the exact repository URL. All 10 unittest tests passed. Python compilation and Ruff style/import checks passed. The GUI smoke check was automated; student manual review and phone scanning are not claimed. macOS rejected the screenshot capture, so the only outstanding artifact step is capturing the live window and inserting it into this report.

## 5. GitHub Repository

https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen

## 6. Conclusion

This implementation demonstrates URL validation, QR generation, modular Python functions, GUI event handling, and machine-readable output. The tests and setup instructions support reproducibility. Completing the screenshot evidence will make the report ready for final student review and submission.
