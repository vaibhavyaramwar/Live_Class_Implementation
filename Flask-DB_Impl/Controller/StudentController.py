from DB import SqlDb
from DB import MongoDB
from flask import Flask, request, jsonify,json

app = Flask(__name__)


@app.route("/getStudentDetails", methods=["GET"])
def getStudentSQLDBDetails():
    studentlist = SqlDb.get_StudentData()
    return jsonify({"result":studentlist})

@app.route("/getStudentData",methods=["GET"])
def getStudentMongoDBDetails():
    studentdata = MongoDB.getStudentData()
    return jsonify({"result":str(studentdata)})

if __name__ == '__main__':
    app.run()

