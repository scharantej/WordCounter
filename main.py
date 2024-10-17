
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
  # Get the uploaded file
  file = request.files['text_file']

  # Read the file contents
  text = file.read().decode("utf-8")

  # Count the words
  word_count = len(text.split())

  # Return the word count
  return jsonify({"word_count": word_count})

if __name__ == "__main__":
  app.run(debug=True)
