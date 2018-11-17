from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/aboutme', methods=['GET'])
def aboutme():
    return render_template('aboutme.html')


@app.route('/dna', methods=['GET', 'POST'])
def dna():
    return render_template('dna.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/github', methods=['GET'])
def github():
    return render_template('github.html')


@app.route('/js_timer', methods=['GET'])
def js_timer():
    return render_template('js_timer.html')

@app.route('/game', methods=['GET'])
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
