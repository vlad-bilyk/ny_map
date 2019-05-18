import sys
sys.path.append("..")
import runner
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='vendor')

# HOMEPAGE
@app.route("/")
def index():
    return render_template('home_page.html')

# NEW GENERATED MAP
@app.route("/uptodatemap", methods=["GET", "POST"])
def up_to_date_map():
    if request.method == "POST":
        try:
            day = request.form.get('day')
            print(day)
            runner.main(day)
            print('it worked')
            return redirect(url_for("generated_map"))
        except ValueError as e:
            print(e)
            print(day)
            return redirect(url_for("index"))

    print('it even got here')
    return render_template("my_map.html")


# OLD GENERATED MAP
@app.route("/generatedmap", methods=["GET", "POST"])
def generated_map():

    print('map is opening')
    return render_template("my_map.html")


if __name__ == "__main__":
    app.run(debug=True)
