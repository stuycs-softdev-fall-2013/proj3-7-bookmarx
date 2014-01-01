from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
