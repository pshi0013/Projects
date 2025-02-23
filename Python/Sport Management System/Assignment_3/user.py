class User:
    def __init__(self, email, password):
        """
        Parameters
        ----------
        email : str
        The user's email
        password : str
        The user's password
        """

        self.email = email
        self.password = password

    def get_email(self):
        return f"'Email : ''{self.email}'"

    def get_password(self):
        return f"'Password : ''{self.password}'"

    def set_email(self, new_email):
        self.email = new_email

    def set_password(self, new_password):
        self.password = new_password




