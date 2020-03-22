import os

from flask import (
    Flask, 
    render_template, 
    redirect
)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(f'/basic')

@app.route('/basic')
def basic():
    print("touch")
    return render_template('basic_charts.html')


#export FLASK_ENV=development
#export FLASK_DEBUG=1