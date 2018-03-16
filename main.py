from flask import Flask,render_template
#from wtforms import Form, TextAreaField, validators

#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)

@app.route('/')
def index():
    return render_template('thanks.html')
if __name__ == '__main__':
  app.run()
