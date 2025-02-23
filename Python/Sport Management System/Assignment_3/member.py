from user import User
class Member(User):

    def __init__(self, email, password, first_name , last_name, phone, street, suburb, state, postcode, favorite_branch, favorite_pt):
        """
        Parameters
        ----------
        email : str
        The user's email
        password : str
        The user's password
        first_name : str
        The member's firstname
        last_name : str
        The member's lastname
        phone : str
        The member's phone
        street : str
        The member's address
        suburb : str
        The member's address
        state : str
        The member's address
        postcode : str
        The member's address
        favorite_branch : list
        The member's favorite branches
        favorite_pt : list
        The member's favorite pts
        """

        super().__init__(email, password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.favorite_branch = favorite_branch
        self.favorite_pt = favorite_pt

    def get_first_name(self):
        return f"First Name : {self.first_name}"

    def get_last_name(self):
        return f"Password : {self.last_name}"

    def get_phone(self):
        return f"Phone : {self.phone}"

    def get_street(self):
        return f"Street : {self.street}"

    def get_suburb(self):
        return f"Suburb : {self.suburb}"

    def get_state(self):
        return f"State : {self.state}"

    def get_postcode(self):
        return f"Postcode : {self.postcode}"

    def get_favorite_branch(self):
        return self.favorite_branch

    def get_favorite_list(self):
        return self.favorite_pt

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_phone(self, new_phone):
        self.phone = new_phone

    def set_street(self, new_street):
        self.street = new_street

    def set_suburb(self, new_suburb):
        self.suburb = new_suburb

    def set_state(self, new_state):
        self.state = new_state

    def set_postcode(self, new_postcode):
        self.postcode = new_postcode

    def set_favorite_branch(self, new_favorite_branch):
        self.favorite_branch = new_favorite_branch

    def set_favorite_pt(self, new_favorite_pt):
        self.favorite_pt = new_favorite_pt