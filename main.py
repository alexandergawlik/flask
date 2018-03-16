from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  form = ReviewForm(request.form)
    return render_template('reviewform.html', form = form)
if __name__ == '__main__':
  app.run()
