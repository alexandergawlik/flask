from flask import Flask,render_template
#from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('thanks.html')
if __name__ == '__main__':
  app.run()
