import mysql.connector

connection = mysql.connector.connect(user='justing498',
                                     password='232149427',
                                     host='10.8.37.226',
                                     database='justing498_db')

cursor = connection.cursor()
DepartmentNames = " SELECT DepartmentName FROM Departments"
cursor.execute(DepartmentNames)
for row in cursor:
    print(row[0])
spInput = input("Select a department and get all it's teachers, enter 'Exit' to close")

SP = f"CALL Department_Teachers('{spInput}')"
cursor.execute(SP)

for row in cursor:
    print(row[0])

cursor.close()
connection.close()

