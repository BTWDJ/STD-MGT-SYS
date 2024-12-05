import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="8585",  
    database="student_db"  
)
cursor = conn.cursor()
print("****************************************************************")
print("                STUDENT MANAGEMENT SYSTEM                ")
print("****************************************************************")

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    Class INT,
    subject VARCHAR(10),
    fees INT       
)
""")

def add():
    print("-----ADD A STUDENT RECORD-----")
    DJ = int(input("Enter the no. of records you want to add: "))
    for i in range(DJ):
        roll_no = int(input("Enter student's Roll_no: "))
        name = input("Enter student Name: ")
        Class = int(input("Enter student's Class: "))
        subject = input("Enter student Subject: ")
        fees = int(input("Enter the fees: "))
        query = "INSERT INTO students (roll_no, name, Class, subject, fees) VALUES (%s, %s, %s, %s, %s)"
        values = (roll_no, name, Class, subject, fees)
        cursor.execute(query, values)
        conn.commit()
        print("Student added successfully!")

def search():
    print("-----SEARCH A STUDENT BY ROLL_NO-----")
    roll = input("Enter student's roll_no to search: ")
    query = "SELECT * FROM students WHERE roll_no LIKE %s"
    values = (f"%{roll}%",)
    cursor.execute(query, values)
    results = cursor.fetchall()
    if results:
        for student in results:
            print(f"Roll_no: {student[0]}, Name: {student[1]}, Class: {student[2]}, Subject: {student[3]}, Fee: {student[4]}")
    else:
        print("No such Student found.")

def show():
    print("-----SHOW A STUDENT RECORD-----")
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    if results:
        for student in results:
            print(f"Roll_no: {student[0]}, Name: {student[1]}, Class: {student[2]}, Subject: {student[3]}, Fee: {student[4]}")
    else:
        print("No students found.")

def delete():
    print("-----DELETE A STUDENT RECORD BY ROLL_NO-----")
    TG = int(input("Enter student's Roll_no to delete: "))
    try:
        query = "DELETE FROM students WHERE roll_no = %s"
        values = (TG,)
        cursor.execute(query, values)
        conn.commit()
        print("Student deleted successfully!")
    except:
        conn.rollback()

def update():
    print("-----UPDATE A STUDENT RECORD------")
    roll_no = int(input("Enter student roll_no to update: "))
    name = input("Enter new name: ")
    Class = int(input("Enter updated Class: "))
    subject = input("Enter new Subject: ")
    fees = int(input("Enter New Fee: "))
    query = "UPDATE students SET name = %s, Class = %s, subject = %s, fees = %s WHERE roll_no = %s"
    values = (name, Class, subject, fees, roll_no)
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1 FOR ADD STUDENT RECORD")
        print("2 FOR SEARCH STUDENT RECORD")
        print("3 FOR SHOW STUDENT RECORD")
        print("4 FOR UPDATE STUDENT RECORD")
        print("5 FOR DELETE STUDENT RECORD")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add()
        elif choice == '2':
            search()
        elif choice == '3':
            show()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

cursor.close()
conn.close()
