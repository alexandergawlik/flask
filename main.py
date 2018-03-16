from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

class ReviewForm(Form):
    moviereview = TextAreaField('',[validators.DataRequired(), validators.lenght(min=15)])
@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html',form=form)
if __name__ == '__main__':
  app.run()
