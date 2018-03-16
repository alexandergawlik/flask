from flask import Flask,render_template, request
from wtforms import Form, StringField, TextAreaField, validators


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('reviewform.html')
if __name__ == '__main__':
  app.run()
