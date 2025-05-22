import sys, os
from datetime import datetime

# Add project root to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
from phishing_detector.detector import is_phishing_url

# Set template folder relative to this file
app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            result = is_phishing_url(url)

    # Pass year to the template
    year = datetime.now().year
    return render_template("index.html", result=result, year=year)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)


