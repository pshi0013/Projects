import random
import random
from user import User
from unit import Unit

class UserStudent(User):
    def __init__(self, user_id=1111111, user_name="Tom", user_password="", user_role="ST", user_status="enabled", enrolled_units=[("FIT9136", 80), ("FIT9131", 70)]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        enrolled_units_list = []
        for unit in self.enrolled_units:
            enrolled_units_list.append(unit)

        return f"{super().__str__()},{enrolled_units_list}"


    def student_menu(self):
        print("\nStudent menu:")
        print("1. List available units")
        print("2. List enrolled units")
        print("3. Enrol a unit")
        print("4. Drop a unit")
        print("5. Check unit score")
        print("6. Generate the score for a unit")
        print("7. Log out")

    def list_available_units(self):
        print("\nAvailable units: ")
        with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
            units = unit_file.readlines()
            for i in range(len(units)):
                unit_token = units[i].strip("\n").split(",")
                unit_code = unit_token[1]
                unit_name = unit_token[2]
                unit_cap = int(unit_token[3])
                enrol_stu = 0
                with open("data/user.txt", "r", encoding='utf-8') as user_file:
                    users = user_file.readlines()
                    for i in range(len(users)):
                        user_token = users[i].strip("\n").split(",")
                        if user_token[3] == "ST":

                            # Check if the student has the unit. If the student has this unit, enrol_stu will add one.
                            if not user_token.count("[('" + unit_code + "'") == 0:
                                enrol_stu += 1
                            elif not user_token.count(" ('" + unit_code + "'") == 0:
                                enrol_stu += 1

                    # Check if there is still space for students to enroll in; if it is available. students can enroll this unit.
                    if unit_cap > enrol_stu:
                        print("Unit code: " + unit_code + "   Unit name: " + unit_name)

    def list_enrolled_units(self):
        all_unit_list = []
        user_student_list = self.__str__().split(",")
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_token[1] == user_student_list[1]:
                    for i in range(len(user_token)):

                        # collect the unit and score into the list.
                        if i-4 > 0:
                            all_unit_list.append(user_token[i])

        if len(all_unit_list) == 0:
            print("You have not enrolled any units.")
        else:
            unit_code = []
            if len(all_unit_list) == 2:

                # Put the unitcode(s) of enrolled units into a list
                unitcode = all_unit_list[0].strip("[('")
                unit_code.append(unitcode)

            elif len(all_unit_list) == 4:
                unitcode_1 = all_unit_list[0].strip("[('")
                unit_code.append(unitcode_1)
                unitcode_2 = all_unit_list[2].strip(" ('")
                unit_code.append(unitcode_2)

            elif len(all_unit_list) == 6:
                unitcode_1 = all_unit_list[0].strip("[('")
                unit_code.append(unitcode_1)
                unitcode_2 = all_unit_list[2].strip(" ('")
                unit_code.append(unitcode_2)
                unitcode_3 = all_unit_list[4].strip(" ('")
                unit_code.append(unitcode_3)

            # Search for tht unit name and display the enrolled units
            print("\nList of enrolled units:")
            with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
                units = unit_file.readlines()
                for i in range(len(units)):
                    unit_token = units[i].strip("\n").split(",")
                    for each_unit in unit_code:
                         if unit_token[1] == each_unit:
                             print("Unit code: " + unit_token[1] + "   Unit name: " + unit_token[2])

    def enrol_unit(self, unit_code):
        user_student_list = self.__str__().split(",")

        # Check if the student already has this unit.
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_student_list[1] == user_token[1]:
                    if user_token.count("[('" + unit_code + "'") != 0 or user_token.count(" ('" + unit_code + "'") != 0:
                        print("You have already enrolled this unit.")

                    else:
                        # Check if the unit can be enrolled.
                        with open("data/unit.txt", "r", encoding='utf-8') as unit_file:
                            units = unit_file.readlines()
                            for i in range(len(units)):
                                unit_token = units[i].strip("\n").split(",")
                                if unit_token[1] == unit_code:
                                    unit_cap = int(unit_token[3])
                                    enrol_stu = 0
                                    with open("data/user.txt", "r", encoding='utf-8') as user_file:
                                        users = user_file.readlines()
                                        for i in range(len(users)):
                                            user_token = users[i].strip("\n").split(",")
                                            if user_token[3] == "ST":
                                                if not user_token.count("[('" + unit_code + "'") == 0:
                                                    enrol_stu += 1
                                                elif not user_token.count(" ('" + unit_code + "'") == 0:
                                                    enrol_stu += 1

                                    if unit_cap > enrol_stu:
                                        print("This unit is available.")
                                        print("You have successfully enrolled in this unit.")
                                        for i in range(len(users)):
                                            user_token = users[i].strip("\n").split(",")
                                            if user_token[1] == self.user_name:
                                                if len(user_token) == 5:
                                                    user_token.append("['(" + unit_code +"'")
                                                    user_token.append("-1)'")
                                                    print(user_token)

                                                elif len(user_token) > 5:
                                                    token_last = user_token[len(user_token) - 1].strip("]")
                                                    user_token[len(user_token)-1] = token_last
                                                    user_token.append(" ('" + unit_code + "'")
                                                    user_token.append(" -1)]")

                                            # add the unit information in the txt, file
                                            users[i] = ",".join(user_token) + "\n"
                                        with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                            user_file.writelines(users)

                                    elif unit_cap <= enrol_stu:
                                        print("The unit is not available.")

    def drop_unit(self, unit_code):
        user_student_list = self.__str__().split(",")

        # Check if the student has this unit.
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_student_list[1] == user_token[1]:

                    # The student doesn't have this unit.
                    if user_token.count("[('" + unit_code + "'") == 0 and user_token.count(" ('" + unit_code + "'") == 0:
                        print("You don't have this unit.")

                    # The student has this unit.
                    elif user_token.count("[('" + unit_code + "'") != 0:
                        user_token.pop(5)
                        user_token.pop(5)
                        character = "["
                        if len(user_token) > 5:
                            user_token[5].strip()
                            user_token[5] = character + user_token[5].strip()
                            print("You have dropped the unit successfully.")

                            # Update the information in the txt.file
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)
                        else:
                            print("You have dropped the unit successfully.")
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
                            print("You have dropped the unit successfully.")
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)

                        else:
                            user_token.pop(unit_index)
                            user_token.pop(unit_index)
                            print("You have dropped the unit successfully.")
                            users[i] = ",".join(user_token) + "\n"
                            with open("data/user.txt", "w", encoding='utf-8') as user_file:
                                user_file.writelines(users)

    def check_score(self, unit_code):
        user_student_list = self.__str__().split(",")

        # Check if the student has enrolled any unit or has enrolled this unit
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_student_list[1] == user_token[1]:
                    if len(user_token) == 5:
                        print("You have not enrolled any unit.")
                    else:
                        if not unit_code == "":
                            if user_token.count("[('" + unit_code + "'") == 0 and user_token.count(" ('" + unit_code + "'") == 0:
                                print("You don't have this unit.")

                            else:
                                # The student has enrolled this unit.
                                if user_token.count("[('" + unit_code + "'") != 0:
                                    score = user_token[6].strip(")'")
                                    print("Your score for " + unit_code +" is:" + score)

                                elif user_token.count(" ('" + unit_code + "'") != 0:
                                    index = user_token.index(" ('" + unit_code + "'")
                                    if index == len(user_token) - 2 :
                                        score = user_token[index + 1].strip(")]'")
                                        print("Your score for " + unit_code +" is:" + score)

                                    else:
                                        score = user_token[index + 1].strip(")'")
                                        print("Your score for " + unit_code + " is:" + score)

                        # If the input of 'unit_code' field is empty, display the scores for all units the student has.
                        elif unit_code == "":
                            all_unit_list = []
                            unit_list = []
                            score_list = []
                            for i in range(len(user_token)):
                                if i-4 > 0:
                                    all_unit_list.append(user_token[i])
                                    print(all_unit_list)

                            # Check the student's enrolled units
                            if len(all_unit_list) == 0:
                                print("You have not enrolled any unit.")

                            elif len(all_unit_list) == 2:
                                unit_list.append(all_unit_list[0].strip("[('"))
                                score_list.append(all_unit_list[1].strip(")]'"))
                                print(unit_list)
                                print(score_list)

                            elif len(all_unit_list) == 4:
                                unit_list.append(all_unit_list[0].strip("[('"))
                                score_list.append(all_unit_list[1].strip(")'"))
                                unit_list.append(all_unit_list[2].strip(" ('"))
                                score_list.append(all_unit_list[3].strip(")]'"))
                                print(unit_list)
                                print(score_list)

                            elif len(all_unit_list) == 6:
                                unit_list.append(all_unit_list[0].strip("[('"))
                                score_list.append(all_unit_list[1].strip(")'"))
                                unit_list.append(all_unit_list[2].strip(" ('"))
                                score_list.append(all_unit_list[3].strip(")'"))
                                unit_list.append(all_unit_list[4].strip(" ('"))
                                score_list.append(all_unit_list[5].strip(")]'"))
                                print(unit_list)
                                print(score_list)

                            for i in range(len(unit_list)):
                                print("Your score for " + unit_list[i] + " is:" + score_list[i])


    def generate_score(self, unit_code):
        user_student_list = self.__str__().split(",")

        # Check if the student has enrolled any unit or has this unit
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")
                if user_student_list[1] == user_token[1]:
                    if len(user_token) == 5:
                        print("You have not enrolled any unit.")

                    else:
                        if user_token.count("[('" + unit_code + "'") == 0 and user_token.count(" ('" + unit_code + "'") == 0:
                            print("You don't have this unit.")

                        else:
                            # Generate a score for the unit
                            if user_token.count("[('" + unit_code + "'") != 0:
                                score = str(random.randint(0,100))
                                user_token[6] = " " + score + ")"
                                print("Score: " + score + " for " + unit_code + " has been generated.")

                            elif user_token.count(" ('" + unit_code + "'") != 0:
                                index = user_token.index(" ('" + unit_code + "'")
                                if index == len(user_token) - 2 :
                                    score = str(random.randint(0, 100))
                                    user_token[index + 1] = " " + score + ")]"
                                    print("Score: " + score + " for " + unit_code + " has been generated.")

                                else:
                                    score = str(random.randint(0, 100))
                                    user_token[index + 1] = " " + score + ")"
                                    print("Score: " + score + " for " + unit_code + " has been generated.")

                # Update the information in the txt.file
                users[i] = ",".join(user_token) + "\n"
                with open("data/user.txt", "w", encoding='utf-8') as user_file:
                    user_file.writelines(users)