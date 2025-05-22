import sys
import os

# ✅ Add root project folder to Python's module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import csv
import time
from phishing_detector.detector import is_phishing_url

# 🌐 Sample phishing feed (can be upgraded later)
PHISH_FEED_URL = "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links.txt"
LOG_FILE = "logs/phish_feed_scan_log.csv"

# 📝 Ensure log file exists with headers
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "url", "is_phishing", "confidence"])

# 🔍 Download live phishing URLs and scan them
def collect_and_scan():
    print("🌐 Fetching phishing URLs...")
    response = requests.get(PHISH_FEED_URL)
    urls = response.text.splitlines()

    for url in urls[:20]:  # limit to 20 for now
        if not url or url.startswith("#"):  # Skip empty or commented lines
            continue

        result = is_phishing_url(url)
        print(f"[{result['confidence']}%] {result['url']} → {'PHISHING' if result['is_phishing'] else 'SAFE'}")

        with open(LOG_FILE, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime("%Y-%m-%d %H:%M:%S"),
                result["url"],
                result["is_phishing"],
                result["confidence"]
            ])

if __name__ == "__main__":
    collect_and_scan()

