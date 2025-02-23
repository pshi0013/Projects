import random
from user import User
from unit import Unit

class UserAdmin(User):
    def __init__(self, user_id=11111, user_name='', user_password='', user_role='AD', user_status='enabled'):
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        return f"{super().__str__()}"

    def admin_menu(self):
        print("Admin menu:")
        print("1. Search user information")
        print("2. List all user information")
        print("3. List all unit information")
        print("4. Enable/Disable user")
        print("5. Add user")
        print("6. Delete user")
        print("7. Log out")

    def search_user(self, user_name):
        with open('data/user.txt', 'r', encoding='utf-8') as user_file:
            for user in user_file:
                user_token = user.strip().split(',')
                #compares to check if the name stored in the user.txt file matches with the name input by the admin
                if user_token[1] == user_name:
                    print(f"Here are the details of '{user_name}':", user_token)
                    return
            print(f"User '{user_name}' not found.")

    def list_all_users(self):
        with open('data/user.txt', 'r', encoding='utf-8') as user_file:
            user_lines = user_file.readlines()
            for line in user_lines:
                user_token = line.strip().split(",")
                #check if necessary user data is present
                if len(user_token) >= 5:
                    print(user_token)


    def list_all_units(self):
        with open('data/unit.txt', 'r', encoding='utf-8') as unit_file:
            for unit in unit_file:
              unit_tokens = unit.strip().split(",")
              #access and assign each element, then print to display
              unit_id = unit_tokens[0]
              unit_code = unit_tokens[1]
              unit_name = unit_tokens[2]
              unit_capacity = unit_tokens[3]
              print(f"Unit ID: {unit_id}, Unit Code: {unit_code}, Unit Name: {unit_name}, Unit Capacity: {unit_capacity}")



    def enable_disable_user(self, user_name):
        with open('data/user.txt', 'r+', encoding='utf-8') as user_file:
            user = user_file.readlines()
            for i in range(len(user)):
                user_token = user[i].strip().split(',')
                if user_token[1] == user_name:
                    #access the status of the user, if enabled switch to disabled and vice versa
                    if user_token[4] == "enabled":
                        user_token[4] = "disabled"
                    else:
                        user_token[4] = "enabled"
                    #makes modifications to the user.txt file
                    user[i] = ",".join(user_token) + "\n"
                    user_file.seek(0)
                    user_file.writelines(user)
                    print(f"User {user_name} status updated to {user_token[4]}")
                    break

                if user_token is None:
                    print("User not found")

    def add_user(self, user_obj):
        with open('data/user.txt', 'a', encoding='utf-8') as user_file:
            # get the user information from the user object
            user_id = user_obj.user_id
            user_name = user_obj.user_name
            user_password = user_obj.user_password
            user_role = user_obj.user_role
            user_status = user_obj.user_status

            # write the user information to the file as a new line
            user_file.write(f"{user_id},{user_name},{user_password},{user_role},{user_status}\n")

    def delete_user(self, user_name):
        with open('data/user.txt', 'r', encoding='utf-8') as user_file:
            users = user_file.readlines()
            for user in users:
                user_token = user.strip().split(',')
                #matches the input of user name with the name in the user.txt file
                #uses .remove to delete information corresponding to that user
                if user_token[1] == user_name:
                    print("The details of the user entered are:", ", ".join(user_token))
                    users.remove(user)
                    #write the  changes to the text file
                    with open('data/user.txt', 'w', encoding='utf-8') as updated_user_file:
                        updated_user_file.writelines(users)
                    print(f"User {user_name} has been deleted.")
                    return
            print(f"User {user_name} cannot be found.")


