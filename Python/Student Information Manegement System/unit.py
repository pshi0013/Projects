import random
class Unit:
    unit_list=[]
    def __init__(self, unit_id, unit_code, unit_name, unit_capacity):
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __init__(self, unit_id = 1111111, unit_code = "FIT9136", unit_name = "Tom",unit_capacity = 100):
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return f'{self.unit_id},{self.unit_code},{self.unit_name},{self.unit_capacity}'

    def generate_unit_id(self):
        while True:
            new_unit_id = str(random.randint(1000000, 9999999))
            with open("data/unit.txt", "r",encoding='utf-8') as unit_file:
                for unit in unit_file:
                    unit_tokens = unit.split(",")

                    # Check if the number has already been used or not
                    if unit_tokens[0] != new_unit_id:
                        return new_unit_id
                else:
                    print(f"user with id {new_user_id} already exists")