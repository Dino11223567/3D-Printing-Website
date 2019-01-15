from flask import Flask, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename
import os
from O365 import *
from datetime import datetime
# Create empty variables to hold email account credentials
O365_username = ""
O365_password = ""
# Load credentials from textfile
O365_file = open('O365_auth.txt')
lines = O365_file.readlines()
O365_username = lines[0]
O365_username = O365_username[0:len(O365_username) - 1]
O365_password = lines[1]
O365_creds = (O365_username, O365_password)


# Initialize flask app
app = Flask(__name__)
folder = os.getcwd() + "\\prints\\"
port = 4000
Bootstrap(app)
app.secret_key = "?k3x,_rBva9gZ>8?r,bZ5]4?_}>ASQWcy.L}m17>{NGJ0nUz!B;x]L9-*;t$"

# Handle home route
@app.route("/", methods=['GET'])
def index():
    return render_template('3DView.html')

# 404 handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle Order request 
@app.route("/placeOrder", methods=['POST', 'GET'])
def placeOrder():
    if request.method == 'POST':
        # Save file in folder on server
        file = request.files["file"]
        file.save(folder + secure_filename(file.filename))
        # Get order info from request
        color = request.form["color"]
        length = request.form["length"]
        width = request.form["width"]
        height = request.form["height"]

        # Create new email with credentials
        m = Message(auth=O365_creds)
        # Add recipient
        m.setRecipients("Enter Recipient Here")
        # Add email subject
        m.setSubject("3D Printer Order")
        # Add order info to email-body
        m.setBody("Color: " + color + "\nLength: " + length + "\nWidth: " + width + "\nHeight: " + height)
        # Add file attachment
        att = Attachment(path=(folder + file.filename))
        m.attachments.append(att)
        # Send email
        m.sendMessage()

    return ('', 204)

# Run app
app.run(port=port)
