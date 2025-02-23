class Branch:
    def __init__(self, name, street, suburb, state, postcode, phone, opening_hours, list_of_pts):
        self.name = name
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.phone = phone
        self.opening_hours = opening_hours
        self.list_of_pts = list_of_pts

    def get_name(self):
        return f'Branch Name : {self.name}'

    def get_street(self):
        return f'Street : {self.street}'

    def get_suburb(self):
        return f'Suburb : {self.suburb}'

    def get_suburb(self):
        return f'State : {self.state}'

    def get_postcode(self):
        return f'Postcode : {self.postcode}'

    def get_phone(self):
        return f'Phone : {self.phone}'

    def get_opening_hours(self):
        return f'{self.opening_hours}'

    def get_list_of_pts(self):
        return f'{self.list_of_pts}'

    def set_name(self, new_name):
        self.name = new_name

    def set_street(self, new_street):
        self.street = new_street

    def set_suburb(self, new_suburb):
        self.suburb = new_suburb

    def set_state(self, new_state):
        self.state = new_state

    def set_postcode(self, new_postcode):
        self.postcode = new_postcode

    def set_phone(self, new_phone):
        self.phone = new_phone

    def set_opening_hours(self, new_opening_hours):
        self.opening_hours = new_opening_hours

    def set_list_of_pts(self, new_list_of_pts):
        self.list_of_pts = new_list_of_pts

branch = Branch("clayton",'df','df','df','df','df','df','df')
#print(branch.get_street())