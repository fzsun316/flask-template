from myapp import app
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
from flask_socketio import send, emit
from myapp import socketio
import time
import datetime
import json
import requests
import pytz

@app.route('/')
@app.route('/index')
def index():
	return render_template("home.html")
