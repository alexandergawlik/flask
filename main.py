from flask import Flask,render_template, request
from wtforms import Form, TextAreaField, validators


app = Flask(__name__)

class ReviewForm(Form):
    moviereview = TextAreaField('',[validators.DataRequired()])

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('thanks.html', form=form)
if __name__ == '__main__':
  app.run()
