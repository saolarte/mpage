import logging
from multiprocessing import Process

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import loads, dumps

from bg_task import read_tasks

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://mongo/assessment"
mongo = PyMongo(app)

#Start background process
bg_process = Process(target=read_tasks, args=(mongo,) )
bg_process.start()


@app.route('/new_task', methods=['POST'])
def new_task():
    """
    Read request json and insert new document to database
    """
    req = request.json
    if 'cmd' in req:
        id = mongo.db.tasks.insert({
            'cmd' : req['cmd'],
            'status' : 'Not started'
        })

    response = {'id' : str(id)}
    return response


@app.route('/get_output/<id>', methods=['GET'])
def get_output(id):
    tasks = []
    query = mongo.db.tasks.find({'_id':ObjectId(oid=str(id))})
    for e in query:
        try: 
            output = e['output']
        except:
            output = "Task has not been ran yet"
        tasks.append(output)
    
    return jsonify(status = e['status'], output =  output)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)