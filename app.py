
from flask import Flask,render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

app = Flask(__name__)


@app.route("/")
@app.route("/<category>")
def home(category="general"):
    url = f"{BASE_URL}?country=us&category={category}&apiKey={API_KEY}"
    result = requests.get(url).json()
    news = {
        "articles":result['articles']
    }
    categories = ["general","sports","entertainment","business","entertainment","technology"]
    return render_template("home.html",allNews=news,categories=categories,active_category=category)
# 2ae52e9d05e246f396d70ee6acc8f7e3


if __name__ == "__main__":
    app.run(debug=True)