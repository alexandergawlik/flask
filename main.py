from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reviewform.html', form=form)
if __name__ == '__main__':
  app.run()
