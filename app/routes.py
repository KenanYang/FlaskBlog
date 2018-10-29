from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kenan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The movie is good!'
        },
        {
            'author': {'username': 'Tony'},
            'body': 'Suzy is cute!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
