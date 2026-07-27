Page Pulse

Page Pulse is a lightweight, full-stack web application that audits any URL and returns basic SEO and performance metrics. It was built as a clean, simple tool with a focus on robust error handling and a minimalist user interface.

## Features
* **Performance Metrics:** Checks HTTP status codes and measures response times.
* **SEO Basics:** Extracts page title, meta description, and counts `<h1>` tags.
* **Accessibility:** Counts the number of `<img>` tags missing `alt` attributes.
* **Content:** Calculates an approximate word count of the visible text.
* **Robust Error Handling:** Gracefully handles invalid URLs, timeouts, and non-HTML responses (e.g., PDFs or images) without crashing.

## Tech Stack
* **Backend:** Python, Flask
* **Web Scraping:** `requests`, `beautifulsoup4`
* **Frontend:** Vanilla HTML, CSS, JavaScript

## How to Run Locally

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone <your-repo-url-here>
   cd page_pulse
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000/`.
