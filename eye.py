#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:39:42 2018

@author: ganeson
"""

import flask
import sqlite3
from flask import Flask , jsonify , request

app = Flask(__name__) 

connection = sqlite3.connect('eyeproject.db') 

def InitDB():
    connection.execute('Create table Frame (ID Number , Brand String ,Model String)');
    
InitDB()


@app.route('/'):
    def works():
        return "It works"
        

@app.route('/Add/Frame'):
    def AddF():
        data = request.parse_json()
        
        