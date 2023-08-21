from flask import Flask, render_template
from shared.shared_utils import hello

app = Flask(__name__)

@app.route('/')
def home():
    message = hello()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
