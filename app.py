from flask import Flask

app = Flask(__name__)


# Task 1
@app.route('/')
def hello_world():
    return 'Hello World!'


# Task 2
# @app.route('/')
# def hello_world():
#     return '<h1>Hello World :) <h1>'

# Task 3
@app.route('/greet')
def greet():
    return "Hello"


# Task 4
@app.route('/greeting/<name>')
def greeting(name=""):
    return "Hello {}".format(name)


# Task 5
@app.route('/f/<celsius>')
def f(celsius=""):
    return "{}".format(int(celsius) * 9 / 5 + 32)


if __name__ == '__main__':
    app.run()
