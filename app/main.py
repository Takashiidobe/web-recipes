from flask import Flask, request, render_template
from recipe_scrapers import scrape_me
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/", methods=['GET'])
def main():
    URL = request.args
    if URL:
        URL = URL.get('url')
    if not URL:
        return render_template('404.html')
    r = scrape_me(URL, wild_mode=True)
    template = render_template('index.html',
        title=r.title(),
        total_time=r.total_time(),
        ingredients=r.ingredients(),
        instructions=r.instructions().splitlines(),
        image=r.image(),
    )
    return template
