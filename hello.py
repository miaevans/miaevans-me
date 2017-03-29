from flask import Flask
from flaskrun import flaskrun
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('hello.html')

@app.route("/hpstuff")
def hpstuff():
	return render_template('hpstuff.html')

@app.route("/hp_knuts_converter")
def hp_knuts_converter():
	return render_template('hp_knuts_converter.html')

if __name__ == "__main__":
    flaskrun(app)
