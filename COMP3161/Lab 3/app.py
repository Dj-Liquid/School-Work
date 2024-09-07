from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)






@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "hello world"






@app.route('/get_students', methods=['GET'])
def get_students():
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                host='127.0.0.1',
                                database='uwi')
        cursor = cnx.cursor()
        cursor.execute('SELECT * from students')
        student_list = []
        for student_id, last_name, first_name, address, city in cursor:
            student = {}
            student['id'] = student_id
            student['last_name'] = last_name
            student['first_name'] = first_name
            student['address'] = address
            student['city'] = city
            student_list.append(student)
        cursor.close()
        cnx.close()
        return make_response(student_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/get_student/<student_id>', methods=['GET'])
def get_sudent(student_id):
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                host='127.0.0.1',
                                database='uwi')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * from students WHERE StudentID={student_id}")
        row = cursor.fetchone()
        student = {}
        if row is not None:
            student_id, last_name, first_name, address, city = row
            student = {}
            student['id'] = student_id
            student['last_name'] = last_name
            student['first_name'] = first_name
            student['address'] = address
            student['city'] = city
            cursor.close()
            cnx.close()
            return make_response(student, 200)
        else:
            return make_response({'error': 'Student not found'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                    host='127.0.0.1',
                                    database='uwi')
        cursor = cnx.cursor()
        content = request.json
        id = content['id']
        last_name = content['last_name']
        first_name = content['first_name']
        address = content['address']
        city = content['city']
        cursor.execute(f"INSERT INTO Students VALUES('{id}','{last_name}','{first_name}','{address}','{city}')")
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success" : "Student added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/update_address/<student_id>', methods=['PUT'])
def update_address(student_id):
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                        host='127.0.0.1',
                                        database='uwi')
        cursor = cnx.cursor()
        content = request.json
        address = content['address']
        cursor.execute(f"UPDATE Students SET address='{address}' WHERE StudentID={student_id}")
        cnx.commit()
        cursor.close()
        return make_response({"success" : "Student updated"}, 202)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/delete_student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                            host='127.0.0.1',
                                            database='uwi')
        cursor = cnx.cursor()
        cursor.execute(f"DELETE FROM Students WHERE StudentID={student_id}")
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success" : "Student deleted"}, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/address_report', methods=['GET'])
def get_addresses():
    try:
        cnx = mysql.connector.connect(user='uwi_user', password='uwi876',
                                            host='127.0.0.1',
                                            database='uwi')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM ALL_ADRESSESS")
        address_lst = []
        for add in cursor:
            address = {}
            address['Address'] = add[0]
            address_lst.append(address)
        return make_response(address_lst, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
if __name__ == '__main__':
    app.run(port=6000)