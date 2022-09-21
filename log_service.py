from urllib import response
import flask
import sqlite3
from flask import request, render_template

app = flask.Flask(__name__)


class Log_Database:
    def __init__(self):

        #create database
        self.conn = sqlite3.connect('logs.db')
        sql = """ CREATE TABLE IF NOT EXISTS logs(DATA TEXT NOT NULL) """
        self.conn.execute(sql)
        self.conn.commit()

    def add_log():
        ''' function to add logs from system'''


@app.route('/save_log', methods=['POST'])
def save_log():
    #this function consumes a log and saves it in a db
    for i in request.form:
        print(i)
        
    return response()
