from flask import Flask
from flask import render_template, url_for, request, session, redirect
import user
import tag
import bookmark

app = Flask(__name__)
app.secret_key = "wacky potato fingers"

@app.route("/", methods=["GET", "POST"])
def home():
	d = {}
	if 'usern' in session:
		d['loggedin'] = True

	if request.method == "GET":
		if 'action' in session:
			d['action'] = session['action']
			del session['action']
		return render_template("home.html", d=d)

	# POST
	d['action'] = 'login'
	d['loggedin'] = True
	session['usern'] = request.form['usern']
	session['pswd'] = request.form['pswd']
	return render_template("home.html", d=d)

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	
	form = request.form
	if True: #user.registerUser(form['usern'], form['pswd']):
		session['usern'] = form['usern']
		session['pswd'] = form['pswd']
		session['action'] = 'register'
		return redirect(url_for('home'))

@app.route("/logout")
def logout():
	if 'usern' in session:
		del session['usern']
	if 'pswd' in session:
		del session['pswd']
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
