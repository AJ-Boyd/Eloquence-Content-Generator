"""
auth: AJ Boyd
date: 6/29/2024
file: routes.py
desc: handles the form requests for the generator
"""

from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, session
from .generate_content import *

routes = Blueprint("routes", __name__)
llm = config_LLM()

@routes.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@routes.route('/generate', methods=["POST"])
def submit():
    attributes = []
    print(request.files)
    for d in request.form:
        x = request.form[d]
        if request.form[d] == "--":
            x = None
        attributes.append(x)
    
    # file = request.form['example'] if 'example' in request.form else None
    # print(file)
    file = request.form['example']

    print(attributes)
    content = gen_content(llm, attributes)
    return redirect(url_for('routes.home'))