from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
port = 5000

table = pd.read_csv("data_small/stations.txt", skiprows=17)
table = table[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=table.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # data_small / TG_STAID000001.txt
    print(f"data_small/TG_STAID000{station.zfill(3)}.txt")
    df = pd.read_csv(f"data_small//TG_STAID000{station.zfill(3)}.txt",
                     skiprows=20,
                     parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"date": f"{date}", "station": station, "temperature": temperature}



if __name__ == "__main__":
    app.run(debug=True, port=port)

