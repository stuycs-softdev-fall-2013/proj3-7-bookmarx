from flask import Flask
from flask import render_template, url_for, request, session, redirect
from models.user import User
from models.tag import Tag
from models.bookmark import Bookmark

app = Flask(__name__)
app.secret_key = "wacky potato fingers"

@app.route("/welcome")
def welcome():
	if 'user_id' in session:
		return redirect(url_for('home'))
	return render_template("welcome.html")

@app.route("/", methods=["GET", "POST"])
def home():
	if 'user_id' not in session:
	    return redirect(url_for("welcome"))

	d = {}
	d['user'] = User(session['user_id'])
	t = Tag("Search engines")
	d['user'].tags.append(t)
	b = Bookmark("http://google.com", "Googggggggle")
	b.tags.append(t)
	t.unload()
	b.unload()
	return render_template("home.html", d=d)

@app.route("/login", methods=["POST"])
def login():
	# TODO add id verification
	if 'user_id' not in request.form:
		return redirect(url_for('welcome'))

	session['user_id'] = request.form['user_id']
	user = User(session['user_id'])
	if user.username:
	    return redirect(url_for('home'))
	else:
	    return redirect(url_for('register'))

@app.route("/register", methods=["GET","POST"])
def register():
    if 'user_id' not in session:
        return redirect(url_for('welcome'))
    if request.method == "GET":
        return render_template("register.html")

    user = User(session['user_id'])
    user.username = request.form['usern']
    user.unload()
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
	if 'user_id' in session:
		del session['user_id']
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
