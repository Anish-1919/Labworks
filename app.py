from functools import wraps
from flask import Flask, redirect, render_template, session
import pymongo

app = Flask(__name__)
app.secret_key=b'\x95O\xa2\xca\x07)\x1a\x13HiEH\xff~\x9e\x1b'

#Database
# client = pymongo.MongoClient('localhost', 27017)
# db = client.mydb

client = pymongo.MongoClient("mongodb+srv://Anish:Anish123@cluster0.cew55.mongodb.net/mydb?retryWrites=true&w=majority")
db = client.mydb

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap
  
#Routes
from user import routes

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template('dashboard.html')

