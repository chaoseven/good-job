from flask import render_template
from . import main

@main.route("/")
def index():
    return home('home')

def home(id):
    return render_template('main/index.html',active_item=id)

@main.route('/<id>')
def items(id):
    return render_template('main/items.html',active_item=id)

@main.route('/items/add_item')
def add_item():
    return render_template('main/add_item.html',active_item='items')
