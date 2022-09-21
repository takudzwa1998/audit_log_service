from urllib import response
import flask
import sqlite3
from flask import request, render_template
from flask_httpauth import HTTPBasicAuth
import json


app = flask.Flask(__name__)

class Log_Database:
    def __init__(self):

        #create database
        self.conn = sqlite3.connect('logs.db', check_same_thread=False)
        sql = """ CREATE TABLE IF NOT EXISTS logs (DATA TEXT NOT NULL) """
        self.conn.execute(sql)
        self.conn.commit()

    def save_logs(self, log_dict):
        log_string = json.dumps(log_dict)
        try:
            sql = """ INSERT into logs (DATA) VALUES (?) """
            self.conn.execute(sql, (log_string,))
            self.conn.commit()
            return "great, added!"
        except Exception as e:
            print("Exception while inserting: ", e)
            return "not so great, not added"
    
    def get_logs(self, keywords):
        try:
            for i in keywords:
                print("Keyword: ", keywords[i])
                sql = """ SELECT * FROM logs WHERE (DATA like ?) """
                res = self.conn.execute(sql, ('%'+keywords[i]+'%',))
                result = res.fetchall()
                print(result)
            return "Retrieved something, Yay!!"
        except Exception as e:
            print("Exception while searching: ", e)
            return "Nothing retrieved!! Epic Fail"

log_db = Log_Database()

@app.route('/')
def home():
    return "works"

@app.route('/save_log', methods=['POST', 'GET'])
def save_log():
    global log_db
    logs_dict={}
    #this function consumes a log and saves it in a db
    #print("req form: ", request.form.to_dict(flat=False))
    received_logs = request.form.to_dict(flat=False)
    for i in received_logs:
        logs_dict[i] = received_logs[i][0]
        
    print("saved logs: ", logs_dict)

    did_it_work = log_db.save_logs(logs_dict)

    return str(did_it_work)

@app.route('/get_logs', methods=['POST', 'GET'])
def get_logs():
    global log_db
    query_dict={}
    #this function consumes a log and saves it in a db
    #print("req form: ", request.form.to_dict(flat=False))
    query = request.form.to_dict(flat=False)
    for i in query:
        query_dict[i] = query[i][0]
        
    print("saved logs: ", query_dict)

    did_it_work = log_db.get_logs(query_dict)

    return str(did_it_work)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
