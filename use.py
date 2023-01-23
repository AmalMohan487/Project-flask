from flask import *
from database import DB, CR
from datetime import datetime

use=Blueprint("use",__name__)

@use.route("/")
def user():
    
    return render_template('user.html')

@use.route("/ask",methods=["post","get"])
def Ask():
    if "submit" in request.form:
        question = request.form['question']
        date=datetime.now()
        sql ='INSERT INTO qanda (question,date) VALUES (%s,%s)'
        val=(question,date)
        CR.execute(sql,val)
        DB.commit()
        flash("Question Submited")
        return render_template('user.html')

    return render_template('ask.html')

@use.route("/ans",methods=["post","get"])
def Ans():
    CR.execute("SELECT * FROM  qanda")
    qanda=CR.fetchall()
    if 'submit' in request.form:
        answer=request.form['ans']
        id=request.form['submit']
        sql="UPDATE qanda set answer=%s WHERE id=%s"
        val=(answer,id)
        CR.execute(sql,val)
        DB.commit()
        flash("submitted")
        return redirect(url_for("use.Ans"))
    return render_template('answer.html',qanda=qanda)

@use.route("/view")
def View():
    CR.execute("SELECT * FROM qanda ")
    res=CR.fetchall()
    return render_template('viewans.html',res=res)

@use.route("/logout")
def logout():
    return render_template("index.html")