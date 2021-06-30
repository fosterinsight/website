from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/subscribed', methods=['GET', 'POST'])
def subscribed():
    return render_template('subscribed.html', scroll='subscribed')


if __name__ == '__main__':
    app.run(debug=False)
