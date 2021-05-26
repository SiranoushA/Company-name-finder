from flask import Flask
from flask import request
import requests
from lxml.html import fromstring

app = Flask(__name__)

@app.route("/")
def index():
    link = request.args.get("link", "")
    if link:
        company = get_name(link)
    else:
        company = ""
    return (
        """<form action="" method="get">
                Website URL: <input type="text" name="link">
                <input type="submit" value="Submit">
            </form>"""
        + "Company name: "
        + company
    )

def get_name(link):

    try:
        req = requests.get(str(link))
        tree = fromstring(req.content)
        company = tree.findtext('.//title')
        return str(company)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)