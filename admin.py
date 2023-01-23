from flask import *
from database import DB, CR
admin=Blueprint("admin",__name__)

@admin.route("/")
def Admin():
    
    return render_template('admin.html')

@admin.route("/ans",methods=["post","get"])
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
        return redirect(url_for("admin.Ans"))
    return render_template('ans.html',qanda=qanda)

@admin.route("/delete",methods=["post","get"])
def deleteqanda():
    CR.execute("SELECT * FROM qanda")
    res =CR.fetchall()
    if "submit" in request.form:
        id=request.form['submit']
        CR.execute("DELETE  FROM qanda WHERE id=%s",(id,))
        DB.commit()
        flash("item deleted")
        return redirect(url_for("admin.deleteqanda"))
    return render_template("deleteqanda.html",res=res)

@admin.route("/duser",methods=["post","get"])
def deleteuser():
    CR.execute("SELECT * FROM user")
    res =CR.fetchall()
    if "submit" in request.form:
        id=request.form['submit']
        CR.execute("DELETE  FROM user WHERE id=%s",(id,))
        DB.commit()
        flash("item deleted")
        return redirect(url_for("admin.deleteuser"))
    return render_template("deleteuser.html",res=res)

@admin.route("/logout")
def logout():
    return render_template("index.html")