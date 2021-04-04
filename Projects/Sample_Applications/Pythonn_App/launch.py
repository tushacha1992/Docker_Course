from flask import Flask
WelcomePython = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Welcome to Python Application V1\"}"
if __name__ == "__main__":
    WelcomePython.run(host="0.0.0.0", port=int("5000"), debug=True)
