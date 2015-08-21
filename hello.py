from flask import Flask, jsonify, render_template, request
import cPickle
import json
import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
app = Flask(__name__)

@app.route('/')
def index(methods=None):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

