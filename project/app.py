
from flask import Flask, render_template, make_response
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import os

app = Flask(__name__)
app.config.from_pyfile('setting.py')

pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/blog')
def blog():
    posts = [page for page in pages if 'date' in page.meta]
    # sort pages
    sorted_pages = sorted(posts)  # , reverse=True, key=lambda page: page['date']
    return render_template('index.html', pages=sorted_pages)


@app.route('/about')
def about():
    ret = make_response(render_template('about.html'))
    ret.headers['Content-Type'] = 'text/html; charset=utf-8'
    return ret


@app.route('/<path:path>/')
def page(path):
    page_return = pages.get_or_404(path)
    resp = make_response(render_template('page.html', page=page_return))
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(port=port)
