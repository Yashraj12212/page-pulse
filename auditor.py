import requests
import time
from bs4 import BeautifulSoup

def audit_page(url: str):

    report = {
        "url": url,
        "status_code": None,
        "response_time_seconds": None,
        "title": None,
        "meta_description": None,
        "h1_count": 0,
        "missing_alt_images": 0,
        "word_count": 0,
        "error": None
    }

    # making request
    try:
        start = time.time()
        res = requests.get(url,timeout =5)
        end = time.time()

        report["status_code"] = res.status_code
        report["response_time_seconds"] = round(end-start,2)

        if "text/html" not in res.headers.get("Content-Type",""):
            report["error"] = "URL did not return HTML page."
            return report
        
    except requests.RequestException as e:
        report["error"] = "Failed to reach URL"
        return report

    # HTML raw text to BeautifulSoup

    soup = BeautifulSoup(res.text, 'html.parser')

    if soup.title:
        report["title"] = soup.title.string
    
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        report["meta_description"] = meta_tag.get("content")
        
    h1_tags = soup.find_all("h1")
    report["h1_count"] = len(h1_tags)
    
    all_images = soup.find_all("img")
    missing_alt_count = 0

    for img in all_images:
        if not img.get("alt"):
            missing_alt_count += 1
    report["missing_alt_images"] = missing_alt_count
    
    # get_text() grabs all visible text.
    visible_text = soup.get_text(separator=' ')
    words = visible_text.split()
    report["word_count"] = len(words)

    return report


if __name__ == "__main__":
    target_url = "https://example.com"
    result = audit_page(target_url)
    print(result)