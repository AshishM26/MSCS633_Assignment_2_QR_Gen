"""Logic tests; no display server or additional test package is required."""

import tempfile
import unittest
from pathlib import Path

from PIL import Image
from qrcode.exceptions import DataOverflowError

from qr_generator import generate_qr_code, validate_url


class URLValidationTests(unittest.TestCase):
    def test_https_url(self):
        self.assertTrue(validate_url("https://github.com/AshishM26"))

    def test_http_url(self):
        self.assertTrue(validate_url("http://example.com/path?q=hello#top"))

    def test_empty_input(self):
        for url in ("", "   ", "\t\n"):
            with self.subTest(url=url):
                self.assertFalse(validate_url(url))

    def test_malformed_urls(self):
        for url in (
            "example.com",
            "https://",
            "https:///path",
            "ftp://example.com",
            "https://bad host.com",
            "https://-bad.com",
            "https://a..com",
            "https://example.com:abc",
            "https://example.com:99999",
            "https://example.com:",
            "https://[broken",
            "https://a\nb.com",
            "https://user:pass@example.com",
            "https://example.com/hi there",
        ):
            with self.subTest(url=url):
                self.assertFalse(validate_url(url))

    def test_supported_hosts(self):
        for url in (
            "https://example.com:443",
            "http://localhost:8000",
            "http://127.0.0.1",
            "http://[::1]",
            "https://bücher.de",
            "  https://example.com  ",
        ):
            with self.subTest(url=url):
                self.assertTrue(validate_url(url))


class QRGenerationTests(unittest.TestCase):
    def test_creates_nonempty_png_and_parent_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "qr.png"
            self.assertEqual(
                generate_qr_code("https://example.com", path), path.resolve()
            )
            self.assertGreater(path.stat().st_size, 0)
            with Image.open(path) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(image.width, image.height)
                self.assertEqual(image.convert("RGB").getpixel((0, 0)), (255, 255, 255))
            with Image.open(path) as image:
                image.verify()

    def test_invalid_url_does_not_create_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "qr.png"
            with self.assertRaises(ValueError):
                generate_qr_code("invalid", path)
            self.assertFalse(path.exists())

    def test_capacity_error(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaises(DataOverflowError),
        ):
            generate_qr_code(
                "https://example.com/" + "a" * 5000, Path(directory) / "qr.png"
            )

    def test_save_error(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaises(OSError),
        ):
            generate_qr_code("https://example.com", Path(directory))

    def test_surrounding_whitespace_is_trimmed(self):
        with tempfile.TemporaryDirectory() as directory:
            first = generate_qr_code("https://example.com", Path(directory) / "a.png")
            second = generate_qr_code(
                "  https://example.com  ", Path(directory) / "b.png"
            )
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == "__main__":
    unittest.main()
