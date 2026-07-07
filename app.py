from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_excel("movies.xlsx")

    search = request.args.get("search")

    if search:
        df = df[df["Title"].astype(str).str.contains(search, case=False, na=False)]

    movies = df.to_dict(orient="records")

    return render_template(
        "index.html",
        movies=movies,
        total_movies=len(df)
    )

if __name__ == "__main__":
    app.run(debug=True)