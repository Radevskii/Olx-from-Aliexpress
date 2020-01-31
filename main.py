from flask import Flask
from flask import render_template, request, redirect, url_for

from User import user
from ad import ad

app = Flask(__name__)


@app.route("/")
def ads():
    return render_template("index.html", user=None,ads=ad.all())


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
        return redirect("/{}/".format(user.get_user_id(request.form['email'])))


@app.route("/<int:id>/new_ad/", methods=["GET", "POST"])
def add_ad(id):
    if request.method == "GET":
        return render_template('new_ad.html', user = user.get_user(id))
    elif request.method == "POST":
        values = (
            None,
            request.form['name_ad'],
            request.form['info_ad'],
            request.form['price'],
            id
        )
        ad(*values).add_ad()
        return redirect('/{}/'.format(id))


@app.route('/<int:id>/edit_ad/<int:id_ad>/', methods=['GET', 'POST'])
def edit_ads(id, id_ad):
    if request.method == "GET":
        return render_template("edit_ad.html", user=user.get_user(id), ad=ad.find(id_ad))
    elif request.method =="POST":
        values = (
            id_ad,
            request.form['name_ad'],
            request.form['info_ad'],
            request.form['price'],
            id
        )
        ad(*values).edit_ad()
        return redirect('/{}/'.format(id))


@app.route('/<int:id>/delete', methods=['POST'])
def delete_post(id):
    post = ad.find(id)
    User_name = user.get_user(post.user_id)
    post.delete()

    return render_template("index.html", user=User_name, ads = ad.all())





@app.route("/<int:id>/")
def print_hello(id):
    User_name = user.get_user(id)
    print(User_name)
    return render_template("index.html", user=User_name, ads = ad.all())


if __name__ == "__main__":
    app.run(debug=True)
