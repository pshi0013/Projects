"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the UserOperation class which implements the methods related to users.
"""

import re
import random
import string
from model_admin import Admin
from model_customer import Customer

class UserOperation():
    """
    A class used to operate methods related to users

    Methods
    -------
    generate_unique_user_id()
        Generate an unique user id
    encrypt_password()
        Encrypt the user's password
    decrypt_password()
        Decrypt the user's password
    check_username_exist()
        Check if the username has been used
    validate_username()
        Check if the username is valid
    validate_password()
        Check if the password is valid
    login()
        Login the user to the system
    """

    def generate_unique_user_id(self):
        """
        Generate and return a 10-digit unique user id starting with ‘u_’.

        Returns
        -------
        an unique user id
        """

        while True:
            new_user_id = 'u_' + ''.join(random.choices(string.digits, k=10))

            # Check if the user id has been used from the users.txt file
            with open("data/users.txt", "r", encoding='utf-8') as users_file:
                users = users_file.read()
                pattern = "'user_id': " + new_user_id
                if re.search(pattern, users) is None:
                    return new_user_id

    def encrypt_password(self, user_password):
        """
        Encrypt the user's password.

        Parameters
        ----------
        user_password: str
            the password provided by the user

        Returns
        -------
        an encrypted password
        """

        # Generate a random string whose length is equal to two times of the length of the user_password
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=2 * len(user_password)))
        encrypted_password = '^^'
        for i in range(len(user_password)):
            encrypted_password += random_string[2 * i : 2 * i + 2] + user_password[i]
        encrypted_password += '$$'
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        """
        Decrypt the user's encrypted password.

        Parameters
        ----------
        encrypted_password: str
            the password which has been encrypted

        Returns
        -------
        an user-provided password

        """

        decrypted_password = ''

        # Iterate through the encrypted password and extract characters
        for i in range(4, len(encrypted_password) - 2, 3):
            decrypted_password += encrypted_password[i]
        return decrypted_password

    def check_username_exist(self, user_name):
        """
        Check whether the username has already been registered in the system.

        Parameters
        ----------
        user_name: str
            the user's username

        Returns
        -------
        True if the username already existed in the system.
        False if the username does not exist in the system.
        """

        with open("data/users.txt", "r", encoding='utf-8') as users_file:
            users = users_file.readlines()
            pattern = r"'user_name': '([^']*)'"

            # Iterate through the user list in the file to check if there is the same username
            for user in users:
                match = re.search(pattern, user)
                if user_name == match.group(1):
                    return True
            return False

    def validate_username(self, user_name):
        """
        Verify whether the user's name only contain letters or underscores, and at least 5 characters.

        Parameters
        ----------
        user_name: str
            the user's username

        Returns
        -------
        True if the username is valid.
        False if the username is invalid.
        """

        pattern = r'^[a-zA-Z_]{5,}$'

        # Check if the username matches the pattern
        if re.search(pattern, user_name) is not None:
            return True
        else:
            return False

    def validate_password(self, user_password):
        """
        Verify whether the user's password contains at least one (uppercased or lowercased) and one number.
        The length of the password should be at least 5 characters.

        Parameters
        ----------
        user_password: str
            the user's password

        Returns
        -------
        True if the user's password is valid.
        False if the user's password is invalid.
        """

        pattern = r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{5,}$'

        # Check if the password matches the pattern
        if re.search(pattern, user_password) is not None:
            return True
        else:
            return False

    def login(self, user_name, user_password):
        """
        Authorise the user's username and password and login the user into the system

        Parameters
        ----------
        user_name: str
            the username
        user_password: str
            the user's password

        Returns
        -------
        A Customer object or an Admin object
        """

        # Search for the username in the users.txt file
        with open("data/users.txt", "r", encoding='utf-8') as users_file:
            users = users_file.readlines()
            for user in users:
                pattern = r"'user_name': '" + user_name + "'"

                # The username is found and verify if the password matches
                if re.search(pattern, user) is not None:
                    pattern_1 = r"'user_password': '(\^\^[A-Za-z0-9]+\$+)\'"
                    match = re.search(pattern_1, user)
                    if match is not None:
                        encrypted_password = match.group(1)

                        # Decrypt the password stored in the file
                        decrypted_password = self.decrypt_password(encrypted_password)

                        # The password in the file matches the user_password; check the user role is admin or customer.
                        if decrypted_password == user_password:
                            if re.search("'user_role': 'admin'", user) is not None:
                                admin = Admin()
                                return admin
                            elif re.search("'user_role': 'customer'", user) is not None:
                                pattern_1 = r"'user_id': '([^']*)'"
                                match_1 = re.search(pattern_1, user)
                                user_id = match_1.group(1)
                                pattern_2 = r"'user_name': '([^']*)'"
                                match_2 = re.search(pattern_2, user)
                                user_name = match_2.group(1)
                                pattern_3 = r"'user_password': '([^']*)'"
                                match_3 = re.search(pattern_3, user)
                                user_password = match_3.group(1)
                                pattern_4 = r"'user_register_time': '([^']*)'"
                                match_4 = re.search(pattern_4, user)
                                user_register_time = match_4.group(1)
                                pattern_5 = r"'user_email': '([^']*)'"
                                match_5 = re.search(pattern_5, user)
                                user_email = match_5.group(1)
                                pattern_6 = r"'user_mobile': '([^']*)'"
                                match_6 = re.search(pattern_6, user)
                                user_mobile = match_6.group(1)
                                customer = Customer(user_id, user_name, user_password, user_register_time, "customer",
                                                    user_email, user_mobile)
                                return customer