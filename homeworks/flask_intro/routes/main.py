from flask import Flask
from app import app


@app.route('/')
def home():
    return '''FOR EXAMPLE:
                /add/2/2 - will return 4
                /add/4/1 - will return 5
                /add/5/3 - will return 8'''

@app.route('/add/<num1>/<num2>')
def add_operation(num1, num2):
    res = int(num1) + int(num2)
    return str(res)
