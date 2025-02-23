"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the ProductOperation class which implements the methods related to products.
"""

import re
import math
import pandas as pd
import matplotlib.pyplot as plt
from model_product import Product

class ProductOperation():
    """
    A class used to operate methods related to products

    Methods
    -------
    extract_products_from_files()
        Extract product information from the data files
    get_product_list()
        Retrieve product list from the system
    delete_product()
        Delete the product from the system
    get_product_list_by_keyword()
        Retrieve the products whose product name includes the keyword
    get_product_by_id()
        Retrieve the product by product id
    generate_category_figure()
        Generate a figure showing the total number of products in each category
    generate_discount_figure()
        Generate a figure showing the proportion of products with different discounts
    generate_likes_count_figure()
        Generate a figure showing the likes-count of products in each category
    generate_discount_likes_count_figure()
        Generate a figure showing the relationship between likes_count and discount for all products.
    delete_all_products()
            Delete all products from the system
    """

    def extract_products_from_files(self):
        """
        Extract the product information from the provided csv files.
        """

        df = pd.read_csv("data/product/accessories.csv")
        df = df.loc[:,['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]

        # Convert each row into a dictionary
        accessories_dict = df.to_dict("records")
        acc_str = ""
        for dict in accessories_dict:
            acc_value_list = list(dict.values())

            # Create product objects with the value extracted from the dictionary
            product = Product(acc_value_list[0], acc_value_list[1], acc_value_list[2], acc_value_list[3],
                              acc_value_list[4], acc_value_list[5], acc_value_list[6], acc_value_list[7])

            # Formate the product informtaion
            acc_str += (product.__str__()+"\n")

        df = pd.read_csv("data/product/bags.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        bags_dict = df.to_dict("records")
        bags_str = ""
        for dict in bags_dict:
            bags_value_list = list(dict.values())
            product = Product(bags_value_list[0], bags_value_list[1], bags_value_list[2], bags_value_list[3],
                              bags_value_list[4], bags_value_list[5], bags_value_list[6], bags_value_list[7])
            bags_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/beauty.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        beauty_dict = df.to_dict("records")
        beauty_str = ""
        for dict in beauty_dict:
            beauty_value_list = list(dict.values())
            product = Product(beauty_value_list[0], beauty_value_list[1], beauty_value_list[2], beauty_value_list[3],
                              beauty_value_list[4], beauty_value_list[5], beauty_value_list[6], beauty_value_list[7])
            beauty_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/house.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        house_dict = df.to_dict("records")
        house_str = ""
        for dict in house_dict:
            house_value_list = list(dict.values())
            product = Product(house_value_list[0], house_value_list[1], house_value_list[2], house_value_list[3],
                              house_value_list[4], house_value_list[5], house_value_list[6], house_value_list[7])
            house_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/jewelry.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        jewelry_dict = df.to_dict("records")
        jewelry_str = ""
        for dict in jewelry_dict:
            jewelry_value_list = list(dict.values())
            product = Product(jewelry_value_list[0], jewelry_value_list[1], jewelry_value_list[2], jewelry_value_list[3],
                              jewelry_value_list[4], jewelry_value_list[5], jewelry_value_list[6], jewelry_value_list[7])
            jewelry_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/kids.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        kids_dict = df.to_dict("records")
        kids_str = ""
        for dict in kids_dict:
            kids_value_list = list(dict.values())
            product = Product(kids_value_list[0], kids_value_list[1], kids_value_list[2], kids_value_list[3],
                            kids_value_list[4], kids_value_list[5], kids_value_list[6], kids_value_list[7])
            kids_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/men.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        men_dict = df.to_dict("records")
        men_str = ""
        for dict in men_dict:
            men_value_list = list(dict.values())
            product = Product(men_value_list[0], men_value_list[1], men_value_list[2], men_value_list[3],
                              men_value_list[4], men_value_list[5], men_value_list[6], men_value_list[7])
            men_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/shoes.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        shoes_dict = df.to_dict("records")
        shoes_str = ""
        for dict in shoes_dict:
            shoes_value_list = list(dict.values())
            product = Product(shoes_value_list[0], shoes_value_list[1], shoes_value_list[2], shoes_value_list[3],
                              shoes_value_list[4], shoes_value_list[5], shoes_value_list[6], shoes_value_list[7])
            shoes_str += (product.__str__() + "\n")

        df = pd.read_csv("data/product/women.csv")
        df = df.loc[:, ['id', 'model', 'category', 'name', 'current_price', 'raw_price', 'discount', 'likes_count']]
        women_dict = df.to_dict("records")
        women_str = ""
        for dict in women_dict:
            women_value_list = list(dict.values())
            product = Product(women_value_list[0], women_value_list[1], women_value_list[2], women_value_list[3],
                              women_value_list[4], women_value_list[5], women_value_list[6], women_value_list[7])
            women_str += (product.__str__() + "\n")

        # Write all product information in the txt file
        with open("data/products.txt", "w", encoding='utf-8') as products_file:
            products_file.write(acc_str + bags_str + beauty_str + house_str + jewelry_str + kids_str + men_str + shoes_str + women_str)

    def get_product_list(self, page_number):
        """
        Retrieve product list from the system. One page includes a maximum of 10 products.

        Parameters
        ----------
        page_number: int
            the page number of the customer list

        Returns
        ------
        A tuple:
            including a list of product objects, the page number and the total number of pages.
        """

        product_object_list = []

        # Search the products in the file and put the info in the product_list
        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.readlines()
            products = [product.rstrip('\n') for product in products]

            # Calculate the total pages of the product list
            total_pages = math.ceil(len(products) / 10)

            # Calculate the start and end index of the product list in a page
            if page_number * 10 < len(products):
                start_ind = (page_number - 1) * 10
                end_ind = start_ind + 10
                product_list = products[start_ind:end_ind]

            # The last page may contain fewer than 10 products
            elif page_number * 10 >= len(products):
                start_ind = (page_number - 1) * 10
                end_ind = len(products)
                product_list = products[start_ind:end_ind]

            # Iterate the products to extract the information, and create product objects
            for product in product_list:
                pattern_1 = r"\"pro_id\": \"(\d+)\""
                match_1 = re.search(pattern_1, product)
                pro_id = match_1.group(1)
                pattern_2 = r"\"pro_model\": \"([^\"]*)\""
                match_2 = re.search(pattern_2, product)
                pro_model = match_2.group(1)
                pattern_3 = r"\"pro_category\": \"([^\"]*)\""
                match_3 = re.search(pattern_3, product)
                pro_category = match_3.group(1)
                pattern_4 = r"\"pro_name\": \"([^\"]*)\""
                match_4 = re.search(pattern_4, product)
                pro_name = match_4.group(1)
                pattern_5 = r"\"pro_current_price\": \"([^\"]*)\""
                match_5 = re.search(pattern_5, product)
                pro_current_price = match_5.group(1)
                pattern_6 =  r"\"pro_raw_price\": \"([^\"]*)\""
                match_6 = re.search(pattern_6, product)
                pro_raw_price = match_6.group(1)
                pattern_7 = r"\"pro_discount\": \"([^\"]*)\""
                match_7 = re.search(pattern_7, product)
                pro_discount = match_7.group(1)
                pattern_8 = r"\"pro_likes_count\": \"([^\"]*)\""
                match_8 = re.search(pattern_8, product)
                pro_likes_count = match_8.group(1)
                product = Product(pro_id, pro_model, pro_category, pro_name, float(pro_current_price), float(pro_raw_price),
                                  int(pro_discount), int(pro_likes_count))

                # Put the objects into product_object_list
                product_object_list.append(product)
            return (product_object_list, page_number, total_pages)

    def delete_product(self, product_id):
        """
        Delete the product in the system with the provided product id

        Parameters
        ----------
        product_id: str
            the pro_id of the product

        Returns
        ------
        True if the product is deleted, otherwise False
        """

        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.readlines()
            products = [product.rstrip('\n') for product in products]

        updated_products = []
        for product in products:

            # If the product stored in the file does not contain the product_id,
            # the product is put in the updated_products list
            if re.search(product_id, product) is None:
                updated_products.append(product)

        # If the number of products in the file is more than the number of products in the updated_products list,
        # the product is deleted.
        if len(products) > len(updated_products):

            # Write the updated information in the file.
            with open("data/products.txt", "w", encoding='utf-8') as products_file:
                for product in updated_products:
                    products_file.write(product + "\n")
                return True
        else:
            return False

    def get_product_list_by_keyword(self, keyword):
        """
        Retrieve the products whose product name includes the keyword. The keyword is case insensitive,

        Parameters
        ----------
        keyword: str
            the keyword provided

        Returns
        ------
        A list of product objects.
        """

        product_list = []
        product_object_list = []
        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.readlines()
            for i in range(len(products)):

                # Convert the keyword and the product info in the file into uppercase characters.
                pattern = keyword.upper()
                search_string = products[i].strip("\n").upper()

                # If the keyword appears in the product info, the product is put into the list.
                if re.search(pattern, search_string) is not None:
                    product_list.append(products[i].strip("\n"))

            # Extract the product info to create product objects
            for product in product_list:
                pattern_1 = r"\"pro_id\": \"(\d+)\""
                match_1 = re.search(pattern_1, product)
                pro_id = match_1.group(1)
                pattern_2 = r"\"pro_model\": \"([^\"]*)\""
                match_2 = re.search(pattern_2, product)
                pro_model = match_2.group(1)
                pattern_3 = r"\"pro_category\": \"([^\"]*)\""
                match_3 = re.search(pattern_3, product)
                pro_category = match_3.group(1)
                pattern_4 = r"\"pro_name\": \"([^\"]*)\""
                match_4 = re.search(pattern_4, product)
                pro_name = match_4.group(1)
                pattern_5 = r"\"pro_current_price\": \"([^\"]*)\""
                match_5 = re.search(pattern_5, product)
                pro_current_price = match_5.group(1)
                pattern_6 = r"\"pro_raw_price\": \"([^\"]*)\""
                match_6 = re.search(pattern_6, product)
                pro_raw_price = match_6.group(1)
                pattern_7 = r"\"pro_discount\": \"([^\"]*)\""
                match_7 = re.search(pattern_7, product)
                pro_discount = match_7.group(1)
                pattern_8 = r"\"pro_likes_count\": \"([^\"]*)\""
                match_8 = re.search(pattern_8, product)
                pro_likes_count = match_8.group(1)
                product = Product(pro_id, pro_model, pro_category, pro_name, float(pro_current_price),
                                  float(pro_raw_price),
                                  int(pro_discount), int(pro_likes_count))

                # Append the objects into product_object_list
                product_object_list.append(product)
            return product_object_list

    def get_product_by_id(self, product_id):
        """
        Retrieve the product by product_id

        Parameters
        ----------
        product_id: str
            the provided product_id

        Returns
        ------
        A product object or None if the product is not found.
        """

        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.readlines()
            for prod in products:

                # Search the file to check if the provided product id exists
                pattern = r"\"pro_id\": \"(\d+)\""
                match = re.search(pattern, prod)

                # If the product id exists, extract the product info to create a product
                if match.group(1) == product_id:
                    pattern_2 = r"\"pro_model\": \"([^\"]*)\""
                    match_2 = re.search(pattern_2, prod)
                    pro_model = match_2.group(1)
                    pattern_3 = r"\"pro_category\": \"([^\"]*)\""
                    match_3 = re.search(pattern_3, prod)
                    pro_category = match_3.group(1)
                    pattern_4 = r"\"pro_name\": \"([^\"]*)\""
                    match_4 = re.search(pattern_4, prod)
                    pro_name = match_4.group(1)
                    pattern_5 = r"\"pro_current_price\": \"([^\"]*)\""
                    match_5 = re.search(pattern_5, prod)
                    pro_current_price = match_5.group(1)
                    pattern_6 = r"\"pro_raw_price\": \"([^\"]*)\""
                    match_6 = re.search(pattern_6, prod)
                    pro_raw_price = match_6.group(1)
                    pattern_7 = r"\"pro_discount\": \"([^\"]*)\""
                    match_7 = re.search(pattern_7, prod)
                    pro_discount = match_7.group(1)
                    pattern_8 = r"\"pro_likes_count\": \"([^\"]*)\""
                    match_8 = re.search(pattern_8, prod)
                    pro_likes_count = match_8.group(1)
                    product = Product(product_id, pro_model, pro_category, pro_name, float(pro_current_price), float(pro_raw_price), int(pro_discount), int(pro_likes_count))
                    return product
            else:
                return None

    def generate_category_figure(self):
        """
        Generate a bar chart displaying the total number of products for each category in descending order.
        """

        total_number = {}
        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.read()

            # Search all products in the accessories category
            acc_list = re.findall("\"pro_category\": \"accessories\"", products)

            # Count the number of products in the accessories category and put the result in a dictionary
            total_number["accessories"] = len(acc_list)

            bags_list = re.findall("\"pro_category\": \"bags\"", products)
            total_number["bags"] = len(bags_list)

            beauty_list = re.findall("\"pro_category\": \"beauty\"", products)
            total_number["beauty"] = len(beauty_list)

            house_list = re.findall("\"pro_category\": \"house\"", products)
            total_number["house"] = len(house_list)

            jewelry_list = re.findall("\"pro_category\": \"jewelry\"", products)
            total_number["jewelry"] = len(jewelry_list)

            kids_list = re.findall("\"pro_category\": \"kids\"", products)
            total_number["kids"] = len(kids_list)

            men_list = re.findall("\"pro_category\": \"men\"", products)
            total_number["men"] = len(men_list)

            shoes_list = re.findall("\"pro_category\": \"shoes\"", products)
            total_number["shoes"] = len(shoes_list)

            women_list = re.findall("\"pro_category\": \"women\"", products)
            total_number["women"] = len(women_list)

            # Sort the dictionary by the values in descending order
            sorted_total_number = dict(sorted(total_number.items(), key=lambda item: item[1], reverse=True))

            # Create the bar chart
            category = list(sorted_total_number.keys())
            value = list(sorted_total_number.values())
            plt.bar(category, value, linewidth = 1.5)
            plt.xlabel('Categories')
            plt.ylabel('Total Number of Products')
            plt.title('Total Number of Products in Categories')
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)

            # Save the bar chart ino the folder
            plt.savefig("data/figure/generate_category_figure.png")
            plt.close()

    def generate_discount_figure(self):
        """
        Generate a pie chart displaying the proportion of products with different discount values
        """

        discount = [0, 0, 0]
        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.read()
            pattern = r"\"pro_discount\": \"([^\"]*)\""

            # Collect all discount values in the products file
            result = re.findall(pattern, products)
            for num in result:
                if int(num) < 30:
                    discount[0] += 1
                elif 30 <= int(num) and int(num) <= 60:
                    discount[1] += 1

                else:
                    discount[2] += 1

            # Create the pie chart
            x = ["< 30", "30-60 (inclusive)", "> 60"]
            plt.pie(discount, labels = x)
            plt.title("Distribution of Products' Discounts")

            # Save the chart in the folder
            plt.savefig("data/figure/generate_discount_figure.png")
            plt.close()

    def generate_likes_count_figure(self):
        """
        Generate a bar chart displaying products’ likes_count for each category in ascending order.
        """

        acc_likes = []
        bags_likes = []
        beauty_likes = []
        house_likes = []
        jewelry_likes = []
        kids_likes = []
        men_likes = []
        shoes_likes = []
        women_likes = []
        likes_count = {}
        with open("data/products.txt", "r", encoding='utf-8') as products_file:
            products = products_file.readlines()
            pattern = r"\"pro_likes_count\": \"([^\"]*)\""
            for product in products:

                # If the product is in accessories category
                if re.search("\"pro_category\": \"accessories\"", product) is not None:

                    # Collect the number of likes-count to the list
                    acc_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"bags\"", product) is not None:
                    bags_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"beauty\"", product) is not None:
                    beauty_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"house\"", product) is not None:
                    house_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"jewelry\"", product) is not None:
                    jewelry_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"kids\"", product) is not None:
                    kids_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"men\"", product) is not None:
                    men_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"shoes\"", product) is not None:
                    shoes_likes += (re.findall(pattern, product))

                elif re.search("\"pro_category\": \"women\"", product) is not None:
                    women_likes += (re.findall(pattern, product))

            for i in range(len(acc_likes)):

                # Convert the string into integer
                acc_likes[i] = int(acc_likes[i])
            total = sum(acc_likes)

            # Put the result into a dictionary
            likes_count["accessories"] = total

            for i in range(len(bags_likes)):
                bags_likes[i] = int(bags_likes[i])
            total = sum(bags_likes)
            likes_count["bags"] = total

            for i in range(len(beauty_likes)):
                beauty_likes[i] = int(beauty_likes[i])
            total = sum(beauty_likes)
            likes_count["beauty"] = total

            for i in range(len(house_likes)):
                house_likes[i] = int(house_likes[i])
            total = sum(house_likes)
            likes_count["house"] = total

            for i in range(len(jewelry_likes)):
                jewelry_likes[i] = int(jewelry_likes[i])
            total = sum(jewelry_likes)
            likes_count["jewelry"] = total


            for i in range(len(kids_likes)):
                kids_likes[i] = int(kids_likes[i])
            total = sum(kids_likes)
            likes_count["kids"] = total

            for i in range(len(men_likes)):
                men_likes[i] = int(men_likes[i])
            total = sum(men_likes)
            likes_count["men"] = total

            for i in range(len(shoes_likes)):
                shoes_likes[i] = int(shoes_likes[i])
            total = sum(shoes_likes)
            likes_count["shoes"] = total

            for i in range(len(women_likes)):
                women_likes[i] = int(women_likes[i])
            total = sum(women_likes)
            likes_count["women"] = total

            # Sorting the dictionary by the values in ascending order
            sorted_likes_count = dict(sorted(likes_count.items(), key=lambda item: item[1]))

            # Create the bar chart
            category = list(sorted_likes_count.keys())
            likes = list(sorted_likes_count.values())
            plt.bar(category, likes, linewidth=1.5)
            plt.xlabel('Categories')
            plt.ylabel('The Sum of Like-Count')
            plt.title('Likes-count of Products in Different Categories')
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.ylim(0)
            plt.ticklabel_format(style='plain', axis='y')

            # Save the chart into the folder
            plt.savefig("data/figure/generate_likes_count_figure.png")
            plt.close()

    def generate_discount_likes_count_figure(self):
        """
        Generate a scatter chart displaying the relationship between likes_count and discount for all products.
        """

        with open("data/products.txt", "r" , encoding='utf-8') as products_file:
            products = products_file.read()
            pattern = r"\"pro_discount\": \"([^\"]*)\""

            # Search for all the discount values and put the values in a list
            discount = re.findall(pattern, products)
            for i in range(len(discount)):
                discount[i] = int(discount[i])

            pattern = r"\"pro_likes_count\": \"([^\"]*)\""

            # Search for all likes-count values and put the values in a list
            likes = re.findall(pattern, products)
            for i in range(len(likes)):
                likes[i] = int(likes[i])

        plt.scatter(discount, likes, linewidth=1.5, s=1)
        plt.xlabel("Discount")
        plt.ylabel("Likes-count")
        plt.title("The Relationship between Likes-count and Discount for All Products")

        # Save the chart into the folder
        plt.savefig("data/figure/generate_discount_likes_count_figure.png")
        plt.close()

    def delete_all_products(self):
        """
        Delete all products from the system
        """

        with open("data/products.txt", "w", encoding='utf-8') as products_file:
            products_file.write("")