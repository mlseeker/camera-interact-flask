# -*- coding: utf-8 -*-

from flask import request
from flask import Flask
from flask import render_template

from PIL import Image
from PIL import ImageFilter
import base64
import json

app = Flask(__name__)


@app.route("/index", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST', 'GET'])
def acceptImage():
    image = request.form.get('image')
    fh = open("upload.jpg", "wb")
    fh.write(base64.b64decode(image))
    fh.close()
    return process_img()


def process_img():
    img = Image.open("upload.jpg")
    img = img.filter(ImageFilter.FIND_EDGES)
    img.save("after.jpg")
    f = open("after.jpg", "rb")
    bs64 = base64.b64encode(f.read())
    f.close()
    # rs_baes = [1, 2, 3]
    # rs_dict = {}
    # rs_dict['img'] = 1
    # rs_dict['1'] = 2
    # rs = json.dumps(dict(zip(range(len(rs_baes)), rs_baes)), ensure_ascii=False)

    return bs64


if __name__ == "__main__":
    app.run()
