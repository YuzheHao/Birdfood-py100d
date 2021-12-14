from flask import Flask
from flask import render_template
from flask import request
from flask import Response
from school.playground import *
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def build():
    return render_template('frontpage.html')

@app.route('/item/<id>/')
def item(id):
    return "heloo world %s" % id

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
