"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 25th May 2023
Last Modified Date:
Description: This script includes the Order class.
"""

class Order:
    """
    A class used to represent the model of orders

    Attributes
    ----------
    order_id : str
        a string to store the order id
    user_id : str
        a string to store the customer id
    pro_id : str
        a string to store the product id
    order_time : str
        a string to store the order time
    """
    def __init__(self, order_id="o_12345", user_id="u_0000000001", pro_id="1671872", order_time="22-05-2023_00:00:00"):
        """
        Parameters
        ----------
        order_id : str
            The ID of the order (default is "o_12345")
        user_id : str
            The ID of the user (default is "u_0000000001")
        pro_id : str
            The ID of the product (default is "1671872")
        order_time : str
            The time of creating the order (default is ""22-05-2023_00:00:00")
        """

        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        """
        Returns
        ----------
        A formatted string containing the details of an order
        """

        return f"{{'order_id': '{self.order_id}', 'user_id': '{self.user_id}', \"pro_id\": \"{self.pro_id}\", 'order_time': '{self.order_time}'}}"
