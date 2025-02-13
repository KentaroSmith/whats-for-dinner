"""
Planning out my pseudo code:

functions to generate lists will all reside in app.py
templates for the CSV files will live in the csv_templates folder


"""

from os import environ
from os.path import basename
from flask import Flask, render_template, request, send_file, after_this_request
import logging.handlers 
from logging.handlers import SMTPHandler
import logging, smtplib, os, time, json
from dotenv import load_dotenv
from waitress import serve
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#actual app 
app = Flask(__name__)
app.debug = True
#https://stackoverflow.com/questions/36937461/how-can-i-send-an-email-using-python-loggings-smtphandler-and-ssl


# Apply format to the log messages
formatter = '[{asctime}] [{name}] [{levelname}] - {message}' 
logging.basicConfig(filename="webapp.log", format=formatter, style="{")
logger = logging.getLogger()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/refresh_list', methods = ['GET', 'POST'])
def update_cards():
    if request.method == 'POST':
        form_data = request.form
        return render_template("confirmed.html")
    elif request.method == 'GET':
        return render_template('update_cardholders.html')

app.secret_key = environ.get("SECRET_KEY")
app.debug = True
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000, threads=1) #WAITRESS!