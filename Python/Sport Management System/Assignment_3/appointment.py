class Appointment:
    def __init__(self, member_name, member_status, reason, datetime, branch_name, pt_name, checkin=False):
        """
        Parameters
        ----------
        member_name : str
        The member's name
        member_status : str
        The member's status
        reason : str
        The appointment reason
        datetime : Local Datetime
        The appointment date and time
        branch_name : str
        The appointment branch
        checkin : boolean
        the checkin status of the appointment
        """

        self.member_name = member_name
        self.member_status = member_status
        self.reason = reason
        self.datetime = datetime
        self.branch_name = branch_name
        self.pt_name = pt_name
        self.checkin = checkin

    def get_member_name(self):
        return f"Member Name : {self.member_name}"

    def get_member_status(self):
        return f"Member Status : {self.member_status}"

    def get_reason(self):
        return f"Reason : {self.reason}"

    def get_datetime(self):
        return f"Datetime : {self.datetime}"

    def get_branch_name(self):
        return f"Branch : {self.branch_name}"

    def get_pt_name(self):
        return f"PT : {self.pt_name}"

    def get_checkin(self):
        return f"Checkin : {self.checkin}"

    def set_member_name(self, new_member_name):
        self.member_name = new_member_name

    def set_member_status(self, new_member_status):
        self.member_status = new_member_status

    def set_reason(self, new_reason):
        self.reason = new_reason

    def set_datetime(self, new_datetime):
        self.datetime = new_datetime

    def set_branch_name(self, new_branch_name):
        self.branch_name = new_branch_name

    def set_pt_name(self, new_pt_name):
        self.pt_name = new_pt_name

    def set_checkin(self, new_checkin):
        self.checkin = new_checkin