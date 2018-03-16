from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
#from wtforms import Form, TextAreaField, validators
#import pickle
#import sqlite3
#import os
#import numpy as np
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#class ReviewForm(Form):
 #   moviereview = TextAreaField('',[validators.DataRequired()])
@app.route('/')
def index():
    #form = ReviewForm(request.form)
    return render_template('thanks.html')
if __name__ == '__main__':
  app.run()
