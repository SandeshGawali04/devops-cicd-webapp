import unittest
from pathlib import Path

HTML_FILE = Path(__file__).resolve().parent.parent / "index.html"


class TestWebApplication(unittest.TestCase):

    def test_html_file_exists(self):
        self.assertTrue(HTML_FILE.exists())

    def test_page_title(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn("<title>DevOps Project Dashboard</title>", html)

    def test_dashboard_heading(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn("DevOps Project Dashboard", html)

    def test_application_status(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn("Application Running Successfully", html)


if __name__ == "__main__":
    unittest.main()
