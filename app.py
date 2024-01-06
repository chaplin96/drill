import re
import os
from flask import Flask, render_template, send_file
from datetime import datetime, timedelta, timezone
import random
import json

app = Flask(__name__)

@app.route("/")
def oogiri_drill():
    # TODO 大喜利回答例、スコア高いのを表示した方が参考になるよな
    with open("data/oogiri.json", "r", encoding="utf-8") as f:
        tmp_oogiri_list = json.load(f)
    
    oogiri = random.choice(tmp_oogiri_list)
    oogiri["answer_samples"] = random.sample(oogiri["answer_samples"], 3)

    return render_template("drill.html", oogiri=oogiri)

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True, host="0.0.0.0", port=80)
    # sudo /home/g3ma510_96ki/.pyenv/versions/3.10.0/bin/python3.10 app.py
