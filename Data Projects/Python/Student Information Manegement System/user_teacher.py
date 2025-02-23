from user import User
from unit import Unit

class UserTeacher(User):

    def __init__(self, user_id = 22222, user_name = "Jerry", user_password = " ", user_role = "TA", user_status = "enabled", teach_units = ["FIT9136", "FIT9132"]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.teach_units = teach_units

    def __str__(self):
        return f"{super().__str__()}, {','.join(self.teach_units)}"

    def teacher_menu(self):
        print("\nTeacher menu:")
        print("1. List all taught units")
        print("2. Add a new unit")
        print("3. Delete a taught unit")
        print("4. List the enrolled students in a unit")
        print("5. Show the average, max, and min score in a unit")
        print("6. Log out")

    def list_teach_unit(self):
        if len(self.teach_units) == 0:
            print("No units are found in the system.")

        else:
            print("The list of taught units: \n")
            for unit_code in self.teach_units:
                with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
                    for unit in unit_file:
                        unit_token = unit.split(",")
                        #matches the code of the unit input with the unit.txt file
                        if unit_token[1] == unit_code:
                            print(f"{unit_token[1]}: {unit_token[2]}")

    def add_teach_unit(self, unit_obj):
        # Write the new unit in the unit.txt
        with open('data/unit.txt', 'r+',encoding='utf-8') as unit_file:
            for unit in unit_file:
                unit_token = unit.strip().split(',')
                unit_id = unit_obj.unit_id
                unit_code = unit_obj.unit_code
                unit_name = unit_obj.unit_name
                unit_capacity = unit_obj.unit_capacity
                unit_file.write(f"{unit_id},{unit_code},{unit_name},{unit_capacity}")

        # Write the new unit in the user.txt
        with open ('data/user.txt', 'r+', encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_token[1] == self.user_name:
                    self.teach_units.append(unit_code)
                    user_token[5] = self.teach_units
                    for i in range(len(users)):
                        if user_token[1] in users[i]:
                            users[i] = self.__str__() + "\n"
            user_file.seek(0)
            user_file.writelines(users)


    def delete_teach_unit(self, unit_code):
        # removes the unit_code from the unit.txt file
        if unit_code not in self.teach_units:
            print("Unit: " + unit_code + " is not taught by the teacher.")


        else:
            self.teach_units.remove(unit_code)

            with open("data/unit.txt", "r+", encoding='utf-8') as unit_file:
                unit_list = []
                units = unit_file.readlines()
                for i in range(len(units)):
                    unit_token = units[i].strip("\n").split(",")
                    unit_list.append(unit_token[1])

                index = unit_list.index(unit_code)
                units.pop(index)
                unit_file.seek(0)
                unit_file.truncate()
                unit_file.writelines(units)

            # removes the given unit_code from the teacher's list of taught units
            user_teacher_list = self.__str__().split(",")
            with open("data/user.txt", "r+", encoding='utf-8') as user_file:
                users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_teacher_list[1] == user_token[1]:
                    n_unit_code = " " + unit_code
                    user_token.remove(n_unit_code)
                    users[i] = ",".join(user_token) + "\n"
                    with open("data/user.txt", "w", encoding='utf-8') as user_file:
                        user_file.writelines(users)

                    # removes the unit_code from any students' lists of enrolled units in the user.txt file.
                elif user_token[3] == "ST":
                    if user_token.count("[('" + unit_code + "'") != 0:
                        user_token.pop(5)
                        user_token.pop(5)
                        character = "["
                        if len(user_token) > 5:
                            user_token[5].strip()
                            user_token[5] = character + user_token[5].strip()
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                    user_file.writelines(users)
                        else:
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)

                    elif user_token.count(" ('" + unit_code + "'") != 0:
                        unit_index = user_token.index(" ('" + unit_code + "'")
                        if unit_index == len(user_token)-2:
                            user_token.pop(unit_index)
                            user_token.pop(unit_index)
                            character = "]"
                            user_token[unit_index-1] = user_token[unit_index-1] + character
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)

                        else:
                            user_token.pop(unit_index)
                            user_token.pop(unit_index)
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)

    def list_enrol_student(self, unit_code):
        enrol_student = []
        if not unit_code in self.teach_units:
                print("Unit: " + unit_code + " is not taught by the teacher.")
        else:
            with open("data/user.txt", "r+", encoding='utf-8') as user_file:
                users = user_file.readlines()
                for i in range(len(users)):
                    user_token = users[i].strip("\n").split(",")
                    #print(user_token)
                    # checks if user is a student
                    if user_token[3] =='ST':
                        # check whether student is enrolled in the unit
                        if user_token.count("[('" + unit_code + "'") > 0:
                            print(user_token)

                        elif user_token.count(" ('" + unit_code + "'") > 0:
                            print(user_token)


    def show_unit_avg_max_min_score(self, unit_code):
        if unit_code not in self.teach_units:
            print("Unit: " + unit_code + " is not taught by the teacher.")

        else:
            score_list = []
            with open("data/user.txt", "r", encoding='utf-8') as user_file:
                users = user_file.readlines()
                #iterate through students enrolled in unit
                for i in range(len(users)):
                    user_token = users[i].strip("\n").split(",")
                    if user_token[3] == 'ST':
                        if user_token.count("[('" + unit_code + "'") > 0:
                            score = int(user_token[6].strip().strip(")]").strip(")"))
                            score_list.append(score)

                        elif user_token.count(" ('" + unit_code + "'") != 0:
                            unit_index = user_token.index(" ('" + unit_code + "'")
                            score = int(user_token[unit_index + 1].strip().strip(")]").strip(")"))
                            score_list.append(score)

                if len(score_list) == 0:
                    print("No score for this unit.")
                #calculates average, minimum and maximum if scores are present
                else:
                    maximum = round(max(score_list), 2)
                    minimum = round(min(score_list), 2)
                    average = round((sum(score_list) / len(score_list)),2)
                    print("Unit: " + unit_code + "\nThe maximum score is: " + str(maximum) + "\nThe minimum score is: " + str(minimum) + "\nThe average score is: " + str(average))