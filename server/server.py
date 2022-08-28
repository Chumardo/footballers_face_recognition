from crypt import methods
from re import A
from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def classify_image():
    return render_template('app.html')


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
