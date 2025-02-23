"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 25th May 2023
Last Modified Date:
Description: This script includes the Customer class which inherits from the User class.
"""

from model_user import User

class Customer(User):
    """
    A class used to represent the model of customers

    Attributes
    ----------
    user_id : str
        a string to store the customer's id
    user_name : str
        a string to store the customer's username
    user_password : str
        a string to store the customer's password
    user_register_time: str
        a string to store the customer's registered time
    user_role : str
        a string to store the customer's role
    user_email : str
        a string to store the customer's email
    user_mobile : str
        a string to store the customer's mobile
    """

    def __init__(self, user_id="u_0000000003", user_name="customer_", user_password="customer", user_register_time="22-05-2023_00:00:00",
                 user_role="customer", user_email="aa00@gamil.com", user_mobile="0412345678"):
        """
        Parameters
        ----------
        user_id : str
            The ID of the user (default is "u_0000000003")
        user_name : str
            The name of the user (default is "customer_")
        user_password : str
            The password of the user (default is "customer")
        user_register_time : str
            The registered time of the user (default is "22-05-2023_00:00:00")
        user_role : str
            The role of the user (default is "customer")
        user_email : str
            The user's email (default is "aa00@gamil.com")
        user_mobile : str
            The user's mobile (default is "0412345678")
        """

        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        """
        Returns
        ----------
        A formatted string containing the customer's details
        """

        return f"{{'user_id': '{self.user_id}', 'user_name': '{self.user_name}', 'user_password': '{self.user_password}'," \
               f"'user_register_time': '{self.user_register_time}', 'user_role': '{self.user_role}', " \
               f"'user_email': '{self.user_email}', 'user_mobile': '{self.user_mobile}'}}"