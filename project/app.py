
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


@app.route('/blogs')
def blog():
    posts = [page for page in pages if 'date' in page.meta]
    # sort pages
    sorted_pages = sorted(posts, reverse=True, key=lambda page: page['date'])
    return render_template('index.html', pages=sorted_pages)


@app.route('/about')
def about():
    page_return = pages.get_or_404('about')
    return render_template('about.html', page=page_return)


@app.route('/resume/')
def resume():
    page_return = pages.get_or_404('resume')
    return render_template('resume.html', page=page_return)


@app.route('/blogs/<path:path>')
def page(path):
    page_return = pages.get_or_404(path)
    return render_template('blog.html', page=page_return)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5012))
    app.run(port=port)
