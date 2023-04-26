from flask import Flask, render_template

mean = Flask(__name__)

@mean.route("/")
def home():
    return render_template("side_project.html")

@mean.route("/meaningapi/v1/<word>")
def meaning(word):
    return {"definition": word.upper(), "word": word}

if __name__ == "__main__":
    mean.run(debug=True)
