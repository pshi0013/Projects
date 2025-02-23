"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 25th May 2023
Last Modified Date:
Description: This script includes the Admin class which inherits from the User class
"""

from model_user import User

class Admin(User):
    """
    A class used to represent the model of admins

    Attributes
    ----------
    user_id : str
        a string to store the admin's id
    user_name : str
        a string to store the admin's username
    user_password: str
        a string to store the admin's password
    user_register_time: str
        a string to store the admin's registered time
    user_role: str
        a string to store the admin's role
    """

    def __init__(self, user_id="u_0000000002", user_name="admin_", user_password="admin1", user_register_time="22-05-2023_00:00:00", user_role="admin"):
        """
        Parameters
        ----------
        user_id : str
            The ID of the user (default is "u_0000000002")
        user_name : str
            The name of the user (default is "admin_")
        user_password : str
            The password of the user (default is "admin1")
        user_register_time : str
            The registered time of the user (default is "22-05-2023_00:00:00")
        user_role : str
            The role of the user (default is "admin")
        """

        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        """
        Returns
        ----------
        A formatted string containing the admin's details
        """

        return f"{{'user_id': '{self.user_id}', 'user_name': '{self.user_name}', 'user_password': '{self.user_password}'," \
               f"'user_register_time': '{self.user_register_time}', 'user_role': '{self.user_role}'}}"
