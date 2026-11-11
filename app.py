from flask import Flask, request
import subprocess, hashlib
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
DB_PASSWORD = config.DB_PASSWORD

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output("ping -c 1 " + host, shell=True)

@app.route("/hash")
def h():
    return hashlib.md5(request.args.get("p", "").encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)