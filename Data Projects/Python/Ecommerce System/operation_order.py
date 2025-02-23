"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the OrderOperation class which implements the methods related to orders.
"""

import re
import time
import math
import random
import string
import matplotlib.pyplot as plt
from model_order import Order
from model_customer import Customer
from operation_user import UserOperation

class OrderOperation():
    """
        A class used to operate methods related to orders

        Methods
        -------
        generate_unique_order_id()
            Generate unique id for an order
        create an order()
            Create an order in the system
        delete_order()
            Delete the order from the system
        get_order_list()
            Retrieve order list from the system
        generate_test_order_data()
            Create test data for the program
        generate_single_customer_consumption_figure()
            Generate a graph showing the consumption of the customer in 12 different months
        generate_all_customer_consumption_figure()
            Generate a graph showing the consumption of all customersin 12 different months
        generate_all_top_10_best_sellers_figure
            Generate a graph showing the top 10 best-selling products in descending order.
        delete_all_orders()
                Delete all orders from the system
        """
    def generate_unique_order_id(self):
        """
        Generate an unique id for an order

        Returns
        ------
        An unique order id
        """

        while True:
            unique_id = random.randint(1, 99999)
            formatted_id = "{:05d}".format(unique_id)
            order_id = "o_" + str(formatted_id)

            # Search in the file to check whether the id has been used
            with open("data/orders.txt", "r", encoding='utf-8') as orders_file:
                orders = orders_file.read()
                if re.search(order_id, orders) is None:
                    return order_id

    def create_an_order(self, customer_id, product_id, create_time):
        """
        Create an order

        Parameters
        ----------
        customer_id: str
            the user_id of the customer
        product_id: str
            the pro_id of the product
        create_time: str
            the time of creating the order

        Returns
        ------
        True if the order is created successfully, false otherwise
        """

        # Generate an unique id for the order
        order_id = self.generate_unique_order_id()

        # If create time is not provided, use the current time
        if create_time is None:
            create_time = time.strftime('%d-%m-%Y_%H:%M:%S')

        # Create an order object
        order = Order(order_id, customer_id, product_id, create_time)

        # Write the order info into the file
        with open("data/orders.txt", "a", encoding='utf-8') as orders_file:
            orders_file.write(order.__str__()+"\n")

    def delete_order(self, order_id):
        """
        Delete the order in the system with the provided order id

        Parameters
        ----------
        order_id: str
            the order_id of the order

        Returns
        ------
        True if the order is deleted, otherwise False
        """

        # Check if the length of the order id is correct
        if not len(order_id) == 7:
            return False

        with open("data/orders.txt", "r", encoding='utf-8') as orders_file:
            orders = orders_file.readlines()
            orders = [order.rstrip('\n') for order in orders]

        updated_orders = []
        for order in orders:

            # If the order id does not exist in the order info, added the order in the updated_orders list.
            if re.search(order_id, order) is None:
                updated_orders.append(order)

        # If the number of orders in the file is more than the number of orders in the updated_products list,
        # the order is deleted.
        if len(orders) > len(updated_orders):
            with open("data/orders.txt", "w", encoding='utf-8') as orders_file:
                for order in updated_orders:
                    orders_file.write(order + "\n")
                return True
        else:
            return False

    def get_order_list(self, customer_id, page_number):
        """
        Retrieve order list from the system. One page includes a maximum of 10 orders.

        Parameters
        ----------
        customer_id: str
            the user_id of the customer
        page_number: int
            the page number of the order list

        Returns
        ------
        A tuple:
            including a list of order objects, the page number and the total number of pages.
        """

        order_list = []
        order_object_list = []
        with open("data/orders.txt", "r", encoding="utf-8") as orders_file:
            orders = orders_file.readlines()
            for i in range(len(orders)):

                # Search for the orders with the same customer_id
                if re.search(customer_id, orders[i]) is not None:
                    order_list.append(orders[i].strip("\n"))

            # If no customer_id is specified, return all orders
            if customer_id is None:
                order_list = orders

        # Calculate the total pages of the order list
        total_pages = math.ceil(len(order_list) / 10)

        # Calculate the start and end index of the order list in a page
        if page_number * 10 < len(order_list):
            start_ind = (page_number - 1) * 10
            end_ind = start_ind + 10
            order_list = order_list[start_ind:end_ind]

        # The last page may contain fewer than 10 orders
        elif page_number * 10 >= len(order_list):
            start_ind = (page_number - 1) * 10
            print(start_ind)
            end_ind = len(order_list)
            order_list = order_list[start_ind:end_ind]

        # Iterate the order_list to extract the information, and create order objects
        for order in order_list:
            pattern_1 = r"'order_id': '([^']*)'"
            match_1 = re.search(pattern_1, order)
            order_id = match_1.group(1)
            pattern_2 = r"'user_id': '([^']*)'"
            match_2 = re.search(pattern_2, order)
            user_id = match_2.group(1)
            pattern_3 = r"\"pro_id\": \"(\d+)\""
            match_3 = re.search(pattern_3, order)
            pro_id = match_3.group(1)
            pattern_4 = r"'order_time': '([^']*)'"
            match_4 = re.search(pattern_4, order)
            order_time = match_4.group(1)
            order = Order(order_id, user_id, pro_id, order_time)

            # Add the objects in the order_object_list
            order_object_list.append(order)
        return (order_object_list, page_number, total_pages)

    def generate_test_order_data(self):
        """
        Generate test order data for the system
        """

        # Create 10 customers
        customer_str = ""
        user_operation = UserOperation()
        for i in range(10):
            customer = Customer()
            customer.user_id = user_operation.generate_unique_user_id()

            # Create a customer whose username is "customer_" for testing
            customer.user_name = "customer_"

            # Check if the username has already existed
            while True:
                result = user_operation.check_username_exist(customer.user_name)
                if result:
                    characters = string.ascii_letters + "_"
                    length = random.randint(5, 10)
                    user_name = ''.join(random.choice(characters) for _ in range(length))
                    customer.user_name = user_name
                break

            # Set the password "customer1" for all created customers
            password = "customer1"
            encrypted_password = user_operation.encrypt_password(password)
            customer.user_password = encrypted_password

            # Create the register time
            year = 2022
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            customer.user_register_time = f"{day:02d}-{month:02d}-{year}_{hour:02d}:{minute:02d}:{second:02d}"

            customer.user_role = "customer"

            # Randomly create the emails
            username_length = random.randint(5, 10)
            domain_length = random.randint(5, 10)
            username = ''.join(random.choices(string.ascii_letters + string.digits + '_.+-', k = username_length))
            domain = ''.join(random.choices(string.ascii_letters + string.digits + '-', k = domain_length))
            extension = ''.join(random.choices(string.ascii_letters + string.digits + '-.', k = random.randint(2, 4)))
            customer.user_email = f"{username}@{domain}.{extension}"

            # Randomly create the mobiles
            code = random.choice(['04', '03'])
            digits = ''.join(random.choices('0123456789', k=8))
            customer.user_mobile = code + digits

            customer_str += customer.__str__()+"\n"

            # Write the customer info to the file
            with open("data/users.txt", "w", encoding="utf-8") as users_file:
                users_file.write(customer_str)

            # Randomly generate 50-200 orders for a customer
            num_of_orders = random.randint(50, 200)
            for j in range(num_of_orders):

                # Create the order time
                months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
                month = random.choice(months)
                day = random.randint(1, 28)
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                order_time = f"{day:02d}-{month}-{year}_{hour:02d}:{minute:02d}:{second:02d}"

                # Randomly choose product_id from the products file
                with open("data/products.txt", "r", encoding="utf-8") as products_file:
                    products = products_file.read()
                    pattern = r"\"pro_id\": \"(\d+)\""
                    product_list = re.findall(pattern, products)
                    product_id = random.choice(product_list)

                    # Create an order
                    self.create_an_order(customer.user_id, product_id, order_time)

    def generate_single_customer_consumption_figure(self, customer_id):
        """
        Generate a bar chart displaying the customer's consumption in 12 different months

        Parameters
        ----------
        customer_id: str
            the user_id of the customer
        """

        product_month = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0}
        with open("data/orders.txt", "r", encoding="utf-8") as orders_file:
            orders = orders_file.readlines()

            # Iterate through all orders
            for order in orders:

                # Search for the same customer_id
                if customer_id in order:

                    # Collect the order time (month) and the pro_id
                    pattern_1 = r"'order_time': '\d{2}-(\d{2})-\d{4}_\d{2}:\d{2}:\d{2}'"
                    pattern_2 = r"\"pro_id\": \"(\d+)\""
                    match_1 = re.search(pattern_1, order)
                    match_2 = re.search(pattern_2, order)
                    if match_1 is not None:
                        month = match_1.group(1)
                    if match_2 is not None:
                        pro_id = match_2.group(1)

                    # Search the current price of the product from the products file
                    with open("data/products.txt", "r", encoding="utf-8") as products_file:
                        products = products_file.readlines()
                        for product in products:
                            if pro_id in product:
                                pattern_3 = r"\"pro_current_price\": \"([^\"]*)\""
                                match_3 = re.search(pattern_3, product)
                                if match_3 is not None:
                                    price = match_3.group(1)
                                    price = float(price)

                                    # Add the price into the dictionary under the order month
                                    if month in product_month:
                                        product_month[month] += price
                                    else:
                                        product_month[month] = price

        product_month = {month: round(float(price), 2) for month, price in product_month.items()}
        # sorted_product_month = dict(sorted(product_month.items(), key=lambda item: item[0]))

        # Create the bar chart
        months = list(product_month.keys())
        price = list(product_month.values())
        plt.bar(months, price)
        plt.xlabel('Month')
        plt.ylabel('Consumption')
        plt.title('The Consumption in 12 Months')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylim(0)

        # Save the chart into the folder
        plt.savefig("data/figure/generate_single_customer_consumption_figure.png")
        plt.close()

    def generate_all_customers_consumption_figure(self):
        """
        Generate a bar chart displaying all customer's consumption in 12 different months
        """
        month_consumption = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0, "12": 0}
        with open("data/orders.txt", "r", encoding="utf-8") as orders_file:
            orders = orders_file.readlines()
            for order in orders:

                # Collect the order time (month) and the pro_id
                pattern_1 = r"'order_time': '\d{2}-(\d{2})-\d{4}_\d{2}:\d{2}:\d{2}'"
                pattern_2 = r"\"pro_id\": \"(\d+)\""
                match_1 = re.search(pattern_1, order)
                match_2 = re.search(pattern_2, order)
                if match_1 is not None:
                    month = match_1.group(1)
                if match_2 is not None:
                    pro_id = match_2.group(1)
                with open("data/products.txt", "r", encoding="utf-8") as products_file:
                    products = products_file.readlines()
                    for product in products:

                        # Search for the current price of the same product
                        if pro_id in product:
                            pattern_3 = r"\"pro_current_price\": \"([^\"]*)\""
                            match_3 = re.search(pattern_3, product)
                            price = float(match_3.group(1))

                            if month in month_consumption:
                                month_consumption[month] += price
                            else:
                                month_consumption[month] = price


        month_consumption = {month: round(price, 2) for month, price in month_consumption.items()}
        #sorted_month_consumption = dict(sorted(month_consumption.items(), key=lambda item: item[0]))

        # Create the bar chart
        months = list(month_consumption.keys())
        price = list(month_consumption.values())
        plt.bar(months, price)
        plt.xlabel('Month')
        plt.ylabel('Consumption')
        plt.title('The Consumption in 12 Months')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylim(0)

        # Save the chart into the folder
        plt.savefig("data/figure/generate_all_customers_consumption_figure.png")
        plt.close()

    def generate_all_top_10_best_sellers_figure(self):
        """
        Generate a bar chart displaying the top 10 best-selling products in descending order.
        """

        product_counts = {}
        with open("data/orders.txt", "r", encoding="utf-8") as orders_file:
            orders = orders_file.readlines()
            for order in orders:

                # Search for the pro_id in the order
                pattern = r"\"pro_id\": \"(\d+)\""
                matches = re.findall(pattern, order)
                for match in matches:
                    product_id = match

                    # Collect the product_id and the number of consumption into a dictionary
                    if product_id in product_counts:
                        product_counts[product_id] += 1
                    else:
                        product_counts[product_id] = 1

        # Sort the dictionary by the values in descending order
        sorted_product_counts = dict(sorted(product_counts.items(), key=lambda item: item[1], reverse=True)[:10])

        # Create the bar chart
        product = list(sorted_product_counts.keys())
        order_num = list(sorted_product_counts.values())
        plt.bar(product, order_num, linewidth=1.5)
        plt.xlabel('Product ID')
        plt.ylabel('Total Number of Orders')
        plt.title('Top Ten Best Sellers')
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=8)
        plt.ylim(0)
        plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

        # Save the chart into the folder
        plt.savefig("data/figure/generate_all_top_10_best_sellers_figure.png")
        plt.close()

    def delete_all_orders(self):
        """
        Delete all orders from the system
        """
        with open("data/orders.txt", "w", encoding='utf-8') as orders_file:
            orders_file.write("")