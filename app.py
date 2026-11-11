from flask import Flask, request
import subprocess, hashlib

app = Flask(__name__)
app.secret_key = "super-secret-123"
DB_PASSWORD = "admin12345"

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output("ping -c 1 " + host, shell=True)

@app.route("/hash")
def h():
    return hashlib.md5(request.args.get("p", "").encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)