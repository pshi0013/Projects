
class PtAvailability:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def get_date(self):
        return f"Date : {self.date}"

    def get_last_name(self):
        return f"Time: {self.time}"

    def set_first_name(self, new_date):
        self.date = new_date

    def set_last_name(self, new_time):
        self.time = new_time

