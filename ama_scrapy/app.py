from flask import Flask render_template,url_for,request,redirect
import os

application=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True) 