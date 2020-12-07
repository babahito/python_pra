import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html=res.read().decode("utf-8")

    soup=BeautifulSoup(html,"html.parser")

    titles=soup.select("item")
    shuffle(titles)
    title=titles[0]
    print(title)
    return json.dumps({
        "content":title.find("title").string,
        "link":title.get('ref:about')
    })

@app.route("/api/xxxx")
def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
