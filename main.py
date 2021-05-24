import config

from posix import environ

from flask.helpers import url_for
from werkzeug.datastructures import FileStorage
from werkzeug.utils import redirect
import os
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import shutil

app = Flask(__name__, static_folder="static")
app.secret_key = os.environ.get('APP_SECRET')

@app.route('/')
def index():
  return "py-chatbot version 1.0"

@app.route('/<name>', methods=['POST'])
def hello(name):
  return f"hello {name}"

@app.route('/watching/')
@app.route('/watching/<type>')
def renderHtml(type):
  return render_template(f"{type}.html", name=f"{type}")

@app.route('/wrongLogin')
def wrongLogin():
  return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login():
  print(request.cookies)
  print(request.json)

  rsp = make_response()
  rsp.set_cookie('username', 'brookie')
  return rsp

@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
  t = request.files.getlist('file')

  print(isinstance(t, list))

  for i in range(len(t)):
    print(t[i].mimetype)
    with open(f'static/upload/{t[i].filename}', 'wb') as out_file:
      shutil.copyfileobj(t[i].stream, out_file)
  
  #for (i in range())
  return 'hello there'
  
if os.environ.get('FLASK_ENV') != 'production':
  app.run(debug=True)
elif  os.environ.get('FLASK_ENV') == 'production':
  app.run(debug=False)


# dynamic url setup
url_for('cdn')