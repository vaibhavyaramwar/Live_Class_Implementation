import mysql.connector as connection

def get_StudentData():
    try:

        studentList = list()
        myDb = connection.connect(host="localhost", port=5506, user="root", password="mysql", database="testDb",use_pure=True)
        cursor = myDb.cursor()
        cursor.execute("select * from ineuron")

        studentList = cursor.fetchall()
        #for result in cursor.fetchall():
         #   print(result)
        myDb.close()

        return studentList
    except Exception as e:
        myDb.close()
        print(e)