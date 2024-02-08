from flask import render_template
from flask import Flask
from flask_flatpages import FlatPages
from datetime import datetime
import markdown

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True

app.config.from_object(__name__)
pages = FlatPages(app)
application = app
app.static_folder = 'static'

def get_published_date(article):
    # Convert the 'published' value to datetime.date object
    return datetime.strptime(article.meta['date'], '%Y/%m/%d').date()

@app.route('/')
def index():
    # Articles are pages with a publication date
    articles = [p for p in pages if 'published' in p.meta]

    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=get_published_date)
    return render_template('index.html', articles=latest)

# @app.route('/feuflask/cat/<cat_name>')
# def catlist(cat_name):
#     # Articles are pages with a publication date
#     articles = [p for p in pages if 'published' in p.meta and p.meta['category'] == cat_name]
#
#     # Render markdown content to HTML for each article
#     for article in articles:
#         article.html = markdown.markdown(article.body)
#
#     # Show the 10 most recent articles, most recent first.
#     latest = sorted(articles, reverse=True, key=lambda p: p.meta['published'])
#     return render_template('index.html', articles=latest, category=cat_name)
