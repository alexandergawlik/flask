from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
from flask_bootstrap import Bootstrap
from nlpcloud import SpamClassifier

app = Flask(__name__)
x = SpamClassifier()
Bootstrap(app)
app.url_map.strict_slashes = False
class ReviewForm(Form):
    comment = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=15)])

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('commentform.html', form=form)

@app.route('/results.html', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['comment']
        #y, proba = classify(review)
        return render_template('results.html',
                                content=review)#,
        #                        prediction=y,
        #                        probability=round(proba*100, 2))
    return render_template('results.html', form=form)

@app.route('/thanks.html', methods=['POST'])
def feedback():
    #feedback = request.form['feedback_button']
    #review = request.form['review']
    #prediction = request.form['prediction']

    #inv_label = {'negatywna': 0, 'pozytywna': 1}
    #y = inv_label[prediction]
    #if feedback == 'Nieprawidłowa':
    #    y = int(not(y))
    #train(review, y)
    #sqlite_entry(db, review, y)
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
