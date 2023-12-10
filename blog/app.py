from flask import Flask



app =Flask(__name__)


@app.route("/")
def frontpage():
    return "ok"

@app.route("/about")
def aboutpage():
    return render_template("about.html")

@app.route("/contact")
def contactpage():
    return "ok"

@app.route("/post/<post_id:int>", endpoint="post")
def postpage(post_id):
    pass

@app.route("/post/<post_id:int>/edit", method=["GET", "POST"], endpoint="edit")
def postedit(post_id):
    pass

@app.route("/post/new", method=["GET", "POST"], endpoint="new")
def postnew():
    pass

@app.route("/login")
def loginpage():
    pass

@app.route("/logout")
def logoutpage():
    pass

