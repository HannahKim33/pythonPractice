from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
list = ['사과', '포도', '수박', '딸기']

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello():
    list.append("수박")
    return render_template('hello.html', name='홍길동', age=20, list=list)

@app.route("/listMember")
def listMember():
    # d = [{'이름': ['홍길동', '이순신', '유관순'], '주소': ['서울', '부산', '광주'], '나이': [20, 40, 24]}]
    d=[
        {'name':'홍길동', 'addr':'서울', 'age':20},
        {'name':'이순신', 'addr':'부산', 'age':40},
        {'name':'유관순', 'addr':'광주', 'age':24}
    ]
    return render_template('listMember.html', d=d)

@app.route("/insert", methods=['GET'])
def insertForm():
    return render_template("insert.html")

@app.route("/insert", methods=['POST'])
def insertSubmit():
    title=request.form['title']
    print('전달된 데이터: '+title)
    return render_template("insert.html")

@app.route("/make_wc", methods=['GET'])
def make_wc_form():
    return render_template("wc.html")

@app.route("/make_wc", methods=['POST'])
def make_wc_submit():
    txt_name=request.form['txt_name']
    img_name=request.form['img_name']
    print(img_name)
    stopwords=request.form['stopwords']
    print(stopwords)
    stopwords=stopwords.split(',')
    print(stopwords)
    msk_name=request.form['msk_name']
    font='../Data/DoHyeon-Regular.ttf'
    from wc import makeWordCloud
    makeWordCloud(txt_name, img_name, stopwords, font, msk_name)
    return render_template("wc_result.html", img_name=img_name)

if __name__ == '__main__':
    app.run()