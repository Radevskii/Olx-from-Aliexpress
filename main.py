from flask import Flask
from flask import render_template, request, redirect, url_for

from User import user

app = Flask(__name__)

@app.route("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        mail = request.form['email']
        values = (
            None,
            request.form['name'],
            mail,
            user.hash_password(request.form['password']),
            request.form['phone_number'],
            request.form['address']
        )
        user(*values).add_user()

        return redirect("/{}/".format(user.get_user_id(mail)))

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        request.form['email'],
        request.form['password']
        return redirect("/{}/".format(user.get_user_id(request.form['email'])))



@app.route("/<int:id>/")
def print_hello(id):
    User_name=user.get_user(id)
    return render_template("index.html", user=User_name)

if __name__ == "__main__":
    app.run(debug=True)