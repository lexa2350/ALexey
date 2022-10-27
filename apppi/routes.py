from apppi import app
from flask import render_template
from random import choice

menu = [{"name": 'Главная', "url": 'index'}, {"name": 'О программе', "url": 'about'}, {"name": 'Помощь', "url": 'help'}, {"name": 'ЛЕХА2350', "url": 'LEXA'}]


@app.route('/')
@app.route('/index')
def index():
    best_pi = {'username': 'Алексей  '}

    return render_template('index.html', title='2022 Forever', user=best_pi, menu=menu)


@app.route('/help')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp), menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', menu=menu)

@app.route('/LEXA')
def LEXA():
    return render_template('LEXA2350.html', menu=menu)