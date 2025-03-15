from flask import Flask, url_for, render_template
import os, sys
from flask_sqlalchemy import SQLAlchemy # 导入扩展类
from markupsafe import escape

app = Flask(__name__)

prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控

# 在扩展类实例化前加上配置
db = SQLAlchemy(app)

# 创建数据库模型
class User(db.Model): # 表名是user（自动生成，小写处理）
    # noinspection PyInterpreter
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(20)) # 名字

class Movie(db.Model): # 表名movie
    id = db.Column(db.Integer, primary_key=True) # 主键
    title = db.Column(db.String(20)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份


# 和flask shell类似，我们可以编写一个自定义命令来自动执行创建数据库表操作
import click

@app.cli.command() # 注册为命令，可以传入name参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.') # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop: # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.') # 输出提示信息

# 测试常见的数据库操作
# 创建，读取，更新，删除

# 在程序里操作数据库

# 在主页视图读取数据库记录
@app.route('/')
def index(): # 因为设置了数据库，负责显示主页的index可以从数据库里读取真实的数据
    user = User.query.first() # 读取用户记录
    movies = Movie.query.all() # 读取所有电影记录
    return render_template('index.html', user=user, movies=movies)

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

# 生成虚拟数据
# 因为有了数据库，我们可以编写一个命令函数把虚拟数据添加到数据库

import click
@app.cli.command()
def forge():
    """Generate fake data"""
    db.create_all()

    # 全局的两个变量移动到这个函数内
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

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done')
#
# @app.route('/')
# def index():
#     return render_template('index.html', name=name, movies=movies)
#
