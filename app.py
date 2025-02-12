from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UNB Games</title>
    <style>
        body {
            background-color: black;
            color: red;
            font-size: 40px;
            text-align: center;
            margin-top: 20%;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    Damir is sigma
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
