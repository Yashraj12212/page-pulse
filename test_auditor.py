import unittest
from unittest.mock import patch, MagicMock
import requests
from auditor import audit_page

class TestAuditor(unittest.TestCase):

    @patch('requests.get')
    def test_happy_path(self, mock_get):
        """1. Happy Path: Valid HTML page parses metrics correctly."""
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'text/html; charset=utf-8'}
        mock_response.text = '''
            <html>
                <head><title>Test Page</title><meta name="description" content="A test description"></head>
                <body>
                    <h1>Main Heading</h1>
                    <img src="test.jpg"> <!-- missing alt -->
                    <img src="test2.jpg" alt="valid image">
                    <p>This is a test sentence with seven words.</p>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response

        # Call our function with a fake URL
        report = audit_page("https://fakeurl.com")

        self.assertEqual(report["status_code"], 200)
        self.assertEqual(report["title"], "Test Page")
        self.assertEqual(report["meta_description"], "A test description")
        self.assertEqual(report["h1_count"], 1)
        self.assertEqual(report["missing_alt_images"], 1)
        self.assertIsNone(report["error"])

    @patch('requests.get')
    def test_non_html_response(self, mock_get):
        """2. Failure Case 1: Handle non-HTML responses gracefully."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/pdf'} # Fake a PDF response
        mock_get.return_value = mock_response

        report = audit_page("https://fakeurl.com/document.pdf")

        # should trigger the specific error
        self.assertEqual(report["error"], "URL did not return HTML page.")

    @patch('requests.get')
    def test_network_timeout(self, mock_get):
        """3. Failure Case 2: Handle connection timeout cleanly."""
        mock_get.side_effect = requests.exceptions.Timeout()

        report = audit_page("https://slow-website.com")

        self.assertEqual(report["error"], "Failed to reach URL")

if __name__ == '__main__':
    unittest.main()