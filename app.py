from flask import Flask, jsonify, request
# from models.user import User

app = Flask(__name__)


# Sample route to check if the app is working
@app.route('/')
def home():
    return jsonify({
            "Name": "Sundhar",
            "Age": 23,
            "Gender": "male"
        })


if __name__ == "__main__":
    app.run(debug=True)
