from flask import Flask

app = Flask(__name__)


# Task 1
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# Task 2
# @app.route('/')
# def hello_world():
#     return '<h1>Hello World :) <h1>'

# Task 3
# @app.route('/greet')
# def greet():
#     return "Hello"


# Task 4
@app.route('/greet/<name>')
def greet(name="Lukas"):
    return "Hello {}".format(name)


if __name__ == '__main__':
    app.run()
