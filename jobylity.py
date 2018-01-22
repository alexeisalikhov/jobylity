import json
import requests

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    url = 'https://feed.jobylon.com/feeds/7d7e6fd12c614aa5af3624b06f7a74b8/?format=json'
    jobs = ((x['title'], x['urls']['ad']) for x in requests.get(url).json())
    return render_template('jobs.html', jobs=jobs)




if __name__ == '__main__':
    app.run()
