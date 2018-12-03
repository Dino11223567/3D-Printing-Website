from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
port = 4000
Bootstrap(app)
app.secret_key = "?k3x,_rBva9gZ>8?r,bZ5]4?_}>ASQWcy.L}m17>{NGJ0nUz!B;x]L9-*;t$"


@app.route("/", methods=['GET'])
def index():
    return render_template('3DView.html')

@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404




# os.system('cls')
app.run(port=port)
