from flask import Flask
from flask import *
from public import public
from use import use
from admin import admin

app=Flask(__name__)
app.secret_key="hello"

app.register_blueprint(public)
app.register_blueprint(use,url_prefix="/use")
app.register_blueprint(admin,url_prefix="/admin")





app.run(debug=True, port=5015)