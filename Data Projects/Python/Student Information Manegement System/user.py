import random
class User:
    user_list = []
    def __init__(self, user_id = 11111, user_name = "Tom", user_password = "Taylor ", user_role ="ST", user_status = "enabled"):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f'{self.user_id},{self.user_name},{self.user_password},{self.user_role},{self.user_status}'

    def generate_user_id(self):
        while True:
            new_user_id = random.randint(10000,99999)
            with open("data/user.txt", "r", encoding='utf-8') as user_file:
                for user in user_file:
                    user_tokens = user.split(",")
                    # Check if the number has already been used or not
                    if user_tokens[0] != new_user_id:
                        return new_user_id
                else:
                    print(f"user with id {new_user_id} already exists")

    def check_username_exist(self, user_name):
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(",")

                # If username exists, return True.
                if user_token[1] == user_name:
                    return True
            return False

    def encrypt(self, user_password):
        password = []
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        for each_letter in user_password:
            ascii_value = ord(each_letter)
            remainder1 = ascii_value % len(str_1)
            char_str1 = str_1[remainder1]
            remainder2 = user_password.index(each_letter) % len(str_2)
            char_str2 = str_2[remainder2]
            sum_str = char_str1 + char_str2
            password.append(sum_str)
        your_password = '^^^' + "".join(password) + '$$$'
        return your_password

    def login(self, user_name, user_password):
        with open("data/user.txt", "r", encoding='utf-8') as user_file:
            users = user_file.readlines()
            for i in range(len(users)):
                user_token = users[i].strip("\n").split(',')
                encrypt_password = self.encrypt(user_password)

                # If the user logs in as the admin, the password would be "password" to log in.
                if user_name == "admin" and user_password == "password":
                    if user_token[4] == "enabled":
                        return user_token
                    else:
                        return None

                # If the user is not the admin, the password would be encrypted to log in.
                elif user_token[1] == user_name and user_token[2] == encrypt_password:
                    if user_token[4] == "enabled":
                        return user_token
                    else:
                        return None

            return None