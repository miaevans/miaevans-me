from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('hello.html')

@app.route("/hpstuff")
def hpstuff():
	return render_template('hpstuff.html')

if __name__ == "__main__":
    app.run()
