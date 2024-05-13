from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]

        if file.filename == "":
            return "No selected file"
       
        file.save(file.filename)
        return "File uploaded successfully"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    
