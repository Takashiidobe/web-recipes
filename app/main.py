from flask import Flask, request, render_template
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
    template = render_template('index.html', 
        title=r.title(), 
        total_time=r.total_time(),
        ingredients=r.ingredients(),
        instructions=r.instructions().splitlines(),
        image=r.image(),
    ) 
    return template
