from flask import *
from database import CR,DB

public=Blueprint("public",__name__)

@public.route("/",methods=["post","get"])
def Index():
    return render_template("index.html")

@public.route("/login",methods=["post","get"])
def Signin():
    if 'submit' in request.form:
        username=request.form["username"]
        password=request.form["password"]
       
        sql="SELECT * FROM user WHERE username=%s AND password =%s"
        val=(username,password)
        CR.execute(sql,val)
        result =CR.fetchall()
        if result:
            if result[0]['usertype'] =='user':
                return redirect(url_for("use.user"))
            if result[0]['usertype'] =='admin':
                return redirect(url_for("admin.Admin"))

            return render_template('index.html')
        else:
            flash("Username or Password invalid")
            
    return render_template('login.html')

@public.route("/reg",methods=["post","get"])
def Signup():
    if 'submit' in request.form:
        name=request.form["name"]
        email=request.form["email"]
        username=request.form["username"]
        usertype =request.form["utype"]
        password=request.form["password"]

        sq="SELECT * FROM user WHERE username=%s OR email=%s"
        va=(username,email)
        CR.execute(sq,va)

        result=CR.fetchall()
        if result:
            flash("Username or Email already exists")
        else:
            sql='INSERT INTO user (name,email,username,password,usertype) VALUES (%s,%s,%s,%s,%s)'
            val=(name,email,username,password,usertype)
            CR.execute(sql,val)
            DB.commit()
            return render_template('login.html')

    return render_template('register.html')