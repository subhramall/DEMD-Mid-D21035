from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Enter your name in URL with leading /"

@app.route("/<name>")
def print_name(name):
    return f"Welcome {name}" 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)