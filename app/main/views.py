from flask import render_template, request, redirect, url_for, current_app, send_from_directory, make_response
from . import main
from . import forms
import os


@main.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
