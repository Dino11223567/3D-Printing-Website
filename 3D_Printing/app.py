from flask import Flask, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename
import os
from O365 import *
from datetime import datetime

O365_username = ""
O365_password = ""

O365_file = open('O365_auth.txt')
lines = O365_file.readlines()
O365_username = lines[0]
O365_username = O365_username[0:len(O365_username) - 1]
O365_password = lines[1]
O365_creds = (O365_username, O365_password)



app = Flask(__name__)
folder = os.getcwd() + "\\prints\\"
port = 4000
Bootstrap(app)
app.secret_key = "?k3x,_rBva9gZ>8?r,bZ5]4?_}>ASQWcy.L}m17>{NGJ0nUz!B;x]L9-*;t$"


@app.route("/", methods=['GET'])
def index():
    return render_template('3DView.html')

@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404

@app.route("/placeOrder", methods=['POST', 'GET'])
def placeOrder():
    if request.method == 'POST':
        file = request.files["file"]
        #file.save(filename=savefilename, ignore_discard=False, ignore_expires=False)
        file.save(folder + secure_filename(file.filename))
        color = request.form["color"]
        length = request.form["length"]
        width = request.form["width"]
        height = request.form["height"]

        m = Message(auth=O365_creds)
        m.setRecipients("david.niederweis@gmail.com")
        m.setSubject("3D Printer Order")
        m.setBody("Color: " + color + "\nLength: " + length + "\nWidth: " + width + "\nHeight: " + height)
        att = Attachment(path=(folder + file.filename))
        m.attachments.append(att)
        m.sendMessage()

    return ('', 204)

# os.system('cls')
app.run(port=port)
