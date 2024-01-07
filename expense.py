from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb
import re
import hashlib

global currency 
currency = "USD"

app = Flask(__name__)
app.secret_key = 'ebx71384hjkdfewk'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Moraxwashere7@'
app.config['MYSQL_DB'] = 'expdb'

mysql = MySQL(app)


@app.route("/budgetmate/login", methods=['GET','POST'])
def login():
    if request.method == "POST" and request.form["email"] != None and request.form["password"] != None:
        
        emailAddress = request.form["email"]
        password = request.form["password"]

        hash = password + app.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("Select * from user where email = %s and password = %s", (emailAddress,password,))
        account = cursor.fetchone()
        if account == None: 
            return render_template("loginpage.html", msg="Incorrect email or password!") 
        return render_template("home.html")
    return render_template("loginpage.html",msg="")


@app.route("/budgetmate/register", methods=['GET','POST'])
def register():
    if request.method == "POST" and request.form["email"] != None and request.form["password"] != None:
        
        firstName = request.form["firstname"]
        lastName = request.form["lastname"]
        emailAddress = request.form["email"]
        password = request.form["password"]
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("Select firstname from user where email = %s", (emailAddress,))
        account = cursor.fetchone()
        if account != None:
            return render_template("register.html", msg="User already exist") 

        hash = password + app.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        print(password)
        cursor.execute("Insert into user values(NULL,%s,%s,%s,%s,%s)",(password,emailAddress,firstName,lastName,currency,))
        mysql.connection.commit()
        cursor.close()    
        return render_template("register.html",msg="Registered successfully! Please login")
    
    
    return render_template("register.html",msg="")

#change the minimum amount of characters in password
# Forget password