# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask import render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        result = request.form
        return render_template('index.html', result = result)
    return render_template('index.html', result = {})



if __name__ == '__main__':
    app.run()
