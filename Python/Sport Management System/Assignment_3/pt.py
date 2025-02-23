from datetime import datetime, timedelta


class Pt:
    def __init__(self, first_name, last_name, specialisation, gender, branch, portfolio):
        """
        Parameters
        ----------
        first_name : str
        The pt's firstname
        last_name : str
        The pt's lastname
        specialisation : str
        The pt's specialisation
        gender : str
        The pt's gender
        portfolio : str
        The pt's portfolio
        """

        self.first_name = first_name
        self.last_name = last_name
        self.specialisation = specialisation
        self.gender = gender
        self.branch = branch
        self.portfolio = portfolio

    def get_first_name(self):
        return f"First Name : {self.first_name}"

    def get_last_name(self):
        return f"Last Name : {self.last_name}"

    def get_specialisation(self):
        return f"Specialisation : {self.specialisation}"

    def get_gender(self):
        return f"Gender : {self.gender}"

    def get_branch(self):
        return f"Branch : {self.branch}"

    def get_portfolio(self):
        return f"Portfolio : {self.portfolio}"

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_specialisation(self, new_specialisation):
        self.specialisation = new_specialisation

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_branch(self, new_branch):
        self.branch = new_branch

    def set_portfolio(self, new_portfolio):
        self.portfolio = new_portfolio

    def generate_time_slots(self, chosen_date):
        # Generate time slots with the specified opening hours for the given date
        opening_hours = {
            "Monday": "6 am-10 pm",
            "Tuesday": "6 am-10 pm",
            "Wednesday": "6 am-10 pm",
            "Thursday": "6 am-10 pm",
            "Friday": "6 am-10 pm",
            "Saturday": "9 am-7 pm",
            "Sunday": "9 am-7 pm",
        }

        day_of_week = chosen_date.strftime("%A")
        opening_hours_str = opening_hours.get(day_of_week)

        if opening_hours_str:
            start_time_str, end_time_str = opening_hours_str.split("-")
            start_time = datetime.strptime(start_time_str.strip(), "%I %p")
            end_time = datetime.strptime(end_time_str.strip(), "%I %p")

            current_time = chosen_date.replace(hour=start_time.hour, minute=start_time.minute, second=0)
            time_slots = []

            while current_time <= chosen_date.replace(hour=end_time.hour, minute=end_time.minute, second=0):
                time_slots.append(current_time.strftime("%I:%M %p"))
                current_time += timedelta(minutes=30)

            return time_slots
        else:
            return []


