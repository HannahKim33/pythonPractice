from flask import Flask
from flask import render_template
from flask import request, redirect
import pymongo
from myutil.dao.memberDao import insertMember, listMember

app = Flask(__name__)

@app.route("/insertCust", methods=['GET'])
def insertCustForm():
    return render_template("insertCustForm.html")

@app.route("/insertCust", methods=['POST'])
def insertCustSubmit():
    name=request.form['name']
    ph=request.form['ph']
    age=request.form['age']
    doc={"name":name,"ph":ph,"age":age}
    insertMember(doc)
    return redirect("/listCust")

@app.route("/listCust")
def listCust():
    mdata=listMember()
    list=[]
    for row in mdata:
        list.append(row)
    return render_template("listCust.html", list=list)

if __name__ == '__main__':
    app.run()