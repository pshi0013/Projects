"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the IOInterface class which implements the I/O of the program.
"""

import pandas as pd

class IOInterface:
    """
    A class used to operate I/O of the program.

    Methods
    -------
    get_user_input()
        Accept the inputs from the user
    main_menu()
        Display the login menu
    admin_menu()
        Display the admin menu
    customer_menu()
        Display the customer menu
    show_list()
        Display the lists required by the users
    print_error_message()
        Display a message when an error occurs and show the error source
    print_message()
        Display a message
    print_object()
        Display an object
    """

    def get_user_input(self, message, num_of_args):
        """
        Accept user's inputs

        Parameters
        ----------
        message: str
            the message to prompt user's input
        num_of_args: int
            the number of arguments required for the user's input

        Returns
        ------
         A list containing all users inputs
        """
        user_input = input(message).split()
        args_list = user_input[:num_of_args]

        # If the user doesn't input for the argument, it will return an empty string.
        args_list += (num_of_args - len(args_list)) * [""]
        return args_list

    def main_menu(self):
        """
            Display main menu
        """

        print("\n Main menu:")
        print("--------------")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

    def admin_menu(self):
        """
            Display admin menu
        """

        print("\n Admin menu:")
        print("----------------")
        print("1.  Show products")
        print("2.  Add customers (You should input “2 username password email mobile”)")
        print("3.  Show customers")
        print("4.  Show orders")
        print("5.  Generate test data")
        print("6.  Generate statistical figures")
        print("7.  Delete all data")
        print("8.  Delete customer with customer ID")
        print("9.  Delete order with order ID")
        print("10. Delete product with product ID")
        print("11. Delete all products")
        print("12. Delete all orders")
        print("13. Logout")

    def customer_menu(self):
        """
            Display customer menu
        """

        print("\n Customer menu:")
        print("------------------")
        print("1. Show profile")
        print("2. Update profile")
        print("3. Show products")
        print("4. Show history orders")
        print("5. Generate all consumption figures")
        print("6. Get product with product id")
        print("7. Logout")


    def show_list(self, user_role, list_type, object_list):
        """
        Print out the lists for the user

        Parameters
        ----------
        user_role: str
            the role of the user
        list_type: str
            the type of the list
        object_list:
            the list of objects
        """

        if user_role == "admin" and list_type == "customer":

            # Format the information of the objects
            customer_data = "ID, Name, Password, Register time, Role, Email, Mobile\n"
            for customer in object_list[0]:
                customer_data += f"\"{customer.user_id}\",\"{customer.user_name}\",\"{customer.user_password}\"" \
                                 f",\"{customer.user_register_time}\", \"{customer.user_role}\", \"{customer.user_email}\", \"{customer.user_mobile}\"\n"

            # Write the information into the csv file and print out the dataframe
            with open("data/customers_list.csv", "w") as customers_list:
                customers_list.write(customer_data)

            df = pd.read_csv("data/customers_list.csv").iloc[:,:]
            df.index = [i + 1 for i in df.index]
            print(df.to_string(justify="left"))
            print("page number: " + str(object_list[1]))
            print("total page number: " + str(object_list[2]) + "\n")

        elif list_type == "order":

            # Format the information of the objects
            order_data = "Order ID, User ID, Product ID, Order time\n"
            for order in object_list[0]:
                order_data += f"\"{order.order_id}\",\"{order.user_id}\",\"{order.pro_id}\",\"{order.order_time}\"\n"

            # Write the information into the csv file and print out the dataframe
            with open("data/orders_list.csv", "w") as orders_list:
                orders_list.write(order_data)

            df = pd.read_csv("data/orders_list.csv").iloc[:,:]
            df.index = [i + 1 for i in df.index]
            print(df.to_string(justify="left"))
            print("page number: " + str(object_list[1]))
            print("total page number: " + str(object_list[2]) + "\n")

        elif user_role == "admin" and list_type == "product":

            # Format the information of the objects
            product_data = "Product ID, Model, Category, Name, Current price, Raw price, Discount, Likes-count\n"
            for product in object_list[0]:
                product_data += f"\"{product.pro_id}\",\"{product.pro_model}\",\"{product.pro_category}\",\"{product.pro_name}.\"," \
                              f"\"{product.pro_current_price}\",\"{product.pro_raw_price}\",\"{product.pro_discount}\"," \
                              f"\"{product.pro_likes_count}\"\n"

            # Write the information into the csv file and print out the dataframe
            with open("data/products_list.csv", "w") as products_list:
                products_list.write(product_data)

            df = pd.read_csv("data/products_list.csv").iloc[:,:]
            df.index = [i + 1 for i in df.index]
            print(df.to_string(justify="left"))
            print("page number: " + str(object_list[1]))
            print("total page number: " + str(object_list[2]) + "\n")

        elif user_role == "customer" and list_type == "product":

            # Format the information of the objects
            product_data = "Product ID, Model, Category, Name, Current price, Raw price, Discount, Likes-count\n"
            for product in object_list:
                product_data += f"\"{product.pro_id}\",\"{product.pro_model}\",\"{product.pro_category}\",\"{product.pro_name}\"," \
                                f"\"{product.pro_current_price}\",\"{product.pro_raw_price}\",\"{product.pro_discount}\"," \
                                f"\"{product.pro_likes_count}\"\n"

            # Write the information into the csv file and print out the dataframe
            with open("data/products_list.csv", "w") as products_list:
                products_list.write(product_data)

            df = pd.read_csv("data/products_list.csv").iloc[:,:]
            df.index = [i + 1 for i in df.index]
            print(df.to_string(justify="left"))

    def print_error_message(self, error_source, error_message):
        """
        Print out the error message

        Parameters
        ----------
        error_source: str
            the source of the error
        error_message: str
            the error message
        """
        print("\nError:")
        print(f"Source: {error_source}")
        print(f"Message: {error_message}\n")

    def print_message(self, message):
        """
        Print out the error message

        Parameters
        ----------
        message: str
            the message to print out
        """

        print(message)

    def print_object(self, target_object):
        """
        Print out the information of the object

        Parameters
        ----------
        target_object: Object
        """

        print(target_object.__str__())