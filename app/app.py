# app.py
from flask import Flask, render_template, request, redirect, url_for 
import psycopg2

####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='myuser',
                            password='mypassword')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html')

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()