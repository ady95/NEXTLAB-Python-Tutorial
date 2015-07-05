import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    output = time.strftime("%Y-%m-%d %I:%M:%S", time.localtime())
    return output

if __name__ == "__main__":
	app.run()