import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	output = "Hello World"
	return output

if __name__ == "__main__":
	app.run()