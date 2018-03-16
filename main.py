from flask import Flask,render_template, request
#from wtforms import Form, TextAreaField, validators


app = Flask(__name__)


@app.route('/results')
def index():
    return render_template('results.html')
if __name__ == '__main__':
  app.run()
