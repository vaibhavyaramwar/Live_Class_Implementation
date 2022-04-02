from DB import SqlDb
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/getStudentDetails", methods=["GET"])
def getStudentDetails():
    studentlist = SqlDb.get_StudentData()
    return jsonify(str(studentlist))


if __name__ == '__main__':
    app.run()
