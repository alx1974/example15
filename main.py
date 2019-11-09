from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Hello Message!"
    current_year = datetime.datetime.now().year
    cities = ["Wien", "Salzburg", "Linz", "Graz"]
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html", methods=["GET"])
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)
        return render_template("success.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()
