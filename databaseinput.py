import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="!!!", passwd="!!!", database="assignment")
cursor = myconn.cursor()
val= []
student_info= ("First_name", "Middle_name", "Last_name", "Gender", "Level1", "Age", "Course", "Address")
querry= "INSERT INTO student_info(First_name, Middle_name, Last_name, Gender, Level1, Age, Course, Address) values(%s, %s, %s, %s, %s, %s, %s,%s )"
for student in range(8):
    user= input(f"Enter your {student_info[student]}: ")
    val.append(user)
cursor.execute(querry, val)    
myconn.commit()
cursor.close()
print(val)
