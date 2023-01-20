from flask import Flask
from myutil.dao.memberDao import listMember as list

app=Flask(__name__)

@app.route("/listMember")
def listMember():
    data=list()
    return "list("+str(data)+")"

@app.route("/hello")
def hello():
    data={"name":"홍길동","age":20}
    return "pro("+data+")"

if __name__=='__main__':
    # app.run(host='192.168.0.104', debug=True)
    app.run()