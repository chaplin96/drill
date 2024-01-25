import re
import os
from flask import Flask, render_template, send_file
from datetime import datetime, timedelta, timezone
import random
import json

app = Flask(__name__)

with open("data/oogiri_20240121.json", "r", encoding="utf-8") as f:
    tmp_oogiri_list = json.load(f)

@app.route("/")
def oogiri_drill():    
    tmp_oogiri = random.choice(tmp_oogiri_list)
    oogiri = {"question":tmp_oogiri["question"]}
    best_answers = tmp_oogiri["answer_samples"]["3"]
    if len(best_answers) > 3:
        # 3点の回答が3つ以上ある場合は、3点の回答を表示する
        oogiri["answer_samples"] = random.sample(tmp_oogiri["answer_samples"]["3"], 3)
    else:
        # 3点の回答が2つ以下の場合は、3点の回答と2点の回答を表示する
        oogiri["answer_samples"] = best_answers + random.sample(tmp_oogiri["answer_samples"]["2"], 3-len(best_answers))

    return render_template("drill.html", oogiri=oogiri)

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True, host="0.0.0.0", port=5000)
    # sudo /home/g3ma510_96ki/.pyenv/versions/3.10.0/bin/python3.10 app.py
    
"""
■起動
python app.py
or
gunicorn app:app

■デーモンで起動
nohup gunicorn app:app &

■停止
ps aux | grep gunicorn | awk '{ print "kill -9", $2 }' | sh

"""