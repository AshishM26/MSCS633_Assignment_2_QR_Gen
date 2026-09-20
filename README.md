# MSCS-633 Hands-On Assignment 2
## QR Code Generator with Python

### Overview
A small Python desktop application that turns an HTTP or HTTPS URL into a QR code, displays it, and saves a PNG. Author: Ashish Bhanudas Mahajan. Course: MSCS-633-M20 — Advanced Artificial Intelligence.

### Assignment Objective
Build a working URL-to-QR application with readable source, dependencies, runtime evidence, and a Word report. Although the assignment title uses “AI QR Code Generator,” QR encoding is a deterministic data-encoding process; this project uses no machine-learning model.

### Features
- Enter a URL and click **Generate QR Code** or press Enter.
- Validate the scheme, hostname, and optional port; show clear input errors.
- Generate a black-and-white QR with automatic version fitting, medium error correction, 10-pixel modules, and a four-module border.
- Display the result and show its encoded URL and absolute output path.
- Handle invalid input, QR capacity limits, and file/display errors.

### Project Structure
```text
MSCS633_Assignment_2_QR_Gen/
├── qr_generator.py
├── requirements.txt
├── README.md
├── .gitignore
├── output/qr_code.png
├── screenshots/application_output.png
├── report/
│   ├── MSCS633_Hands_On_Assignment_2_Report.docx
│   └── report_text.md
└── tests/test_qr_generator.py
```
### Technologies Used
Python, Tkinter/ttk, qrcode, Pillow, pathlib, urllib.parse, and unittest. Runtime packages are pinned in `requirements.txt`; tests use the standard library. Tkinter is supplied by Python/your operating system, not pip.

### Prerequisites
Python 3.10 or newer with Tkinter and a graphical desktop. Tested on macOS with Python 3.11.1 and Tk 8.6. Check Tk with `python -m tkinter`. If unavailable, use a Python installation with Tk support; on Ubuntu/Debian install the matching `python3-tk` package. Internet is needed for dependency installation, but QR generation works offline.

### Installation
```bash
git clone https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen.git
cd MSCS633_Assignment_2_QR_Gen
```
macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If PowerShell activation is restricted, use `.venv\Scripts\python.exe` in place of `python` below.

Install dependencies:
```bash
python -m pip install -r requirements.txt
```
In VS Code, open this folder and select `.venv` as the Python interpreter.

### Running the Application
```bash
python qr_generator.py
```
Enter an HTTP/HTTPS URL, then click **Generate QR Code**. Empty or malformed input displays an error without closing the application. Surrounding whitespace is trimmed; embedded whitespace and credentials are rejected. Localhost, IP addresses, and internationalized hostnames are supported. Validation checks syntax, not whether the website exists or is safe.

### Example
Use:
```text
https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen
```
Click **Generate QR Code** to display and save the result.

### Testing
```bash
python -m unittest discover -s tests -v
python -m compileall -q qr_generator.py tests
python -m pip check
```
All 14 tests passed, covering URL validation, PNG generation, file errors, and preservation of existing output after invalid input.

Optional development-only lint checks (Ruff is not needed to run the app):
```bash
python -m pip install ruff==0.16.8
python -m ruff check --select E,F,I --line-length 88 qr_generator.py tests
python -m ruff format --check qr_generator.py tests
```
The live GUI passed automated checks for valid and invalid input. macOS Vision decoded the saved PNG to the exact repository URL.

### Output
`output/qr_code.png` is saved relative to the script, regardless of the terminal's current folder. Each successful generation replaces the previous PNG. Invalid input clears the preview but leaves any previously saved PNG unchanged.

### Application Screenshot
![Running QR Code Generator application](screenshots/application_output.png)

The student-provided screenshot is also embedded in the Word report.

### Repository
https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen

### Submission
Attach [the Word report](report/MSCS633_Hands_On_Assignment_2_Report.docx) in Blackboard and share the repository URL above. The repository includes the Python source, dependency manifest, tests, and application screenshot.

### Learning Outcomes
Practice separating validation and QR generation from GUI event handling, managing dependencies, handling errors, testing reusable functions, and documenting a reproducible desktop application.

### Technical References
- [qrcode package documentation](https://pypi.org/project/qrcode/)
- [Python URL parsing documentation](https://docs.python.org/3/library/urllib.parse.html)
