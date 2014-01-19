from flask import Flask
from flask import render_template, url_for, request, session, redirect
from models import user, tag, bookmark
from models.user import User
from models.tag import Tag
from models.bookmark import Bookmark

app = Flask(__name__)
app.secret_key = "wacky potato fingers"

@app.route("/welcome")
def welcome():
	if 'usern' in session:
		return redirect(url_for('home'))
	return render_template("welcome.html")

@app.route("/", methods=["GET", "POST"])
def home():
	if 'usern' not in session:
	    return redirect(url_for("welcome"))

	d = {}
	d['user'] = user.User(session['usern'])
	t = tag.Tag()
	d['user'].tags.append(t)
	b = bookmark.Bookmark()
	b.link = "http://google.com"
	b.title = "Googggggggle"
	t.bookmarks.append(b)
	b.tags.append(t)
	t.unload()
	b.unload()
	return render_template("home.html", d=d)

@app.route("/login", methods=["POST"])
def login():
	# TODO add usern / id verification (requires db)
	if 'usern' not in request.form or 'user_id' not in request.form:
		return redirect(url_for('welcome'))

	session['usern'] = request.form['usern']
	session['user_id'] = request.form['user_id']
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
