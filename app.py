from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload():

    photo = request.files["photo"]
    name = request.form["name"]
    email = request.form["email"]

    filename = "face.jpg"
    photo.save(os.path.join(UPLOAD_FOLDER, filename))

    print("Received:", name, email)

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)