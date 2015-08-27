from flask import Flask, jsonify, render_template, request
import cPickle
import json
import random
app = Flask(__name__)

@app.route('/')
def index(methods=None):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

