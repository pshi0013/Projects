"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the AdminOperation class which implements the methods related to admins.
"""

import string
import random
import time
from model_admin import Admin
from operation_user import UserOperation

class AdminOperation():
    """
    A class used to operate methods related to admins

    Methods
    -------
    register_admin()
        Register an admin at the start of the program
    """

    def register_admin(self):
        """
        This function creates an unique admin account and write the info of the admin account into users.txt.
        """
        admin = Admin()
        user_operation = UserOperation()

        # Generate unique id
        admin.user_id = user_operation.generate_unique_user_id()

        # Manually set the admin name and password
        admin.user_name = "admin_"
        password = "admin1"
        encrypted_password = user_operation.encrypt_password(password)
        admin.user_password = encrypted_password

        # Generate the time of the registration
        admin.user_register_time = time.strftime('%d-%m-%Y_%H:%M:%S')
        admin.user_role = "admin"

        while True:

            # Check if the username is unique
            result = user_operation.check_username_exist(admin.user_name)

            # If the username is not unique, randomly generate an username.
            if result:
                characters = string.ascii_letters + "_"
                length = random.randint(5, 10)
                user_name = ''.join(random.choice(characters) for _ in range(length))
                admin.user_name = user_name
            break

        # Write the info into the txt file
        with open("data/users.txt", "a", encoding="utf-8") as users_file:
            users_file.write(admin.__str__() + "\n")