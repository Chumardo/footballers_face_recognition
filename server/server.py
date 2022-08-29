from flask import Flask, render_template, url_for, request, redirect, jsonify
from werkzeug.utils import secure_filename
import os
import util

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "server/static/images"


@app.route('/', )
def home():
    return render_template("app.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'picture.png'))
    full_image_path = "server/static/images/picture.png"
    prediction_dict = util.classify_image(None, full_image_path)
    if len(prediction_dict) == 0:
        prediction_dict.append({"class": "Can't classify image. Classifier was not able to detect face and two eyes properly",
                                'class_probability': [0, 0, 0, 0, 0]})
    else:
        prediction_dict[0]['class'] = prediction_dict[0]['class'].title()
    return render_template("result.html", prediction_dict=prediction_dict)


if __name__ == '__main__':
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True)