from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Welcome to My Watchlist!"
#
# @app.route('/totoro')
# def hello_totoro():
#     return "<h1>Hello Totoro!</h1><img src='https://helloflask.com/totoro.gif'>"
#
# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'
#
# @app.route('/test')
# def test_url_for():
#     print(url_for('hello')) # generate url for view function 'hello'
#     print(url_for('user_page', name='gwen')) # output: /user/gwen
#     print(url_for('user_page', name='Emma')) # output: /user/Emma
#     print(url_for('test_url_for')) # output: /test
#     print(url_for('test_url_for', extra=1)) # output: /test?extra=1
#     return 'Test page'

name = 'Gwen Wu'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
