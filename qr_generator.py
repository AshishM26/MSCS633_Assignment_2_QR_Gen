"""Generate, display, and save a QR code for an HTTP or HTTPS URL."""

import ipaddress
import re
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from urllib.parse import urlsplit

import qrcode
from PIL import Image, ImageTk
from qrcode.exceptions import DataOverflowError

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "qr_code.png"
VALIDATION_MESSAGE = "Enter a valid http:// or https:// URL with a hostname."


def validate_url(url: str) -> bool:
    """Check HTTP(S) URL syntax without contacting the website.

    Accept domain names, localhost, and IP addresses with optional ports.
    Reject credentials and embedded whitespace; trim surrounding whitespace.
    """
    url = url.strip()
    if not url or any(
        character.isspace() or ord(character) < 32 or ord(character) == 127
        for character in url
    ):
        return False
    try:
        parts = urlsplit(url)
        host = parts.hostname
        if parts.scheme not in {"http", "https"} or not host:
            return False
        if parts.username is not None or parts.password is not None:
            return False
        # Accessing port also detects malformed or out-of-range port numbers.
        if parts.port is not None and not 1 <= parts.port <= 65535:
            return False
        if parts.netloc.endswith(":"):
            return False
        # Bracketed IPv6 hosts may only be followed by an optional port.
        if parts.netloc.startswith("[") and not re.fullmatch(
            r"\[[^\]]+\](?::[0-9]+)?", parts.netloc
        ):
            return False
        try:
            ipaddress.ip_address(host)
            return True
        except ValueError:
            pass
        # IDNA supports international domain names. One final DNS dot is valid.
        host = host.encode("idna").decode("ascii").removesuffix(".")
        if len(host) > 253:
            return False
        labels = host.split(".")
        return all(
            re.fullmatch(
                r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?",
                label,
            )
            for label in labels
        )
    except (ValueError, UnicodeError):
        return False


def generate_qr_code(url: str, output_path: Path = OUTPUT_PATH) -> Path:
    """Save a fitted QR code as PNG and return its absolute file path.

    Raise ValueError for invalid input or OSError when saving fails.
    DataOverflowError indicates that the URL exceeds QR capacity.
    """
    url = url.strip()
    if not validate_url(url):
        raise ValueError(VALIDATION_MESSAGE)
    qr_code = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr_code.add_data(url)
    try:
        qr_code.make(fit=True)
    except ValueError as error:
        # qrcode 8.2 can report capacity overflow as an invalid version.
        raise DataOverflowError("URL exceeds QR capacity") from error
    image = qr_code.make_image(fill_color="black", back_color="white")
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="PNG")
    return output_path


class QRCodeGeneratorApp:
    """A small Tkinter interface for the QR generator functions."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("QR Code Generator")
        root.geometry("780x760")
        root.minsize(780, 760)
        self.photo: ImageTk.PhotoImage | None = None
        self.url = tk.StringVar()
        self.status = tk.StringVar(value="Enter a URL to create your QR code.")
        self.details = tk.StringVar()
        frame = ttk.Frame(root, padding=24)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="QR Code Generator", font=("Helvetica", 24, "bold")).pack(
            anchor="w"
        )
        ttk.Label(frame, text="MSCS-633 Hands-On Assignment 2").pack(
            anchor="w", pady=(4, 20)
        )
        ttk.Label(frame, text="URL (http:// or https://)").pack(anchor="w")
        entry = ttk.Entry(frame, textvariable=self.url, font=("Helvetica", 13))
        entry.pack(fill="x", pady=(6, 12))
        entry.focus_set()
        self.generate_button = ttk.Button(
            frame, text="Generate QR Code", command=self.generate
        )
        self.generate_button.pack(anchor="w")
        root.bind("<Return>", lambda event: self.generate())
        self.preview = ttk.Label(
            frame, text="Your QR code will appear here", anchor="center"
        )
        self.preview.pack(fill="both", expand=True, pady=12)
        self.status_label = ttk.Label(frame, textvariable=self.status, wraplength=730)
        self.status_label.pack(anchor="w", pady=(0, 8))
        ttk.Label(frame, textvariable=self.details, wraplength=730).pack(anchor="w")

    def generate(self) -> None:
        """Handle input and report validation, capacity, or file errors."""
        self.preview.configure(image="", text="Your QR code will appear here")
        self.photo = None
        self.details.set("")
        url = self.url.get().strip()
        if not url:
            self.show_error("Enter a URL before generating a QR code.")
            return
        try:
            output_path = generate_qr_code(url)
            with Image.open(output_path) as image:
                # Keep module edges sharp when shrinking a large preview.
                image.thumbnail((410, 410), Image.Resampling.NEAREST)
                self.photo = ImageTk.PhotoImage(image)
        except DataOverflowError:
            self.show_error("This URL is too long for a QR code. Use a shorter URL.")
            return
        except ValueError:
            self.show_error(VALIDATION_MESSAGE)
            return
        except (OSError, tk.TclError) as error:
            self.show_error(f"Unable to save or display the QR code: {error}")
            return
        # Keep the PhotoImage on self; Tk does not retain a Python reference.
        self.preview.configure(image=self.photo, text="")
        self.status_label.configure(foreground="#176b35")
        self.status.set("Success! QR code generated and saved.")
        self.details.set(f"Encoded URL: {url}\nSaved to: {output_path}")

    def show_error(self, message: str) -> None:
        """Show an actionable message without closing the application."""
        self.status_label.configure(foreground="#b3261e")
        self.status.set(message)


def main() -> None:
    """Launch the desktop application."""
    root = tk.Tk()
    QRCodeGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
