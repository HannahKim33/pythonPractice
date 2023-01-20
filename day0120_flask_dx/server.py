from flask import Flask
from flask import render_template
from flask import request
from myutil.sist import makeWordCloud

app = Flask(__name__)
list = ["사과", "포도", "수박", "딸기"]

@app.route("/wc", methods=["GET"])
def wcForm():
    return render_template("wc.html")


# def makeWordCloud(textFile, imgFile, stopWord, font, mask=None):
@app.route("/wc", methods=["POST"])
def wcSubmit():
    textFile = request.form["textFile"]
    imgFile = request.form["imgFile"]
    stopWord = request.form["stopWord"]
    font = request.form["font"]
    mask = request.form["mask"]

    # print("textFile:",textFile)
    # print("imgFile:",imgFile)
    # print("stopWord:",stopWord)
    # print("font:",font)
    # print("mask:",mask)
    stopWord = stopWord.split(",")
    # print(stopWord)

    makeWordCloud(textFile,imgFile,stopWord,font,mask)
    return render_template("wc_ok.html", imgFile=imgFile)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/hello")
def hello():
    list.append("수박")
    return render_template("hello.html", name="홍길동", age=20, list=list)

@app.route('/make_wc')
def make_wc():
    return 'makeColude'

@app.route("/listMember")
def listMember():
    member_list = [
        {"name":"홍길동", "addr":"서울","age":20},
        {"name":"이순신", "addr":"부산","age":40},
        {"name":"유관순", "addr":"광주","age":24},
    ]
    return render_template("listMember.html",list=member_list)


@app.route("/insert", methods=["GET"])
def insertForm():
    return render_template("insert.html")

@app.route("/insert", methods=["POST"])
def insertSumbit():
    title = request.form['title']
    print('전달된 데이터:'+title)
    return render_template("insert.html")



if __name__ == '__main__':
    app.run()










