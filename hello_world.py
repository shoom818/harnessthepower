
import os
from flask import Flask

print("Hello, World!")

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World this is a demo {multiply(5, 4)} {os.environ.get("VERSION")}' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
