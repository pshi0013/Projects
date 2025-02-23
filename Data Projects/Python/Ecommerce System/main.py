"""
Name: Peichun Shih
Student ID: 33475881
The Creation Date: 28th May 2023
Last Modified Date:
Description: This script includes the main class which implements the entire program.
"""

import os
import re
import math
from model_admin import Admin
from model_customer import Customer
from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_user import UserOperation
from operation_product import ProductOperation
from operation_order import OrderOperation
from operation_admin import AdminOperation

def login_control():
    """
    Include the logic of login control
    """

    interface = IOInterface()
    user_operation = UserOperation()
    while True:
        try:
            user_name = interface.get_user_input("Please enter your user name: ", 1)

            # If the username is invalid, raise an error
            if not user_operation.validate_username(user_name[0]):
                raise ValueError

            user_password = interface.get_user_input("Please enter your password: ", 1)
            # If the username is invalid, raise an error
            if not user_operation.validate_password(user_password[0]):
                raise ValueError

            user_object = user_operation.login(user_name[0], user_password[0])

            # If the return object in a customer object, continue to the customer control.
            if isinstance(user_object, Customer):
                customer = user_object
                interface.print_message("Successful login!\n")
                customer_control(customer)
                break

            # If the return object in an admin object, continue to the admin control.
            elif isinstance(user_object, Admin):
                admin = user_object
                interface.print_message("Successful login!\n")
                admin_control(admin)
                break

            else:
                interface.print_error_message("UserOperation.login", "Incorrect username or password--user not found." )
                break

        except ValueError:
            interface.print_error_message("UserOperation.login", "\nInvalid input value. \nUsername: only contains letters or underscores; at least 5 characters"
                                                        "\nPassword: at least one letter and one number; greater than or equal to 5 characters.")

def customer_control(customer):
    """
       Include the manipulation related to customers

    Parameters
    ----------
        A customer object
    """

    interface = IOInterface()
    user_operation = UserOperation()
    customer_operation = CustomerOperation()
    order_operation = OrderOperation()
    product_operation = ProductOperation()
    while True:
        try:
            interface.customer_menu()
            user_input = interface.get_user_input("Please enter the choice: ", 1)
            #customer_dict = {}
            #customer_dict
            if user_input == ['1']:
                #print(customer_dict)
                interface.print_message("\nID: " + customer.user_id)
                interface.print_message("Name: " + customer.user_name)
                decrypted_password = user_operation.decrypt_password(customer.user_password)
                interface.print_message("Password: " + decrypted_password)
                interface.print_message("Registered time: " + customer.user_register_time)
                interface.print_message("Email: " + customer.user_email)
                interface.print_message("Mobile: " + customer.user_mobile + "\n")

            elif user_input == ['2']:
                while True:
                    attribute = interface.get_user_input("Please enter the attribute (Name, Password, Email or Mobile): ", 1)

                    # The user's input is case insensitive.
                    if attribute[0].lower() not in ['name', 'password', 'email', 'mobile']:
                        interface.print_error_message("CustomerOperation.update_profile", "Invalid attribute.")

                    else:
                        value = interface.get_user_input("Please enter the value you want to update: ", 1)
                        if customer_operation.update_profile(attribute[0], value[0], customer):
                            interface.print_message("Profile updated!\n")
                            break

                        else:
                            interface.print_error_message("CustomerOperation.update_profile", "Invalid value. Please enter again.")
                            break


            elif user_input == ['3']:
                while True:
                    product_keyword = interface.get_user_input("Please enter the keyword to search products: ", 1)

                    # if the user doesn't enter a keyword or only whitespaces
                    if not product_keyword[0].strip():
                        interface.print_error_message("ProductOperation.get_product_list_by_keyword",
                                                      "Please enter the keyword.")
                        break

                    product_list = product_operation.get_product_list_by_keyword(product_keyword[0])

                    # At least one product is found
                    if len(product_list) > 0:
                        interface.show_list("customer", "product", product_list)
                    else:
                        interface.print_message("\nNo product found.\n")
                    break


            elif user_input == ['4']:
                while True:
                    try:
                        order_list = []
                        with open("data/orders.txt", "r", encoding="utf-8") as orders_file:
                            orders = orders_file.readlines()
                            for i in range(len(orders)):
                                if re.search(customer.user_id, orders[i]) is not None:
                                    order_list.append(orders[i])

                        total_pages = math.ceil(len(order_list) / 10)

                        if total_pages == 0:
                            interface.print_message("No order found.")
                            break

                        order_page = interface.get_user_input("Please enter the page of order list(1-" + str(total_pages) + "): ", 1)
                        order_page_number = int(order_page[0])
                        if 1 <= order_page_number <= total_pages:
                            order_object_tuple = order_operation.get_order_list(customer.user_id, order_page_number)
                            order_object_list = [list(order_object_tuple[0]), order_object_tuple[1], order_object_tuple[2]]
                            interface.show_list("customer", "order", order_object_list)
                            break

                        else:
                            interface.print_error_message("OrderOperation.get_order_list",
                                                          "Invalid page number. Please enter a number between 1 and " + str(total_pages) + ")")

                    except ValueError:
                        interface.print_error_message("OrderOperation.get_order_list", "Invalid input. Please enter a valid page number.")

            elif user_input == ['5']:
                order_operation.generate_single_customer_consumption_figure(customer.user_id)
                interface.print_message("Customer consumption figure generated.")


            elif user_input == ['6']:
                pro_id = interface.get_user_input("Please enter the product id: ", 1)
                result = product_operation.get_product_by_id(pro_id[0])
                if result is None:
                    interface.print_message("Product Not Found.")
                else:
                    interface.print_message("\nProduct ID: " + result.pro_id)
                    interface.print_message("Model: " + result.pro_model)
                    interface.print_message("Category: " + result.pro_category)
                    interface.print_message("Name: " + result.pro_name)
                    interface.print_message("Current price: " + str(result.pro_current_price))
                    interface.print_message("Raw price: " + str(result.pro_raw_price))
                    interface.print_message("Discount: " + str(result.pro_discount))
                    interface.print_message("Likes-count: " + str(result.pro_likes_count) +"\n")

            elif user_input == ['7']:
                break

            else:
                raise ValueError

        except ValueError:
            interface.print_error_message("Main.customer_control", "Please input a valid choice")



def admin_control(admin):
    interface = IOInterface()
    product_operation = ProductOperation()
    customer_operation = CustomerOperation()
    order_operation = OrderOperation()
    while True:
        try:
            interface.admin_menu()
            user_input = interface.get_user_input("Please enter the choice: ", 5)

            # Filter out the empty string in the user_input list
            user_input = list(filter(lambda x: x != "", user_input))

            if user_input[0] == '1' and len(user_input) == 1:
                while True:
                    try:
                        # Ask to search by keyword or by page
                        search_choice = interface.get_user_input("1. By Keyword  2. By Page: ", 1)
                        if search_choice[0] == "1":
                            product_keyword = interface.get_user_input("Please enter the keyword to search products: ", 1)

                            # if the user doesn't enter a keyword or only whitespaces
                            if not product_keyword[0].strip():
                                interface.print_error_message("ProductOperation.get_product_list_by_keyword",
                                                                  "Please enter the keyword.")
                                break

                            product_list = product_operation.get_product_list_by_keyword(product_keyword[0])

                            # At least one product is found ( the same function of customer show list)
                            if len(product_list) > 0:
                                interface.show_list("customer", "product", product_list)
                                break
                            else:
                                interface.print_message("\nNo product found.\n")
                                break

                        if search_choice[0] == "2":
                            with open("data/products.txt", "r", encoding="utf-8") as products_file:
                                products = products_file.readlines()
                            total_pages = math.ceil(len(products) / 10)

                            if total_pages == 0:
                                interface.print_message("No product found.")
                                break

                            product_page = interface.get_user_input("Please enter the page of product list (1-7500): ", 1)
                            product_page_number = int(product_page[0])
                            if 1 <= product_page_number <= 7500:
                                product_object_tuple = product_operation.get_product_list(product_page_number)
                                product_object_list = [list(product_object_tuple[0]), product_object_tuple[1],
                                                    product_object_tuple[2]]
                                interface.show_list("admin", "product", product_object_list)
                                break
                            else:
                                interface.print_error_message("ProductOperation.get_product_list",
                                                           "Invalid page number. Please enter a number between 1 and 7500.")
                                break
                        else:
                            raise ValueError

                    except ValueError:
                        interface.print_error_message("ProductOperation.get_product_list",
                                                      "Invalid input. Please enter a valid number.")

            elif user_input[0] == '2':
                if not len(user_input) == 5:
                    interface.print_error_message("CustomerOperation.register_customer", "Please input complete infomation to add a customer.")

                else:
                    if customer_operation.register_customer(user_input[1], user_input[2], user_input[3], user_input[4]):
                        interface.print_message("Customer added successfully!")

                    else:
                        interface.print_error_message("CustomerOperation.register_customer",
                                                      "Invalid values. Please input again.")

            elif user_input[0] == '3' and len(user_input) == 1:
                while True:
                    try:
                        customer_list = []
                        with open("data/users.txt", "r", encoding='utf-8') as users_file:
                            users = users_file.readlines()
                            users = [user.rstrip('\n') for user in users]
                            for user in users:
                                if re.search("customer", user) is not None:
                                    customer_list.append(user)

                            total_pages = math.ceil(len(customer_list) / 10)

                        if total_pages == 0:
                            interface.print_message("No customer found.")
                            break

                        customer_page = interface.get_user_input("Please enter the page of customer list(1-" + str(total_pages) + "): ", 1)
                        customer_page_number = int(customer_page[0])
                        if 1 <= customer_page_number <= total_pages:
                            customer_object_tuple = customer_operation.get_customer_list(customer_page_number)
                            customer_object_list = [list(customer_object_tuple[0]), customer_object_tuple[1], customer_object_tuple[2]]
                            interface.show_list("admin", "customer", customer_object_list)
                            break

                        else:
                            interface.print_error_message("OrderOperation.get_order_list",
                                                          "Invalid page number. Please enter a number between 1 and " + str(total_pages)+".")

                    except ValueError:
                        interface.print_error_message("OrderOperation.get_order_list", "Invalid input. Please enter a valid page number.")

            elif user_input[0] == '4' and len(user_input) == 1:
                while True:
                    try:
                        with open("data/orders.txt", "r", encoding="utf-8") as orderss_file:
                            orders = orderss_file.readlines()
                            total_pages = math.ceil(len(orders) / 10)

                        if total_pages == 0:
                            interface.print_message("No order found.")
                            break

                        order_page = interface.get_user_input("Please enter the page of order list (1-" + str(total_pages) + "): ", 1)
                        order_page_number = int(order_page[0])
                        if 1 <= order_page_number <= total_pages:
                            order_object_tuple = order_operation.get_order_list("", order_page_number)
                            order_object_list = [list(order_object_tuple[0]), order_object_tuple[1], order_object_tuple[2]]
                            interface.show_list("admin", "order", order_object_list)
                            break
                        else:
                            interface.print_error_message("ProductOperation.get_product_list",
                                                              "Invalid page number. Please enter a number between 1 and " + str(total_pages)+".")
                            break

                    except ValueError:
                        interface.print_error_message("ProductOperation.get_order_list", "Invalid input. Please enter a valid number.")

            elif user_input[0] == '5' and len(user_input) == 1:
                order_operation.generate_test_order_data()

            elif user_input[0] == '6' and len(user_input) == 1:
                product_operation.generate_category_figure()
                interface.print_message("\nCategory figure generated.")
                product_operation.generate_discount_figure()
                interface.print_message("Discount figure generated.")
                product_operation.generate_likes_count_figure()
                interface.print_message("Likes-count figure generated.")
                product_operation.generate_discount_likes_count_figure()
                interface.print_message("Discount likes-count figure generated.")
                order_operation.generate_all_customers_consumption_figure()
                interface.print_message("All customers' consumption figure generated.")
                order_operation.generate_all_top_10_best_sellers_figure()
                interface.print_message("All top 10 best-sellers figure generated.")

            elif user_input[0] == '7' and len(user_input) == 1:
                customer_operation.delete_all_customers()
                order_operation.delete_all_orders()
                product_operation.delete_all_products()
                interface.print_message("All data deleted (except admin info).")

                # Delete the csv files
                if os.path.exists("data/customers_list.csv"):
                    os.remove("data/customers_list.csv")
                if os.path.exists("data/orders_list.csv"):
                    os.remove("data/orders_list.csv")
                if os.path.exists("data/products_list.csv"):
                    os.remove("data/products_list.csv")

            elif user_input[0] == '8' and len(user_input) == 1:
                customer_id = interface.get_user_input("Please enter the customer's user ID: ", 1)
                result = customer_operation.delete_customer(customer_id[0])
                if result:
                    interface.print_message("Customer deleted!")
                else:
                    interface.print_message("Customer not found.")

            elif user_input[0] == '9' and len(user_input) == 1:
                order_id = interface.get_user_input("Please enter the order ID: ", 1)
                result = order_operation.delete_order(order_id[0])
                if result:
                    interface.print_message("Order deleted!")
                else:
                    interface.print_message("Order not found.")

            elif user_input[0] == '10' and len(user_input) == 1:
                product_id = interface.get_user_input("Please enter the product ID: ", 1)
                result = product_operation.delete_product(product_id[0])
                if result:
                    interface.print_message("Product deleted!")
                else:
                    interface.print_message("Product not found.")

            elif user_input[0] == '11' and len(user_input) == 1:
                product_operation.delete_all_products()
                interface.print_message("All products deleted.")

            elif user_input[0] == '12' and len(user_input) == 1:
                order_operation.delete_all_orders()
                interface.print_message("All orders deleted.")

            elif user_input[0] == '13' and len(user_input) == 1:
                break

            else:
                raise ValueError

        except ValueError:
            interface.print_error_message("Main.customer_control", "Please input a valid choice")

def main():
    admin_operation = AdminOperation()
    product_operation = ProductOperation()
    order_operation = OrderOperation()
    user_operation = UserOperation()
    interface = IOInterface()
    customer_operation = CustomerOperation()
    product_operation.extract_products_from_files()
    order_operation.generate_test_order_data()
    admin_operation.register_admin()
    while True:
        interface.print_message("\n  Welcome to the e-shopping mall!")
        interface.print_message("===================================")
        interface.main_menu()
        try:
            user_input = interface.get_user_input("Please enter the choice: ", 1)

            # Login
            if user_input == ['1']:
                login_control()

            # Register
            elif user_input == ['2']:
                while True:
                    interface.print_message("\nUsername only contains letters or underscores; at least 5 characters.")
                    interface.print_message("------------------------------------------------------------------------")
                    user_name = interface.get_user_input("Please enter the username: ", 1)
                    if user_operation.check_username_exist(user_name[0]):
                        interface.print_message("\nThe username has been used. Please use another username.")
                        continue

                    else:
                        interface.print_message("\nPassword should contain at least one letter and one number; at lease 5 characters.")
                        interface.print_message("-------------------------------------------------------------------------------------")
                        user_password = interface.get_user_input("Please enter the password: ", 1)
                        interface.print_message("\nEmail should contain username, the @ symbol, domain name, and dot (.)")
                        interface.print_message("-----------------------------------------------------------------------")
                        user_email = interface.get_user_input("Please enter the email: ", 1)
                        interface.print_message("\nMobile should contain 10 digits long and starting with '04' or '03'.")
                        interface.print_message("----------------------------------------------------------------------")
                        user_mobile = interface.get_user_input("Please enter the mobile: ", 1)

                        # Check the result of registering a customer
                        result = customer_operation.register_customer(user_name[0], user_password[0], user_email[0], user_mobile[0])
                        if result:
                            interface.print_message("\nRegistered successfully!")
                            break

                        else:
                            interface.print_error_message("\nCustomerOperation.register_customer", "Invalid values. Please register again.")
                            break

            # Exit
            elif user_input == ['3']:

                # Delete the csv files
                if os.path.exists("data/customers_list.csv"):
                    os.remove("data/customers_list.csv")
                if os.path.exists("data/orders_list.csv"):
                    os.remove("data/orders_list.csv")
                if os.path.exists("data/products_list.csv"):
                    os.remove("data/products_list.csv")
                interface.print_message("\nGood bye!\n")
                break

            else:
                raise ValueError

        except ValueError:
            interface.print_error_message(IOInterface, "Invalid input value. Please enter a valid choice (1, 2, or 3).")

if __name__ == "__main__":
    main()