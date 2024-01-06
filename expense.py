from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb
import re


app = Flask(__name__)
app.secret_key = 'ebx71384hjkdfewk'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Moraxwashere7@'
app.config['MYSQL_DB'] = 'expdb'

mysql = MySQL(app)


@app.route("/budgetmate/login", methods=['GET','POST'])
def login():
    msg = ''
    return render_template("loginpage.html")

@app.route("/budgetmate/register", methods=['GET','POST'])
def register():
    msg = ''
    return render_template("register.html")




