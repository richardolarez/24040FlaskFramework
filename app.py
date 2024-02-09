# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/edv')
def about():
    return render_template('EDV.html')

@app.route('/menu')
def contact():
    return render_template('menu.html')

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()