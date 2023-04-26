from flask import Flask, render_template
import pandas

mean = Flask(__name__)


@mean.route("/")
def home():
    return render_template("side_project.html",
                           data=table.to_html())

@mean.route("/meaningapi/v1/<word>")
def meaning(word):
    filename = "dictionary.csv"
    df = pandas.read_csv(filename)

    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"definition": definition, "word": word}

if __name__ == "__main__":
    mean.run(debug=True)
