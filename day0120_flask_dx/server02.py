from flask import Flask
from flask import render_template
from flask import request
from myutil.dao.memberDao import listMember,insertMember

app = Flask(__name__)

@app.route("/insertMember", methods=["GET"])
def insertForm():
    return render_template("insertMember.html")



@app.route("/insertMember", methods=["POST"])
def insertSubmit():
    name = request.form["name"]
    addr = request.form["addr"]
    age = request.form["age"]
    doc = {"name":name, "addr":addr, "age":age}
    insertMember(doc)
    # list = listMember()
    # print(list)
    return render_template("listMember.html", list=listMember())


@app.route("/listMember")
def memberList():
    return render_template("listMember.html", list=listMember())

if __name__ == '__main__':
    app.run()










