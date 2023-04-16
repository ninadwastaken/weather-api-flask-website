from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pandas.read_csv("")
    temperature = 2313
    return str(temperature)


if __name__ == "__main__":
    app.run(debug=True)
