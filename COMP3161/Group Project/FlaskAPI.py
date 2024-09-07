from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)

# Helper function to get database connection
def get_db():
    conn = mysql.connector.connect(user='root', password='jimjones2266',
                                host='127.0.0.1',
                                database='course_management')
    return conn





#GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS
@app.route('/register', methods=['POST'])	
def register_user():
    try:
        conn = get_db()
        cursor = conn.cursor()

        data = request.get_json()
        user_id = 0
        username = data.get('username')
        user_password = data.get('user_password')
        account_type = data.get('account_type')

        # Check if username and user_password are provided
        if not username or not user_password or not account_type:
            return make_response({'error': 'All fields must be filled'}, 400)


        # Inserting user data into the database
        cursor.execute(f"INSERT INTO user_account VALUES('{user_id}','{username}','{user_password}','{account_type}')")
        conn.commit()
        type_id = 0

        cursor.execute("SELECT user_id FROM user_account ORDER BY user_id DESC LIMIT 1")
        user_id_insert = cursor.fetchone()
        cursor.execute(f"INSERT INTO {account_type} VALUES('{type_id}','{user_id_insert[0]}')")
        conn.commit()

        cursor.close()
        conn.close()
        return make_response({"success": "User registered successfully"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occurred'}, 500)



@app.route('/login', methods=['POST'])	
def user_login():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        username = data.get('username')
        user_password = data.get('user_password')
        account_type = data.get('account_type')

        # Check if username and user_password are provided
        if not username or not user_password or not account_type:
            return make_response({'error': 'Fill in all fields'}, 400)
        
        
        # Fetch user details from the database based on username and user_password
        cursor.execute(f"SELECT * FROM user_account WHERE username = '{username}' AND user_password = '{user_password}' AND account_type = '{account_type}'")
        user_data = cursor.fetchone()

        if user_data:
            # Successful login
            return make_response({'success': 'Login successful'}, 200)
        else:
            # Invalid credentials
            return make_response({'error': 'Invalid username or user_password or the account type selected is incorrect'}, 401)

        
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/courses/create', methods=['POST'])	
def create_courses():
    try:
        conn = get_db()
        cursor = conn.cursor()

        data = request.get_json()
        course_id = 0
        lecturer_id = data.get('lecturer_id')
        course_name = data.get('course_name')
        description = data.get('description')

        if not lecturer_id or not course_name or not description:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO course VALUES('{course_id}','{lecturer_id}','{course_name}','{description}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Course added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/courses', methods=['GET'])	
def retrieve_courses():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        #Retrieve all courses: /courses
        #Retrieve courses for a particular student: /courses?student_id=student_id
        #Retrieve courses taught by a particular lecturer: /courses?lecturer_id=lecturer_id
        student_id = request.args.get('student_id')
        lecturer_id = request.args.get('lecturer_id')
        
        if student_id:
            # Retrieve courses for a particular student
            cursor.execute(f"SELECT course_name FROM course WHERE student_id = '{student_id}'")
        elif lecturer_id:
            # Retrieve courses taught by a particular lecturer
            cursor.execute(f"SELECT course_name FROM course WHERE lecturer_id = '{lecturer_id}'")
        else:
            # Retrieve all courses if no query parameters provided
            cursor.execute('SELECT course_name FROM course')

        course_names = cursor.fetchall()
        course_list = [course[0] for course in course_names]
        
        
        cursor.close()
        conn.close()
        return make_response(course_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/courses/register', methods=['POST'])	
def register_for_course():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        student_id = data.get('student_id')
        course_id = data.get('course_id')
        grade = 0

        if not student_id or not course_id:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO assignedto VALUES('{student_id}','{course_id}','{grade}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Student registered"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/members', methods=['GET'])	
def retrieve_members():
    try:
        conn = get_db()
        cursor = conn.cursor()
        count = 0
        course_id = request.args.get('course_id')
        
        if course_id:
            cursor.execute(f"SELECT student_id FROM assignedto WHERE course_id = '{course_id}'")
        else:
            cursor.execute('SELECT course_id FROM course')
            course_names = [cid[0] for cid in cursor.fetchall()]
            cursor.execute('SELECT student_id,course_id FROM assignedto')

        student_course_ids = cursor.fetchall()
        if not course_id:
            student_ids = [row[0] for row in student_course_ids]
            course_ids = [row[1] for row in student_course_ids]
        else:
            student_ids = [row[0] for row in student_course_ids]
        user_ids = []
        member_names = []
        for student in student_ids:
            cursor.execute(f"SELECT user_id FROM student WHERE student_id = '{student}'")
            user_ids.append(cursor.fetchone())
        for user in user_ids:
            cursor.execute(f"SELECT username FROM user_account WHERE user_id = '{user[0]}'")
            member_name = cursor.fetchone()
            if not course_id and course_names:
                if course_ids[count] == course_names[0] :
                    cursor.execute(f"SELECT course_name FROM course WHERE course_id = '{course_names[0]}'")
                    course_names.pop(0)
                    course_name = cursor.fetchone()
                    member_names.append(course_name[0])
                count+=1
            member_names.append(member_name[0])
        
        if course_id:
            cursor.execute(f"SELECT course_name FROM course WHERE course_id = '{course_id}'")
            course_name = cursor.fetchone()
            member_names.insert(0,course_name[0])
            
        cursor.close()
        conn.close()
        return make_response(member_names, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/calendar/events', methods=['GET'])	
def retrieve_calender_events():
    try:
        conn = get_db()
        cursor = conn.cursor()

        #Retrieve all calendar events for a particular course: /calendar/events?course_id=course_id
        #Retrieve all calendar events for a particular date for a particular student: /calendar/events?student_id=student_id&assignment_due_date=yyyy-mm-dd
        
        course_id = request.args.get('course_id')
        student_id = request.args.get('student_id')
        assignment_due_date = request.args.get('assignment_due_date')
        event_list=[]
        if course_id:
            cursor.execute(f"SELECT event_title FROM calendar_event WHERE course_id = '{course_id}'")
            events = cursor.fetchall()
            event_list = [event[0] for event in events]
        elif student_id and assignment_due_date:
            cursor.execute(f"SELECT course_id FROM assignedto WHERE student_id = '{student_id}'")
            courses = cursor.fetchall()
            course_ids = [course[0] for course in courses]
            for course in course_ids:
                cursor.execute(f"SELECT event_title FROM calendar_event WHERE course_id = '{course}' and assignment_due_date = '{assignment_due_date}'")
                events = cursor.fetchall()
                #print([event[0] for event in events])
                event_list_temp = [event[0] for event in events]
                for event in event_list_temp:
                    event_list.append(event)
                    
        else:
            cursor.execute(f"SELECT event_title FROM calendar_event")
            events = cursor.fetchall()
            event_list = [event[0] for event in events]

        #events = cursor.fetchall()
        #event_list = [event[0] for event in events]
            
        cursor.close()
        conn.close()
        return make_response(event_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/calendar/events/create', methods=['POST'])	
def create_calender_events():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        event_id = 0
        course_id = data.get('course_id')
        event_description = data.get('event_description')
        event_title = data.get('event_title')
        assignment_due_date = data.get('assignment_due_date')

        if not event_description or not event_title or not assignment_due_date:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO calendar_event VALUES('{event_id}','{course_id}','{event_description}','{event_title}','{assignment_due_date}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Calendar event added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/forums', methods=['GET'])	
def retrieve_forums():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        course_id = request.args.get('course_id')
        
        if course_id:
            cursor.execute(f"SELECT forum_name FROM discussion_forum WHERE course_id = '{course_id}'")
        else:
            cursor.execute(f"SELECT forum_name FROM discussion_forum")

        forum_names = cursor.fetchall()
        forum_list = [forum[0] for forum in forum_names]
            
        cursor.close()
        conn.close()
        return make_response(forum_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/forums/create', methods=['POST'])	
def create_forums():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        forum_id = 0
        course_id = data.get('course_id')
        forum_name = data.get('forum_name')

        if not course_id or not forum_name:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO discussion_forum VALUES('{forum_id}','{course_id}','{forum_name}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Discussion forum added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/forums/discussions', methods=['GET'])	
def retrieve_discussion_thread():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        forum_id = request.args.get('forum_id')
        
        if forum_id:
            cursor.execute(f"SELECT thread_title FROM Discussion_thread WHERE forum_id = '{forum_id}'")
        else:
            cursor.execute(f"SELECT thread_title FROM Discussion_thread")

        thread_names = cursor.fetchall()
        thread_list = [thread[0] for thread in thread_names]
            
        cursor.close()
        conn.close()
        return make_response(thread_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/forums/discussions', methods=['POST'])	
def create_discussion_thread():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        thread_id = 0
        forum_id = data.get('forum_id')
        thread_title = data.get('thread_title')
        thread_content = data.get('thread_content')

        if not forum_id or not thread_title or not thread_content:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO discussion_thread VALUES('{thread_id}','{forum_id}','{thread_title}','{thread_content}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Thread Created"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)






@app.route('/courses/content', methods=['GET'])	
def retrieve_sections():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        course_id = request.args.get('course_id')
        
        if course_id:
            cursor.execute(f"SELECT section_title FROM section WHERE course_id = '{course_id}'")
        else:
            cursor.execute(f"SELECT section_title FROM section")

        section_names = cursor.fetchall()
        section_list = [section[0] for section in section_names]
            
        cursor.close()
        conn.close()
        return make_response(section_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/content/create', methods=['POST'])	
def create_section():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        
        section_id = 0
        course_id = data.get('course_id')
        section_title = data.get('section_title')
        lecture_slides = data.get('lecture_slides')
        links = data.get('links')

        if not course_id or not section_title or not lecture_slides or not links:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO section VALUES('{section_id}','{course_id}','{section_title}','{lecture_slides}','{links}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Course Content added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/content/section', methods=['GET'])	
def retrieve_section_items():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        section_id = request.args.get('section_id')
        
        if section_id:
            cursor.execute(f"SELECT item_title FROM section_item WHERE section_id = '{section_id}'")
        else:
            cursor.execute(f"SELECT item_title FROM section_item")

        item_names = cursor.fetchall()
        item_list = [item[0] for item in item_names]
            
        cursor.close()
        conn.close()
        return make_response(item_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/content/section/create', methods=['POST'])	
def create_section_item():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        data = request.get_json()
        
        item_id = 0
        course_id = data.get('course_id')
        section_id = data.get('section_id')
        item_title = data.get('item_title')
        item_content = data.get('item_content')

        if not course_id or not section_id or not item_title or not item_content:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"INSERT INTO section_item VALUES('{item_id}','{course_id}','{section_id}','{item_title}','{item_content}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Section Item added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/assignments', methods=['POST'])	
def submit_assignment():
    try:
        conn = get_db()
        cursor = conn.cursor()

        data = request.get_json()
        assignment_id = 0
        course_id = data.get('course_id')
        student_id = data.get('student_id')
        assignment_title = data.get('assignment_title')
        grade=0

        if not student_id or not assignment_title:
            return make_response({'error': 'All fields must be filled'}, 400)
            
        cursor.execute(f"SELECT * FROM assignedto WHERE student_id = '{student_id}' AND course_id = '{course_id}'")
        student_does_course = cursor.fetchone()

        if not student_does_course:
            return make_response({'error': 'There is no relationship between the the specified student and course'}, 404)

        cursor.execute(f"INSERT INTO assignment VALUES('{assignment_id}','{course_id}','{student_id}','{assignment_title}','{grade}')")
        conn.commit()
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Assignment Submitted"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/courses/grades', methods=['PUT'])	
def submit_grade():
    try:
        conn = get_db()
        cursor = conn.cursor()

        data = request.get_json()
        student_id = data.get('student_id')
        course_id = data.get('course_id')
        assignment_id = data.get('assignment_id')
        grade = data.get('grade')

        if not student_id or not course_id or not assignment_id or not grade:
            return make_response({'error': 'All fields must be filled'}, 400)

        cursor.execute(f"SELECT * FROM assignment WHERE student_id = '{student_id}' AND assignment_id = '{assignment_id}'AND course_id = '{course_id}'")
        assignment_exists = cursor.fetchone()

        if not assignment_exists:
            return make_response({'error': 'Assignment not found for the specified student and course'}, 404)

        # Update the grade for the assignment
        cursor.execute(f"UPDATE assignment SET grade = '{grade}' WHERE assignment_id = '{assignment_id}' AND course_id = '{course_id}' AND student_id = '{student_id}'")
        
        # Commit the transaction
        conn.commit()
        
        cursor.execute(f"SELECT grade FROM assignment WHERE student_id = '{student_id}' AND course_id = '{course_id}'")
        grades = [grade[0] for grade in cursor.fetchall()]
        average = sum(grades)/len(grades)
        
        cursor.execute(f"UPDATE assignedto SET average = '{average}' WHERE course_id = '{course_id}' AND student_id = '{student_id}'")
        conn.commit()
        
        
        cursor.close()
        conn.close()
        return make_response({"success" : "Grade Updated"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)



@app.route('/reports', methods=['GET'])	
def reports():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        info_list=[]
        
        cursor.execute('SELECT * FROM courses_with_50_plus_students')
        info = cursor.fetchall()
        course_ids = [row[0] for row in info]
        course_names = [row[1] for row in info]
        student_count = [row[2] for row in info]
        course_info=[]
        for x in range (len(course_ids)):
            course_info += [course_names[x]] + [student_count[x]]
        info_list += [["Courses with more than 50 Students"] + course_info]
        
        cursor.execute('SELECT * FROM students_with_5_plus_courses')
        info = cursor.fetchall()
        student_ids = [row[0] for row in info]
        course_count = [row[1] for row in info]
        student_info=[]
        for x in range (len(student_ids)):
            student_info += [student_ids[x]] + [course_count[x]]
        info_list += [["Students assigned to 5 or more Courses"] + student_info]
        
        cursor.execute('SELECT * FROM lecturers_with_3_plus_courses')
        info = cursor.fetchall()
        lecturer_ids = [row[0] for row in info]
        course_count = [row[1] for row in info]
        lecturer_info=[]
        for x in range (len(lecturer_ids)):
            lecturer_info += [lecturer_ids[x]] + [course_count[x]]
        info_list += [["Lecturers assigned to 3 or more Courses"] + lecturer_info]
        
        cursor.execute('SELECT * FROM top_10_enrolled_courses')
        info = cursor.fetchall()
        course_ids = [row[0] for row in info]
        course_names = [row[1] for row in info]
        student_count = [row[2] for row in info]
        course_info=[]
        for x in range (len(course_ids)):
            course_info += [course_names[x]] + [student_count[x]]
        info_list += [["Top 10 Enrolled Courses"] + course_info]
        
        cursor.execute('SELECT * FROM top_10_students_by_average')
        info = cursor.fetchall()
        student_ids = [row[0] for row in info]
        overall_avg = [row[1] for row in info]
        averages = []
        for x in range (len(student_ids)):
            averages += [student_ids[x]] + [overall_avg[x]]
        info_list += [["Top 10 Students by Overall Average"] + averages]
        
        
        cursor.close()
        conn.close()
        return make_response(info_list, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)
        

if __name__ == '__main__':
    app.run(port=6000)