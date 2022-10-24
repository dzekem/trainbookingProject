from flask import Flask

import app
from flask_login import LoginManager

login_manager = LoginManager()

@app.route('/login',methods=['GET','POST'])
def login():
