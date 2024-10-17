---

## Flask Application Design

### HTML Files

#### `index.html`

- Purpose: The main page of the application, where users can upload text files.
- Content:
```HTML
<!DOCTYPE html>
<html>
<head>
  <title>Text Word Counter</title>
</head>
<body>
  <h1>Upload a Text File</h1>
  <form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="text_file">
    <input type="submit" value="Upload">
  </form>
</body>
</html>
```

### Routes

#### `/upload`

- Purpose: Handles the file upload and processes the text to count the words.
- Function:
```Python
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
```