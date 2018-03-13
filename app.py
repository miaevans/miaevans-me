from flask import Flask
from flaskrun import flaskrun
from flask import render_template


app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')
    
@app.route("/hello2")
def hello2():
	return render_template('hello2.html')

@app.route("/hpstuff")
def hpstuff():
	return render_template('hpstuff.html')

@app.route("/hp_knuts_converter")
def hp_knuts_converter():
	return render_template('hp_knuts_converter.html')

@app.route("/hp_survival")
def hp_survival():
	return render_template('hp_survival.html')

if __name__ == "__main__":
    flaskrun(app)
