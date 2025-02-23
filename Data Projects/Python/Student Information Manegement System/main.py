# Student information: Peichun Shih - 33475881, Rachna Radhakrishna - 33573506, Laxin Marsha Pinto - 33599777
# Creation date: 23/04/2023 Last modified date: 05/05/2023
# This code is for a Student Management System with multiple users (admin, teacher, student)
# It utilizes two text files with unit and user information stored.
# Here it asks the user to enter the username and password and the main menu function displays all the available
# operations for the user to choose. The menu function handles all the user inputs,methods and classes and checks for
# validations.The “logout” option allows the user to logout from the user menu and displays the main menu.


from user import User
from unit import Unit
from user_student import UserStudent
from user_teacher import UserTeacher
from user_admin import UserAdmin
import re


def main_menu():
	print("\nWelcome to Student Information Management System!")
	print("1.Admin")
	print("2.Teacher")
	print("3.Student")
	print("4.Exit")


def generate_test_data():
	unit1 = Unit(1000000,"FIT9136","Algorithms and programming foundations in Python",10)
	unit2 = Unit(2000000,"FIT9131","Programming foundations in Java",5)
	unit3 = Unit(3000000,"FIT9132","Introduction to databases",10)

	with open("data/unit.txt", "w", encoding='utf-8') as unit_file:
		unit_file.write(unit1.__str__() + "\n")
		unit_file.write(unit2.__str__() + "\n")
		unit_file.write(unit3.__str__() + "\n")

	admin = UserAdmin(11111,"admin","password","AD","enabled")

	teachers = [UserTeacher(12222,"Taylor","^^^w!J#8$U%X&1($$$","TA","enabled",["FIT9136"]),
				UserTeacher(13333,"Bruno","^^^e!1#4$W%X&$$$","TA","enabled",["FIT9131"]),
				UserTeacher(14444,"Chen","^^^f!Q#N$W%$$$","TA","enabled",["FIT9132"])]

	students = [UserStudent(15555,"Tom","^^^w!X#V$$$$","ST","enabled",[("FIT9136", 80), ("FIT9131", 70)]),
				UserStudent(16666,"Jack","^^^m!J#L$T%$$$","ST","enabled",[("FIT9132", 60), ("FIT9136", 50), ("FIT9131", 40)]),
				UserStudent(17777,"John","^^^m!X#Q$W%$$$","ST","enabled",[("FIT9132", 70)]),
				UserStudent(18888,"Cindy","^^^f!R#W$M%8&$$$","ST","enabled",[("FIT9136", 30)]),
				UserStudent(19999,"Quinn","^^^t!4#R$W%W%$$$","ST","disabled",[("FIT9131", 20), ("FIT9136", 40)]),
				UserStudent(21111,"Brian","^^^e!1#R$J%W&$$$","ST","enabled",[("FIT9132", 60), ("FIT9136", 50)]),
				UserStudent(22222,"Linda","^^^o!R#W$M%J&$$$","ST","enabled",[("FIT9136", 50), ("FIT9132", 40)]),
				UserStudent(23333,"Wendy","^^^z!N#W$M%8&$$$","ST","enabled",[("FIT9132", 50), ("FIT9136", 60)]),
				UserStudent(24444,"Kony","^^^n!X#W$8%$$$","ST","enabled",[("FIT9131", 60), ("FIT9136", 70)]),
				UserStudent(25555,"Gina","^^^j!R#W$J%$$$","ST","enabled",[("FIT9131", 40), ("FIT9136", 90), ("FIT9132", 70)])]

	with open("data/user.txt", "w", encoding='utf-8') as user_file:
		user_file.write(admin.__str__() + "\n")
		for i in range(len(teachers)):
			user_file.write(teachers[i].__str__() + "\n")
		for i in range(len(students)):
			user_file.write(students[i].__str__() + "\n")

def main():
	generate_test_data()

	# Validate the input
	while True:
		main_menu()
		choice = input("Please enter your choice: ")
		if len(choice.strip()) == 0:
			print("Invalid input. Please enter again.")

		elif not choice.isdigit():
			print("Please enter a number.")
			print("Invalid input. Please enter again.")

		elif choice == "1":
			user = User()

			# Validate the input of user name for the admin
			pattern = r'^\w+$'
			user_name = input("\nEnter user name: ")
			if not re.match(pattern, user_name):
				print("Invalid input.\nUser name can only contain letters, numbers, and underscores. Please try again.")
			else:
				user_password = input("Enter password: ")
				user_token = user.login(user_name, user_password)
				if user_token == None:
					print("Login attempt unsuccessful! Please try again.")

				elif user_token[3] == "AD":
					print("Login successful!")
					user_admin = UserAdmin(User)
					while True:
						user_admin.admin_menu()
						admin_choice = input("Please enter your choice: ")

						# Validate the admin's input
						if len(admin_choice) != 1 or not admin_choice.isdigit() or not (
								1 <= int(admin_choice) <= 7):
							print("Invalid input. Please enter a number between 1 and 7.")

						else:
							if admin_choice == '1':
								search_user_name = input("Please enter the name of the user you want to search: ")
								user_admin.search_user(search_user_name)

							elif admin_choice == '2':
								user_admin.list_all_users()

							elif admin_choice == '3':
								user_admin.list_all_units()

							elif admin_choice == '4':
								admin_enable = input("Please enter the name you want to search to change the status: ")
								user_admin.enable_disable_user(admin_enable)

							elif admin_choice == '5':
								add_user = User()
								add_user_id = add_user.generate_user_id()
								print(
									"Create a username for the new user. The username can contain only alphabets, numbers and underscores")

								# Validate the input of adding user name
								while True:
									add_user_name = input("Enter the user name: ")
									check_username = add_user.check_username_exist(add_user_name)
									pattern = r'^\w+$'
									if not re.match(pattern, add_user_name):
										print("Invalid input.\nUser name can only contain letters, numbers, and underscores. Please try again.")

									elif check_username == True:
										print("The user name has been used. Please try a different username")

									else:
										break

								add_user_password = add_user.encrypt(add_user_name)

								# Validate the input of adding user role
								while True:
									add_user_role = input("Enter the user role: ")
									if add_user_role != "ST" and add_user_role != "TA" and add_user_role != "AD":
										print("Invalid input.\nUser role can only be 'ST', 'TA' or 'AD'. Please try again.")
									else:
										break

								# Validate the input of adding user role
								while True:
									add_user_status = input("Enter the user status (enabled / disabled): ")
									if add_user_status != "enabled" and add_user_status != "disabled":
										print("Invalid input.\nUser role can only be 'enabled' or 'disabled'. Please try again.")
									else:
										break

								add_user = User(add_user_id, add_user_name, add_user_password, add_user_role, add_user_status)
								user_admin.add_user(add_user)
								print(f"The new user details are: {add_user}")

							elif admin_choice == '6':
								delete_user_name = input("To delete a user, please enter the name of the user : ")
								user_admin.delete_user(delete_user_name)

							elif admin_choice == '7':
								print("Logged out successfully. Returning to main menu")
								main()

							else:
								print("Invalid choice. Please enter a valid choice.")


		elif choice == "2":
			user = User()

			# Validate the input of user name for the teacher
			pattern = r'^\w+$'
			while True:
				user_name = input("\nEnter user name: ")
				if not re.match(pattern, user_name):
					print(
						"Invalid input.\nUser name can only contain letters, numbers, and underscores. Please try again.")
				else:
					user_password = input("Enter password: ")
					user_token = user.login(user_name, user_password)
					if user_token == None:
						print("Unsuccessful login! Please try again.")
					elif user_token[3] == "TA":
						print("Login successful!")

						unit_list = []
						for i in range(len(user_token)):
							if i > 4:
								unit_list.append(user_token[i].strip())
						user_teacher = UserTeacher(user_token[0], user_token[1], user_token[2], user_token[3], user_token[4],unit_list)

						while True:
							user_teacher.teacher_menu()
							teacher_choice = input("Please enter your choice: ")

							# Validate the teacher's input
							if len(teacher_choice) != 1 or not teacher_choice.isdigit() or not (
									1 <= int(teacher_choice) <= 6):
								print("Invalid input. Please enter a number between 1 and 6.")

							else:
								if teacher_choice == '1':
									search_user_name = user_name
									print(search_user_name)
									user_teacher.list_teach_unit()


								elif teacher_choice == '2':
									add_unit = Unit()
									unit_id = add_unit.generate_unit_id()
									unit_code = input("Enter the unit code:")
									unit_name = input("Enter the unit name:")
									unit_capacity = input("Enter the unit capacity:")
									if not unit_capacity.isdigit():
										print("Invalid input")

									else:
										with open('data/unit.txt', 'r', encoding='utf-8') as unit_file:
											for unit_line in unit_file:
												unit_token = unit_line.strip().split(',')
												if unit_token[1] == unit_code:
													print("This unit already exists")
													break

												else:
													add_unit = Unit(unit_id, unit_code, unit_name, unit_capacity)
													user_teacher.add_teach_unit(add_unit)
													print("The new unit added is: ", add_unit)
													break

								elif teacher_choice == "3":
									unit_list = []
									unit_code = input("Please enter the unit code: ")
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_teacher.delete_teach_unit(unit_code)

										else:
											print("This unit does not exist!")

								elif teacher_choice == "4":
									unit_list = []
									unit_code = input("Please enter the unit code: ")
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_teacher.list_enrol_student(unit_code)

										else:
											print("This unit does not exist!")

								elif teacher_choice == "5":
									unit_list = []
									unit_code = input("Please enter the unit code: ")
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_teacher.show_unit_avg_max_min_score(unit_code)

										else:
											print("This unit does not exist!")

								elif teacher_choice == "6":
									print("Logged out successfully. Returning to main menu")
									main()

		elif choice == "3":
			user = User()

			# Validate the input of user name for the student
			pattern = r'^\w+$'
			while True:
				user_name = input("\nEnter user name: ")
				if not re.match(pattern, user_name):
					print("Invalid input.\nUser name can only contain letters, numbers, and underscores. Please try again.")
				else:
					user_password = input("Enter password: ")
					user_token = user.login(user_name, user_password)
					if user_token == None:
						print("Login attempt unsuccessful! Please try again.")
					elif user_token[3] == "ST":
						print("Login successful!")
						print(user_token)
						unit_list = []
						for i in range(len(user_token)):
							if i > 4:
								unit_list.append(user_token[i])

						user_student = UserStudent(user_token[0], user_token[1], user_token[2], user_token[3], user_token[4], unit_list)

						while True:
							user_student.student_menu()
							student_choice = input("Please enter your choice: ")

							# Validate the teacher's input
							if len(student_choice) != 1 or not student_choice.isdigit() or not (
									1 <= int(student_choice) <= 7):
								print("Invalid input. Please enter a number between 1 and 7.")

							else:
								if student_choice == "1":
									user_student.list_available_units()

								elif student_choice == "2":
									user_student.list_enrolled_units()

								elif student_choice == "3":
									unit_list = []
									with open("data/user.txt", "r", encoding='utf-8') as user_file:
										users = user_file.readlines()
										for i in range(len(users)):
											user_token = users[i].strip("\n").split(",")
											if user_token[1] == user_name:
												for i in range(len(user_token)):
													if i - 4 > 0:
														unit_list.append(user_token[i])

									# Check if the student has already enrolled three units
									if len(unit_list) == 6:
										print("You have enrolled the maximum three units.")

									else:
										unit_list = []
										unit_code = input("Please enter the unit code: ")

										# Check if the unit exists
										with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
											units = unit_file.readlines()
											for i in range(len(units)):
												unit_token = units[i].strip("\n").split(",")
												unit_list.append(unit_token[1])
											if unit_code in unit_list:
												user_student.enrol_unit(unit_code)
											else:
												print("This unit does not exist!")

								elif student_choice == "4":
									unit_list = []
									unit_code = input("Please enter the unit code: ")

									# Check if the unit exists
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_student.drop_unit(unit_code)
										else:
											print("This unit does not exist!")

								elif student_choice == "5":
									unit_list = []
									unit_code = input("Please enter the unit code: ")

									# Check if the unit exists
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_student.check_score(unit_code)
										else:
											print("This unit does not exist!")

								elif student_choice == "6":
									unit_list = []
									unit_code = input("Please enter the unit code: ")

									# Check if the unit exists
									with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
										units = unit_file.readlines()
										for i in range(len(units)):
											unit_token = units[i].strip("\n").split(",")
											unit_list.append(unit_token[1])
										if unit_code in unit_list:
											user_student.generate_score(unit_code)
										else:
											print("This unit does not exist!")

								elif student_choice == "7":
									print("Logged out successfully. Returning to main menu")
									main()

		elif choice == "4":
			print("Exiting the program. Good bye!")
			break


if __name__ == "__main__":
	main()

