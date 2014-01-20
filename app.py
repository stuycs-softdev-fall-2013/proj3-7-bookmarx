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
    d = { 'logged_in' : False }
    return render_template("welcome.html", d=d)

@app.route("/", methods=["GET", "POST"])
def home():
    if 'user_id' not in session:
        return redirect(url_for("welcome"))

    d = {}
    d['logged_in'] = True
    d['user'] = User(session['user_id'])
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
        d = { 'logged_in' : False }
        return render_template("register.html", d=d)

    user = User(session['user_id'])
    user.username = request.form['usern']
    t = Tag("Search engines")
    user.tags.append(t)
    b = Bookmark("Google", "http://google.com")
    b.tags.append(t)
    t.bookmarks.append(b)
    b.unload()
    t.unload()
    user.unload()
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    if 'user_id' in session:
        del session['user_id']
    return redirect(url_for('home'))

@app.route("/action", methods=["POST"])
def action():
    if 'action' not in request.form:
        return "error: no action"

    action = request.form['action']
    if action == 'make-bookmark':
        b = Bookmark(request.form['title'], request.form['link'])
        b.creator = request.form['user_id']
        b.unload()
        print "make-bookmark %s %s"%(request.form['title'], request.form['link'])
        return "Bookmark created."

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
