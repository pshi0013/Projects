"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 25th May 2023
Last Modified Date:
Description: This script includes the Product class.
"""

class Product:
    """
    A class used to represent the model of products

    Attributes
    ----------
    prot_id : str
        a string to store the product id
    pro_model : str
        a string to store the model of the product
    pro_category : str
        a string to store the category of the product
    pro_name : str
        a string to store the name of the product
    pro_current_price : float
        a float to store the current price of the product
    pro_raw_price : float
        a float to store the raw price of the product
    pro_discount : int
        an integer to store the discount of the product
    pro_likes_count : int
        an integer to store the likes-count of the product
    """

    def __init__(self, pro_id="1671872", pro_model="SKUF08305", pro_category="accessories", pro_name="handbag",
                 pro_current_price=9.99, pro_raw_price=16.99, pro_discount=41, pro_likes_count=140):
        """
        Parameters
        ----------
        pro_id : str
            The ID of the product (default is "1671872")
        pro_model : str
            The model of the product (default is "SKUF08305")
        pro_category :
            The category of the user (default is "accessories")
        pro_name : str
            The name of the product (default is "handbag")
        pro_current_price : float
            The current price of the product (default is 9.99)
        pro_raw_price : float
            The raw price of the product (default is 16.99)
        pro_discount : int
            The discount of the product (default is 41)
        pro_likes_count : int
            The likes-count of the product (default is 140)
        """

        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        """
        Returns
        ----------
        A formatted string containing the details of a product
        """

        return f"{{\"pro_id\": \"{self.pro_id}\", \"pro_model\": \"{self.pro_model}\", \"pro_category\": \"{self.pro_category}\", " \
           f"\"pro_name\": \"{self.pro_name}\", \"pro_current_price\": \"{self.pro_current_price}\", " \
           f"\"pro_raw_price\": \"{self.pro_raw_price}\", \"pro_discount\": \"{self.pro_discount}\", " \
           f"\"pro_likes_count\": \"{self.pro_likes_count}\"}}"
