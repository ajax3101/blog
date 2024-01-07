import sqlite3
from flask import Flask, render_template, session, redirect, g
from forms import LoginForm


app =Flask(__name__)
app.secret_key='secret'

ADMIN_NAME = 'admin'
ADMIN_PASS = '123'
DATABASE = 'blog.sqlite'

@app.before_request
def global_vars():
    if session.get('logged_in'):
        g.logged = True

@app.route("/")
def frontpage():
    db = sqlite3.connect(DATABASE)
    posts = db.execute('select * from post').fetchall()
    return render_template('feed.html', posts=posts)

@app.route("/about")
def aboutpage():
    return render_template("about.html")

@app.route("/contact")
def contactpage():
    return render_template("contact.html")

@app.route("/post/<post_id>", endpoint="post")
def postpage(post_id):
    pass

@app.route("/post/<post_id>/edit", methods=["GET", "POST"], endpoint="edit")
def postedit(post_id):
    pass

@app.route("/post/new", methods=["GET", "POST"], endpoint="new")
def postnew():
    pass


@app.route("/login", endpoint='login', methods=["GET", "POST"] )
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        if form.name.data == ADMIN_NAME and form.password.data == ADMIN_PASS:
            session['logged_in'] = True
            return redirect('/')
    return render_template("login.html", form = form)

@app.route("/logout", endpoint="logout")
def logoutpage():
    session.pop('logged_in', None)
    return redirect('/')


