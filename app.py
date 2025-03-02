from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to My Watchlist!"

@app.route('/totoro')
def hello_totoro():
    return "<h1>Hello Totoro!</h1><img src='https://helloflask.com/totoro.gif'>"

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello')) # generate url for view function 'hello'
    print(url_for('user_page', name='gwen')) # output: /user/gwen
    print(url_for('user_page', name='Emma')) # output: /user/Emma
    print(url_for('test_url_for')) # output: /test
    print(url_for('test_url_for', extra=1)) # output: /test?extra=1
    return 'Test page'
