import mysql.connector

connection = mysql.connector.connect(user='justing498',
                                     password='232149427',
                                     host='10.8.37.226',
                                     database='justing498_db')

cursor = connection.cursor()
DepartmentNames = " SELECT DepartmentName FROM Departments"
cursor.execute(DepartmentNames)
depList = []
numCount = 1
for row in cursor:
    depList.append(row[0])
    print(numCount, row[0])
    numCount+=1
spInput = input("Select a department by number and get all it's teachers: ")

SP = f"CALL Department_Teachers('{depList[int(spInput)-1]}')"
cursor.execute(SP)

for row in cursor:
    print(row[0])

cursor.close()
connection.close()

