"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the CustomerOperation class which implements the methods related to customers.
"""

import re
import math
import time
from model_customer import Customer
from operation_user import UserOperation

class CustomerOperation():
    """
    A class used to operate methods related to customers

    Methods
    -------
    validate_email()
        Check whether the email is valid
    validate_mobile()
        Check whether the mobile is valid
    register_customer()
        Register a customer into the system
    update_profile()
        Update the user's profile
    delete_customer()
        Delete a customer from the system
    get_customer_list()
        Retrieve customer list from the system
    delete all customer()
        Delete all customers from the system
    """

    def validate_email(self, user_email):
        """
        Check whether the email address consists of username, "@", domain name, and Dot(.)

        Parameters
        ----------
        user_email: str
            the email provided by the user

        Returns
        -------
        True if the email is valid
        False if the email is invalid
        """

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        # Check if the email matches the pattern
        if re.search(pattern, user_email):
            return True
        else:
            return False

    def validate_mobile(self, user_mobile):
        """
        Check whether the mobile contains exactly 10 digit and only consists of numbers.
        The number should start with '04' or '03'.

        Parameters
        ----------
        user_mobile: str
            the moblile provided by the user

        Returns
        -------
        True if the mobile is valid
        False if the mobile is invalid
        """

        pattern = '^(04|03)\d{8}$'

        # Check if the mobile matches the pattern
        if re.search(pattern, user_mobile):
            return True
        else:
            return False

    def register_customer(self, user_name, user_password, user_email, user_mobile):
        """
        Validate the provided customer info and register the customer into the system.

        Parameters
        ----------
        user_name: str
            the provided username
        user_password: str
            the provided user password
        user_email: str
            the provided user email
        user_mobile: str
            the provided user mobile

        Returns
        -------
        True if registration is successful, otherwise False
        """

        user_operation = UserOperation()

        # Validate the username
        if not user_operation.validate_username(user_name):
            return False

        # Check whether the username exists
        if user_operation.check_username_exist(user_name):
            return False

        # Validate the password
        if not user_operation.validate_password(user_password):
            return False

        # Validate the email
        if not self.validate_email(user_email):
            return False

        # Validate the mobile
        if not self.validate_mobile(user_mobile):
            return False

        # Generate the unique id for the new user
        user_id = user_operation.generate_unique_user_id()

        # Encrypt the valid password
        encrypted_password = user_operation.encrypt_password(user_password)

        # Generate the register time
        reg_time = time.localtime()
        user_register_time = time.strftime("%m-%d-%Y_%H:%M:%S", reg_time)

        # create a customer and write the info into the txt. file
        customer = Customer(user_id, user_name, encrypted_password, user_register_time, "customer", user_email, user_mobile)
        with open("data/users.txt", "a") as users_file:
            users_file.write(customer.__str__() + "\n")
            return True

    def update_profile(self, attribute_name, value, customer_object):
        """
        Update the customer's stored information in the system.

        Parameters
        ----------
        attribute_name: str
            the attribute that the customer wants to update
        value: str
            the value that the customer wants to update
        customer_object: Customer()
            the customer who wants to update the info

        Returns
        -------
        True if the update is successful, otherwise False
        """

        user_operation = UserOperation()

        # Validate the value of username
        if attribute_name.lower() == "name":
            if not user_operation.validate_username(value):
                return False
            if user_operation.check_username_exist(value):
                return False
            else:
                customer_object.user_name = value

        # Validate the value of password
        elif attribute_name.lower() == "password":
            if not user_operation.validate_password(value):
                return False
            else:
                # If the password is valid, encrypt the password.
                encrypted_password = user_operation.encrypt_password(value)
                customer_object.user_password = encrypted_password

        # Validate the value of email
        elif attribute_name.lower() == "email":
            if not self.validate_email(value):
                return False
            else:
                customer_object.user_email = value

        # Validate the value of mobile
        elif attribute_name.lower() == "mobile":
            if not self.validate_mobile(value):
                return False
            else:
                customer_object.user_mobile = value

        # Update the information in the system
        with open("data/users.txt", "r+", encoding='utf-8') as users_file:
            users = users_file.readlines()
            for i in range(len(users)):
                if customer_object.user_id in users[i]:
                    users.pop(i)
                    users.append(customer_object.__str__() + "\n")
                    users_file.seek(0)
                    users_file.writelines(users)
                    users_file.truncate()
                    return True

    def delete_customer(self, customer_id):
        """
        Delete the customer in the system with the provided customer_id

        Parameters
        ----------
        customer_id: str
            the user_id of the customer

        Returns
        ------
        True if the customer is deleted, otherwise False
        """

        # Check if the length of the provided customer id is valid
        if not len(customer_id) == 12:
            return False

        with open("data/users.txt", "r", encoding='utf-8') as users_file:
            users = users_file.readlines()
            users = [user.rstrip('\n') for user in users]

        updated_users = []
        for user in users:

            # If the user_role is admin, the account will not be deleted.
            if re.search("admin", user) is not None:
                updated_users.append(user)
            else:
                # If the user_role is customer and the user_id is not the provided customer_id, the account will not be deleted.
                if re.search(customer_id, user) is None:
                    updated_users.append(user)

        # If the number of users in the file is more than the number of users in the updated user list, the user is deleted.
        if len(users) > len(updated_users):
            # Write the new data into the file
            with open("data/users.txt", "w", encoding='utf-8') as users_file:
                for user in updated_users:
                    users_file.write(user + "\n")
                return True
        else:
            return False

    def get_customer_list(self, page_number):
        """
        Retrieve customer list from the system. One page includes a maximum of 10 customers.

        Parameters
        ----------
        page_number: int
            the page number of the customer list

        Returns
        ------
        A tuple:
            including a list of customer objects, the page number and the total number of pages.
        """

        customer_list = []
        customer_object_list = []

        # Search the customers in the file and put the info in the customer_list
        with open("data/users.txt", "r", encoding='utf-8') as users_file:
            users = users_file.readlines()
            users = [user.rstrip('\n') for user in users]
            for user in users:
                if re.search("customer", user) is not None:
                    customer_list.append(user)

            # Calculate the total pages of the customer list
            total_pages = math.ceil(len(customer_list) / 10)

            # Calculate the start and end index of the customer list in a page
            if page_number * 10 < len(customer_list):
                start_ind = (page_number - 1) * 10
                end_ind = start_ind + 10
                customer_list = customer_list[start_ind:end_ind]

            # The last page may contain fewer than 10 customers
            elif page_number * 10 >= len(customer_list):
                start_ind = (page_number - 1) * 10
                end_ind = len(customer_list)
                customer_list = customer_list[start_ind:end_ind]

            # Iterate the customer list to extract the information, and create the customer objects
            for customer in customer_list:
                pattern_1 = r"'user_id': '([^']*)'"
                match_1 = re.search(pattern_1, customer)
                user_id = match_1.group(1)
                pattern_2 = r"'user_name': '([^']*)'"
                match_2 = re.search(pattern_2, customer)
                user_name = match_2.group(1)
                pattern_3 = r"'user_password': '([^']*)'"
                match_3 = re.search(pattern_3, customer)
                user_password = match_3.group(1)
                pattern_4 = r"'user_register_time': '([^']*)'"
                match_4 = re.search(pattern_4, customer)
                user_register_time = match_4.group(1)
                pattern_5 = r"'user_email': '([^']*)'"
                match_5 = re.search(pattern_5, customer)
                user_email = match_5.group(1)
                pattern_6 = r"'user_mobile': '([^']*)'"
                match_6 = re.search(pattern_6, customer)
                user_mobile = match_6.group(1)
                customer = Customer(user_id, user_name, user_password, user_register_time, "customer", user_email, user_mobile)

                # Put the objects into customer_object_list
                customer_object_list.append(customer)
            return (customer_object_list, page_number, total_pages)

    def delete_all_customers(self):
        """
        Delete all customers from the system
        """

        admins = []
        with open("data/users.txt", "r+", encoding='utf-8') as users_file:
            users = users_file.readlines()
            users = [user.rstrip('\n') for user in users]
            for user in users:

                # Search for the admins in the users txt
                if re.search("admin", user) is not None:
                    admins.append(user)

        # Only write the admin information into the file
        with open("data/users.txt", "w", encoding='utf-8') as users_file:
            for admin in admins:
                users_file.write(admin + "\n")
