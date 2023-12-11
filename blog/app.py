from flask import Flask, render_template



app =Flask(__name__)


@app.route("/")
def frontpage():
    return "ok"

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

@app.route("/login")
def loginpage():
    pass

@app.route("/logout")
def logoutpage():
    pass

