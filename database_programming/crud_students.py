import sqlite3
import pandas as pd
def create():
    name=input("Enter student name: ")
    attendance=float(input("Enter student attendance: "))
    marks=float(input("Enter student marks: "))
    result= "Pass" if marks >= 40 else "Fail"
    conn=sqlite3.connect('college.db')
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO tbl_students (name, attendance, marks, result)
                      VALUES (?, ?, ?, ?)''', (name, attendance, marks, result))
    conn.commit()
    conn.close()
def update():
    id=int(input("Enter student ID to update: "))
    name=input("Enter new student name: ")
    attendance=float(input("Enter new student attendance: "))
    marks=float(input("Enter new student marks: "))
    result= "Pass" if marks >= 40 else "Fail"
    conn=sqlite3.connect('college.db')
    cursor=conn.cursor()
    cursor.execute('''UPDATE tbl_students
                      SET name=?, attendance=?, marks=?, result=?
                      WHERE id=?''', (name, attendance, marks, result, id))
    conn.commit()
    conn.close()
def delete():
    id=int(input("Enter student ID to delete: "))
    conn=sqlite3.connect('college.db')
    cursor=conn.cursor()
    cursor.execute('''DELETE FROM tbl_students WHERE id=?''', (id,))
    conn.commit()
    conn.close()
def read():
    conn=sqlite3.connect('college.db')
    cursor=conn.cursor()
    df=pd.read_sql_query('''SELECT * FROM tbl_students''', conn)
    print(df)
    conn.close()
def get_student_by_id():
    student_id=int(input("Enter student ID to fetch: "))
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM tbl_students WHERE id=?''', (student_id,))
    student = cursor.fetchone()
    conn.close()
    print(f"Record Found: {student}")


while True:
    print("\nStudent Management System")
    print("1. Create Student Record")
    print("2. Update Student Record")
    print("3. Delete Student Record")
    print("4. Read Student Records")
    print("5. Get Student by ID")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        create()
    elif choice==2:
        update()
    elif choice==3:
        delete()
    elif choice==4:
        read()
    elif choice==5:
        get_student_by_id()
    elif choice==6:
        break
    else:
        print("Invalid choice. Please try again.")