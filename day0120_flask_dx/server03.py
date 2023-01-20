from flask import Flask
from flask import render_template
from flask import request
from myutil.dao.memberDao import listMember,insertMember
from myutil.dao.memberDao import listMember

app = Flask(__name__)

@app.route("/listMember")
def lm():
    memberList  = list(listMember())
    for row in memberList:
        del(row["_id"])
        print(row)

    return "pro("+str(memberList)+")"


@app.route("/hello")
def hello():
    data = {"name":"홍길동","age":20}
    return "pro("+str(data)+")"

if __name__ == '__main__':
    app.run()
    # app.run(host="211.238.142.155", debug=True)










