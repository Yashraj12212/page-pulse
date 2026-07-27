# Page Pulse ⚡

Page Pulse is a lightweight, full-stack web application that audits any URL and returns basic SEO and performance metrics. It focuses on robust error handling, defensive programming, and a minimalist user interface.

## Features

* **Performance Metrics:** Checks HTTP status codes and measures response times.
* **SEO Basics:** Extracts page title, meta description, and counts `<h1>` tags.
* **Accessibility:** Counts the number of `<img>` tags missing `alt` attributes.
* **Content:** Calculates an approximate word count of the visible text.
* **Robust Error Handling:** Gracefully handles invalid URLs, timeouts, and non-HTML responses without crashing.

## Tech Stack

* **Backend:** Python, Flask
* **Web Scraping:** `requests`, `beautifulsoup4`
* **Frontend:** Vanilla HTML, CSS, JavaScript

## Setup & Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Yashraj12212/page-pulse.git
   cd page-pulse
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the local development server:

   ```bash
   python app.py
   ```

   Open the app in your browser at http://127.0.0.1:5000/.

4. Run unit tests:

   ```bash
   python -m unittest test_auditor.py
   ```

## API Contract

### Request

`GET /api/audit?url=<URL>`

**Query Parameters:**

* `url` *(string, required)*: The full URL to audit. Must include a valid schema (`http://` or `https://`).

### Response (200 OK)

Returns a JSON object containing the audit metrics.

```json
{
  "url": "https://example.com",
  "status_code": 200,
  "response_time_seconds": 0.42,
  "title": "Example Domain",
  "meta_description": null,
  "h1_count": 1,
  "missing_alt_images": 0,
  "word_count": 21,
  "error": null
}
```

### Error Response (400 Bad Request)

Returns a JSON object detailing the failure reason, such as invalid URL format, non-HTML content, or timeout.

```json
{
  "error": "Invalid URL format. Please include http:// or https://"
}
```

## Core Design Decisions

1. **Explicit Request Timeout (`timeout=5`)**

   Network requests to third-party sites can hang indefinitely if a server is unresponsive. Hardcoding a 5-second timeout keeps the API responsive and avoids tying up worker threads on dead links.

2. **Server-side Content-Type Pre-check**

   Attempting to parse binary files such as PDFs, ZIPs, or images with BeautifulSoup can waste memory and cause parser failures. The app checks the `Content-Type` header first and aborts early when the response is not HTML.

3. **Vanilla JavaScript Frontend + Flask Backend**

   The project stays intentionally lightweight by avoiding heavy frontend frameworks and complex backend tooling. Flask plus vanilla JavaScript keeps the codebase readable, fast to load, and easy to maintain.
