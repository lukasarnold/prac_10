from flask import Flask

app = Flask(__name__)


@app.route('/f/<celsius>')
def f(celsius=""):
    return int(celsius) * 9 / 5 + 32


if __name__ == '__main__':
    app.run()
