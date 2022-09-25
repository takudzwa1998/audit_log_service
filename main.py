import flask
import sqlite3
from flask import request, Response,render_template
from flask_httpauth import HTTPTokenAuth
import json
import datetime

app = flask.Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

token_dict = open('tokens.json')

tokens = json.load(token_dict)

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

class Log_Database:
    def __init__(self):

        #create database
        self.conn = sqlite3.connect('logs.db', check_same_thread=False)
        sql = """ CREATE TABLE IF NOT EXISTS logs (DATA TEXT NOT NULL) """
        self.conn.execute(sql)
        self.conn.commit()

    def save_logs(self, log_dict):#done
        #save log as json string in logs database
        log_ = json.dumps(log_dict)
        try:
            sql = """ INSERT into logs (DATA) VALUES (?) """
            self.conn.execute(sql, (log_,))
            self.conn.commit()
            return True
        except Exception as e:
            saved_ = "Exception while inserting: " + e
            return saved_
    
    def get_logs(self, keywords):#done
        results = []
        try:
            for i in keywords:
                sql = """ SELECT * FROM logs WHERE (DATA like ?) """
                res = self.conn.execute(sql, ('%'+keywords[i]+'%',))
                result = res.fetchall()
                results.append(result)
            return results
        except Exception as e:
            print("Exception while searching log: ", e)
            return False

log_db = Log_Database()

@app.route('/')
@auth.login_required
def home():
    return "Welcome to the audit log service. Please enter your logs in a key-value JSON format."

@app.route('/save_log', methods=['POST'])
@auth.login_required
def save_logs():
    #this function consumes a log and saves it in a db
    global log_db
    logs_dict={}

    #get received logs and save to dict
    received_logs = request.form.to_dict(flat=False)
    print("CURL received logs: ", received_logs)

    for i in received_logs:
        print("curl logs: ", received_logs[i][0])
        logs_dict[i] = received_logs[i][0]

    saved_ = log_db.save_logs(logs_dict)

    #check if logs are saved and send
    if saved_ is True:
        saved_ = "Logs successfully saved to database!"
        return Response( saved_, status=200, mimetype='application/json')
    else:
        return Response( saved_, status=200, mimetype='application/json')

@app.route('/get_logs', methods=['GET'])
@auth.login_required
def get_logs():
    global log_db
    query_dict={}
    log_str =""
    query = request.form.to_dict(flat=False)
    for i in query:
        query_dict[i] = query[i][0]
        
    print("Get logs with query: ", query_dict)

    logs_ = log_db.get_logs(query_dict)

    #time complexity below is (n^^3)
    #The third loop is to make the return values more readable
    #therefore it can be removed to tradeoff better time complexity for readability

    if logs_ != False:
        for i in logs_: #loop 1
            for event in i: #loop 2
                json_logs = json.loads(event[0])
                for j in json_logs: #loop 3
                    log_str = log_str + j +":"+ json_logs[j] + ","

                log_str = log_str + '\n'
        print("curl returns: ", log_str)
        return Response( log_str, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
