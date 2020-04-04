from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'TJ Salgado',
        'title': 'Blog Post 1',
        'content': 'First post content.',
        'date_posted': 'April 4th, 2020'
    },
    {
        'author': 'TJ Salgado',
        'title': 'Blog Post 1',
        'content': 'First post content.',
        'date_posted': 'April 4th, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')