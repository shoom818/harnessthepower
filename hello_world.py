
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
    multi_line_string = f"""Hello World.<br>
    This is a templatized pipeline. Hi Ulan<br>
    {multiply(5, 4)} <br>
    {os.environ.get("VERSION")}"""

    return multi_line_string 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
