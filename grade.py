from statistics import mean as m


admins = { "Python" : " Pass@123", "User2" : "Pass@456"}
students = {"Max": [23, 26, 30, 18],
            "Sophie":[30,30,29,27],
            "Giacomo":[18,18,23,25]}

def enterGrades():
	nameToEnter = input("Student Name: ")
	gradeToEnter = input("Grade: ")

	if nameToEnter in students:
		print("Adding Grade ...")
		students[nameToEnter].append(float(gradeToEnter))
	else:
		print("Student do not exist!")

   print(students)

def removeStudent():
	nameToRemove = input ("What student do you want to remove?: ")
	if removeStudent in students:
		print("Removing Student ...")
		del students[nameToRemove]

def studentsAvgs():
	for eachStudent in students:
		gradeList = students[eachStudent]
		avgGrade = m(gradeList)

		print(eachStudent, "has an average grade of:" , avgGrade)



def main():
	print("""Welcome to Grade Central

		Choose an Option:
	       [1] - Enter Grade
	       [2] - Remove Student
	       [3] - StudentAverage Grades
	       [4] - Exit
		""")


	action = input ("What whould you like to do today? (Enter a Number!) ")

	if action == "1":
		enterGrades()
		print("1")

	elif action == "2":
		removeStudent()
		print("2")
	elif action == "3":
		studentsAvgs()
		print("3")

	elif action == "4":
		exit()

	else:
		print("No valid choice was given, try again")

login = input("Username: ")
passw = input("Password: ")


if login in admins:
	if admins[login] == passw: 
		print("Welcome! ", login)
		while True:
			main();
	else:
		print("Invalid Password, try again suker!")

else:
	print("Invalid Username, insert again!")