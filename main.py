from flask import Flask, render_template, Response, request
import json
from io import BytesIO


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = read_json()
    return render_template(
        "generic.html",
        speaker=data["speaker"],
        speaker_designation=data["speaker_designation"],
        title=data["title"],
        date=data["date"],
        time=data["time"],
        venue=data["venue"],
        abstract=data["abstract"],
    )


@app.route("/process_form", methods=["POST"])
def process_form():
    # Retrieve the selected option value from the form submission
    selected_option = request.form["view"]
    data = read_json()
    # Render the corresponding HTML template based on the selected option
    return render_template(
        selected_option,
        speaker=data["speaker"],
        speaker_designation=data["speaker_designation"],
        title=data["title"],
        date=data["date"],
        time=data["time"],
        venue=data["venue"],
        abstract=data["abstract"],
    )


def read_json(json_file="data.json"):
    file = open(json_file)  # Opening JSON file
    data = json.load(file)  # returns JSON object as a dictionary
    file.close()  # Closing file
    return data


if __name__ == "__main__":
    app.run(debug=True)
