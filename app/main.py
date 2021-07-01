from flask import Flask, jsonify, request
from recipe_scrapers import scrape_me
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def main():
    URL = request.args.get('url')
    if not URL:
        return None
    r = scrape_me(URL, wild_mode=True)
    dt = {}
    if r.title():
        dt['title'] = r.title()
    if r.total_time():
        dt['total_time'] = r.total_time()
    if r.yields():
        dt['yields'] = r.yields()
    if r.ingredients():
        dt['ingredients'] = r.ingredients()
    if r.instructions():
        dt['instructions'] = r.instructions()
    if r.image():
        dt['image'] = r.image()
    if r.nutrients():
        dt['nutrients'] = r.nutrients()
    return jsonify(dt) 
