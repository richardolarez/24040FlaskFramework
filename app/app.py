# app.py
from flask import Flask, render_template, request, redirect, url_for 
from models import db
import psycopg2

####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost/24040_db'
db = SQLAlchemy(app)
#######################################################################


@app.route('/')
def index():
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM books;')
    # books = cur.fetcose()
    # return render_hall()
    # cur.close()
    return render_template('index.html')

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
    app.jinja_env.cache = {}
    db.create_all()
    app.run()