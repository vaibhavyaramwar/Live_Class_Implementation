from DB import SqlDb
from flask import Flask, request, jsonify,json

app = Flask(__name__)


@app.route("/getStudentDetails", methods=["GET"])
def getStudentDetails():
    studentlist = SqlDb.get_StudentData()
    #dict(studentlist)
    return jsonify({"result":studentlist})


if __name__ == '__main__':
    app.run()
