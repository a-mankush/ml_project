import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")

    data = CustomData(
        gender=request.form.get("gender"),
        race_ethnicity=request.form.get("ethnicity"),
        parental_level_of_education=request.form.get("parental_level_of_education"),
        lunch=request.form.get("lunch"),
        test_preparation_course=request.form.get("test_preparation_course"),
        reading_score=request.form.get("reading_score"),
        writing_score=request.form.get("writing_score"),
    ).get_data_as_frame()

    prediction = round(PredictPipeline().predict(data)[0], 2)

    return render_template("home.html", results=prediction)


if __name__ == "__main__":
    app.run(debug=True)
