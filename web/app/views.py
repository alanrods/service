# views.py

from flask import render_template, request

from app import app

from preprocessing import *

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        not_normalized = request.form['tweet_text']
        normalized = preprocess(not_normalized)
        return render_template('text_result.html',classifier=normalized)
    return render_template('text.html')

@app.route('/tweet')
def tweet():
    return render_template('tweet.html')
