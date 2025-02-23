"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 25th May 2023
Last Modified Date:
Description: This script includes the User class.
"""

class User:
    """
    A class used to represent the model of users

    Attributes
    ----------
    user_id : str
        a string to store the user's id
    user_name : str
        a string to store the username
    user_password : str
        a string to store the user's password
    user_register_time : str
        a string to store the user's registered time
    user_role : str
        a string to store the user's role
    """

    def __init__(self, user_id="u_0000000001", user_name="user__", user_password="user01", user_register_time="22-05-2023_00:00:00", user_role="user"):
        """
        Parameters
        ----------
        user_id : str
            The ID of the user (default is "u_0000000001")
        user_name : str
            The name of the user (default is "user__")
        user_password : str
            The password of the user (default is "user01")
        user_register_time : str
            The registered time of the user (default is "22-05-2023_00:00:00")
        user_role : str
            The role of the user (default is "user")
        """

        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):
        """
        Returns
        ----------
        A formatted string containing the user's details
        """

        return f"{{'user_id': '{self.user_id}', 'user_name': '{self.user_name}', 'user_password': '{self.user_password}', 'user_register_time': '{self.user_register_time}', 'user_role': '{self.user_role}'}}"