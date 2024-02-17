# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify 
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the SECRET_KEY configuration option

app.app_context()
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

###################### Import the TID Models ########################
from models.TIDTables import ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses
from models import User

####################### CREATE TABLES ########################
with app.app_context(): 
    db.create_all()

####################### APIs ########################
# Test Route
@app.route('/test', methods=['GET'])
def test():
    return {'message': 'Test route works!'}

# create a new user
@app.route('/user', methods=['POST', 'GET'])
def create_user():
    try:
        data = request.json
        new_user = User(username=data['username'], password=data['password'], email=data['email'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)
    

# login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return make_response(jsonify({'message': 'login successful'}), 200)
        else:
            return make_response(jsonify({'message': 'invalid credentials'}), 401)
    except Exception as e:
        return make_response(jsonify({'message': str(e)}), 500)
    

####################### VIEWS / PAGE ROUTES ########################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

class UserForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    email = StringField('Email')
    role = StringField('Role')
    submit = SubmitField('Sign Up')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data, email=form.email.data, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully!', 'success')  # Display success message
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)



if __name__ == '__main__':
    app.run()