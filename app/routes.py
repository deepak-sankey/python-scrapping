# routes.py

from flask import render_template
from flask import request, jsonify

from app import app
from app.web_scraper import scrape

# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/getAmazonProducts', methods=['POST'])
def getAmazonProducts():
    responseData = scrape()
    print(responseData)
    
    return jsonify(responseData), 200
