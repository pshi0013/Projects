import re
import datetime
from user import User
from member import Member
from branch import Branch
from pt import Pt
from appointment import Appointment
from userinterface import UserInterface
from datetime import datetime, timedelta


class MonashSportsSystem:
    def __init__(self, list_of_users=[], list_of_branches=[], list_of_pts=[], list_of_appointments=[]):
        """
            Initializes the MonashSportsSystem object with user, branch, PT, and appointment data.

            Args:
                list_of_users (list, optional): A list of user objects. Defaults to an empty list.
                list_of_branches (list, optional): A list of branch objects. Defaults to an empty list.
                list_of_pts (list, optional): A list of PT objects. Defaults to an empty list.
                list_of_appointments (list, optional): A list of appointment objects. Defaults to an empty list.

            Attributes:
                list_of_users (list): A list of user objects.
                list_of_branches (list): A list of branch objects.
                list_of_pts (list): A list of PT objects initialized with time slots.
                list_of_appointments (list): A list of appointment objects.
                reasons (dict): A dictionary mapping reason codes to their descriptions.
            """
        self.list_of_users = list_of_users
        self.list_of_branches = list_of_branches
        # self.list_of_pts = list_of_pts
        self.list_of_pts = self.initialize_pts_with_time_slots(list_of_pts)
        self.list_of_appointments = list_of_appointments
        self.reasons = {
            1: ["Strength and conditioning coach"],
            2: ["Group exercise instructor"],
            3: ["Fitness manager"]
        }

    def login(self):
        """
            Allows a user to log in by entering their email and password.

            Returns:
                Member or None: A Member object if the login is successful, or None if unsuccessful.
            """
        interface = UserInterface()
        while True:
            email = interface.get_user_input("Email: ")
            password = interface.get_user_input("Password: ")

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                interface.print_message("Invalid email format. Please enter a valid email address.")
                choice = interface.get_user_input("Enter 'R' to retry or 'Q' to go back: ")
                if choice.upper() == "Q":
                    return None
                elif choice.upper() == "R":
                    continue
                else:
                    interface.print_message("Invalid choice. Please try again.")
                return None

            if len(password) < 6:
                interface.print_message("Password must be at least 6 characters long.")
                choice = interface.get_user_input("Enter 'R' to retry or 'Q' to go back: ")
                if choice.upper() == "Q":
                    return None
                elif choice.upper() == "R":
                    continue
                else:
                    interface.print_message("Invalid choice. Please try again.")
                return None

            # Search the user info in user txt.
            with open("data/user.txt", "r", encoding="utf-8") as user_file:
                for user in user_file:
                    user = user.strip("\n")
                    user_dict = eval(user)
                    if email == user_dict['email'] and password == user_dict['password']:
                        interface.print_message("Successful login!")
                        member_obj = Member(user_dict['email'], user_dict['password'], user_dict['first_name'],
                                            user_dict['last_name'],
                                            user_dict['mobile'], user_dict['street'], user_dict['suburb'],
                                            user_dict['state'], user_dict['postcode'], user_dict['favorite_branch'],
                                            user_dict['favorite_pt'])
                        return member_obj

                interface.print_message("User Not Found.")
                choice = interface.get_user_input("\nEnter any key to login again or 'Q' to go back: ")
                if choice.upper() == "Q":
                    break

    def search_branch_by_suburb(self):
        """
            Allows a user to search for a branch by suburb and select a reason for an appointment.

            Returns:
                Tuple[Branch, int] or None: A tuple containing a Branch object and a reason code if successful, or None if unsuccessful.
            """
        interface = UserInterface()
        while True:
            selected_branch = None
            suburb = ""

            while not suburb:
                suburb = interface.get_user_input("Please enter the suburb name: ")
                if not suburb:
                    print("Suburb name cannot be empty. Please try again.")
                elif not suburb.isalpha():
                    print("Suburb name cannot contain numbers. Please try again.")
                    suburb = ""

            # Search suburb name in branch txt.
            with open("data/branch.txt", "r", encoding="utf-8") as branch_file:
                for branch in branch_file:
                    branch = branch.strip("\n")
                    branch_dict = eval(branch)
                    branch_obj = Branch(branch_dict['name'], branch_dict['street'], branch_dict['suburb'],
                                        branch_dict['state'],
                                        branch_dict['postcode'], branch_dict['phone'], branch_dict['opening_hours'],
                                        branch_dict['pts'])

                    if suburb.upper() == branch_obj.suburb.upper():
                        selected_branch = branch_obj

            if selected_branch is None:
                print("Suburb not found.")
                choice = interface.get_user_input("\nEnter any key to try again or 'Q' to go back: ")
                if choice.upper() == "Q":
                    break

            else:
                interface.display_appointment_reason()
                reason = int(interface.get_user_input("Please enter the reason: "))
                if reason not in [1, 2, 3]:
                    print("Invalid option")

                valid_spec = self.reasons[reason]
                pt_list = []
                with open("data/pt.txt", "r", encoding="utf-8") as pt_file:
                    for pt in pt_file:
                        pt = pt.strip("\n")
                        pt_dict = eval(pt)
                        if pt_dict['specialisation'] in valid_spec:
                            pt_list.append(pt_dict['first_name'])

                final_pts = []
                for valid_pts in pt_list:
                    for b_pts in eval(selected_branch.get_list_of_pts()):
                        if valid_pts == b_pts[0]:
                            final_pts.append(b_pts)

                selected_branch.set_list_of_pts(final_pts)
                interface.display_branch(selected_branch)
                return selected_branch, reason

    def search_branch_by_postcode(self):
        """
            Allows a user to search for a branch by postcode and select a reason for an appointment.

            Returns:
                Tuple[Branch, int] or None: A tuple containing a Branch object and a reason code if successful, or None if unsuccessful.
            """
        interface = UserInterface()
        while True:
            selected_branch = None
            postcode = ""

            while not postcode:
                postcode = interface.get_user_input("Please enter the postcode: ")
                if not postcode:
                    print("Postcode cannot be empty. Please try again.")
                elif not postcode.isnumeric() or len(postcode) != 4:
                    print("Postcode must be a 4-digit number. Please try again.")
                    postcode = ""

            # Search postcode in branch txt.
            with open("data/branch.txt", "r", encoding="utf-8") as branch_file:
                for branch in branch_file:
                    branch = branch.strip("\n")
                    branch_dict = eval(branch)
                    branch_obj = Branch(branch_dict['name'], branch_dict['street'], branch_dict['suburb'],
                                        branch_dict['state'],
                                        branch_dict['postcode'], branch_dict['phone'], branch_dict['opening_hours'],
                                        branch_dict['pts'])

                    if postcode == branch_obj.postcode:
                        selected_branch = branch_obj

            if selected_branch is None:
                print("Branch not found for the given postcode.")
                choice = interface.get_user_input("\nEnter any key to try again or 'Q' to go back: ")
                if choice.upper() == "Q":
                    break

            else:
                interface.display_appointment_reason()
                reason = int(interface.get_user_input("Please enter the reason: "))
                if reason not in [1, 2, 3]:
                    print("Invalid option")

                valid_spec = self.reasons[reason]
                pt_list = []
                with open("data/pt.txt", "r", encoding="utf-8") as pt_file:
                    for pt in pt_file:
                        pt = pt.strip("\n")
                        pt_dict = eval(pt)
                        if pt_dict['specialisation'] in valid_spec:
                            pt_list.append(pt_dict['first_name'])

                final_pts = []
                for valid_pts in pt_list:
                    for b_pts in eval(selected_branch.get_list_of_pts()):
                        if valid_pts == b_pts[0]:
                            final_pts.append(b_pts)

                selected_branch.set_list_of_pts(final_pts)
                interface.display_branch(selected_branch)
                return selected_branch, reason

    def search_branch_by_current_address(self, member_obj):
        """
           Searches for a branch based on a member's current suburb and postcode and allows them to select a reason for booking an appointment.

           Args:
               member_obj (Member): The Member object representing the current member.

           Returns:
               Tuple[Branch, int] or Tuple[None, None]: A tuple containing a Branch object and a reason code if a branch is found, or
               a tuple containing None values if no branch is found.
           """
        interface = UserInterface()
        selected_branch = None
        reason = None

        with open("data/branch.txt", "r", encoding="utf-8") as branch_file:
            for branch in branch_file:
                branch = branch.strip("\n")
                branch_dict = eval(branch)
                branch_obj = Branch(branch_dict['name'], branch_dict['street'], branch_dict['suburb'],
                                    branch_dict['state'],
                                    branch_dict['postcode'], branch_dict['phone'], branch_dict['opening_hours'],
                                    branch_dict['pts'])

                # Search the suburb name and postcode that match member's suburb and postcode in branch txt.
                if member_obj.suburb.upper() == branch_obj.suburb.upper() or member_obj.postcode == branch_obj.postcode:
                    interface.display_branch(branch_obj)
                    interface.display_appointment_reason()  # Display reasons for booking
                    reason = int(interface.get_user_input("Please enter a reason for booking (1, 2, or 3): "))
                    if reason not in [1, 2, 3]:
                        interface.print_message("Invalid reason. Please try again.")
                    else:
                        valid_spec = self.reasons[reason]
                        pt_list = []
                        with open("data/pt.txt", "r", encoding="utf-8") as pt_file:
                            for pt in pt_file:
                                pt = pt.strip("\n")
                                pt_dict = eval(pt)
                                if pt_dict['specialisation'] in valid_spec:
                                    pt_list.append(pt_dict['first_name'])

                        final_pts = []
                        for valid_pts in pt_list:
                            for b_pts in branch_obj.list_of_pts:  # Removed eval()
                                if valid_pts == b_pts[0]:
                                    final_pts.append(b_pts)

                        branch_obj.set_list_of_pts(final_pts)
                        interface.display_branch(branch_obj)
                        return branch_obj, reason

        interface.print_message("No branch found.")
        return selected_branch, reason

    def search_branch(self, member_obj):
        """
            Search for a branch based on user input and return the branch object.

            Args:
                member_obj (object): The member object for whom the branch is being searched.

            Returns:
                object: The branch object found based on the search criteria.
            """
        interface = UserInterface()
        interface.search_menu()
        search_choice = interface.get_user_input("\nPlease enter your choice: ")
        while True:
            if search_choice == "1":
                branch_obj = system.search_branch_by_current_address(member_obj)
                return branch_obj
            elif search_choice == "2":
                branch_obj, reason = system.search_branch_by_suburb()
                return branch_obj, reason
            elif search_choice == "3":
                branch_obj, reason = system.search_branch_by_postcode()
                return branch_obj, reason
            elif search_choice == "4":
                break
            else:
                interface.print_message("Invalid input. Please enter again.")
                interface.search_menu()
                search_choice = interface.get_user_input("\nPlease enter your choice: ")

    def add_favorite_branch(self, member_obj, branch_obj):
        interface = UserInterface()
        updated_users = []
        with open("data/user.txt", "r+", encoding="utf-8") as user_file:
            for user in user_file:
                user = user.strip("\n")
                user_dict = eval(user)
                if user_dict['email'] == member_obj.email:
                    if branch_obj.name in user_dict['favorite_branch']:
                        interface.print_message("This branch has been already added.")
                    else:
                        # Add the branch in member's favorite branch list
                        user_dict['favorite_branch'].append(branch_obj.name)
                        interface.print_message("Successfully added this branch as favorite!")

                updated_users.append(str(user_dict) + '\n')
            user_file.seek(0)
            # Write the updated info in user txt.
            user_file.writelines(updated_users)
            user_file.truncate()

    def add_favorite_pt(self, member_obj, pt_obj):
        interface = UserInterface()
        updated_users = []
        with open("data/user.txt", "r+", encoding="utf-8") as user_file:
            for user in user_file:
                user = user.strip("\n")
                user_dict = eval(user)
                pt_full_name = pt_obj.first_name + " " + pt_obj.last_name
                if user_dict['email'] == member_obj.email:
                    if pt_full_name in user_dict['favorite_pt']:
                        interface.print_message("This PT has been already added.")
                    else:
                        # Add the PT in member's favorite PT list
                        user_dict['favorite_pt'].append(pt_full_name)
                        interface.print_message("Successfully added this PT as favorite!")

                updated_users.append(str(user_dict) + '\n')
            user_file.seek(0)
            # Write the updated info in user txt.
            user_file.writelines(updated_users)
            user_file.truncate()

    def view_pt(self, branch_obj):
        interface = UserInterface()

        # Sort PT by their name alphabetically
        sorted_list_of_pts = sorted(branch_obj.list_of_pts)
        number = interface.get_user_input("Enter the PT's number (see above): ")
        try:
            number = int(number)
        except ValueError:
            interface.print_message("Invalid input. Please enter again.")
            return None

        if int(number) > len(sorted_list_of_pts) or int(number) - 1 < 0:
            interface.print_message("Invalid input. Please enter again.")
            return None

        else:
            pt_name = sorted_list_of_pts[int(number) - 1]
            with open("data/pt.txt", "r", encoding="utf-8") as pt_file:
                for pt in pt_file:
                    pt = pt.strip("\n")
                    pt_dict = eval(pt)
                    if pt_dict["first_name"] == pt_name[0] and pt_dict["last_name"] == pt_name[1]:
                        pt_obj = Pt(pt_dict["first_name"],
                                    pt_dict["last_name"],
                                    pt_dict["specialisation"],
                                    pt_dict["gender"],
                                    pt_dict["branch"],
                                    pt_dict["portfolio"])

                        interface.print_message("\n" + pt_obj.get_first_name())
                        interface.print_message(pt_obj.get_last_name())
                        interface.print_message(pt_obj.get_specialisation())
                        interface.print_message(pt_obj.get_portfolio())
                        return pt_obj

    def make_an_appointment(self, member_obj):
        interface = UserInterface()
        system = MonashSportsSystem()
        while True:
            interface.booking_menu()
            booking_choice = interface.get_user_input("\nPlease enter your choice: ")
            if booking_choice == "1":
                branch_obj, reason = system.search_branch(member_obj)
                if branch_obj is not None:
                    while True:
                        interface.branch_option()
                        branch_option = interface.get_user_input("Please enter your option: ")
                        if branch_option == "1":
                            system.add_favorite_branch(member_obj, branch_obj)
                        elif branch_option == "2":
                            pt_obj = system.view_pt(branch_obj)
                            if pt_obj is None:
                                continue
                            else:
                                while True:
                                    interface.pt_option()
                                    pt_choice = interface.get_user_input("Please enter your option: ")
                                    if pt_choice == "1":
                                        system.add_favorite_pt(member_obj, pt_obj)
                                    elif pt_choice == "2":
                                        system.book_appointment(member_obj, pt_obj, branch_obj, reason)
                                    elif pt_choice == "3":
                                        interface.display_branch(branch_obj)
                                        break
                                    else:
                                        interface.print_message("Invalid input. Please enter again.")

                        elif branch_option == "3":
                            break

                        else:
                            interface.print_message("Invalid input. Please enter again.")

            elif booking_choice == "2":
                system.show_favorite_branch(member_obj)

            elif booking_choice == "3":
                system.show_favorite_pt(member_obj)

            elif booking_choice == "4":
                break

            else:
                interface.print_message("Invalid input. Please enter again.")

    def search_favorite_branch(self, member_obj):
        interface = UserInterface()
        number = interface.get_user_input("Please enter the branch number (see above): ")
        try:
            number = int(number)
        except ValueError:
            interface.print_message("Invalid input. Please enter again.")
            return None

        if int(number) > len(member_obj.favorite_branch) or int(number) - 1 < 0:
            interface.print_message("Invalid input. Please enter again.")
            return None

        else:
            branch_name = member_obj.favorite_branch[len(member_obj.favorite_branch) - number]

            # Search the branch in branch txt.
            with open("data/branch.txt", "r", encoding="utf-8") as branch_file:
                for branch in branch_file:
                    branch = branch.strip("\n")
                    branch_dict = eval(branch)
                    if branch_dict["name"] == branch_name:
                        branch_obj = Branch(branch_dict["name"], branch_dict["street"], branch_dict["suburb"],
                                            branch_dict["state"], branch_dict["postcode"], branch_dict["phone"],
                                            branch_dict["opening_hours"], branch_dict["pts"])

                        interface.display_branch(branch_obj)
                        return branch_obj

    def delete_favorite_branch(self, member_obj):
        interface = UserInterface()
        number = interface.get_user_input("Please enter the branch number (see above): ")
        try:
            number = int(number)
        except ValueError:
            interface.print_message("Invalid input. Please enter again.")
            return None

        if int(number) > len(member_obj.favorite_branch) or int(number) - 1 < 0:
            interface.print_message("Invalid input. Please enter again.")
            return None

        else:
            branch_name = member_obj.favorite_branch[len(member_obj.favorite_branch) - number]
            member_obj.favorite_branch.remove(branch_name)
            updated_users = []
            with open("data/user.txt", "r", encoding="utf-8") as user_file:
                for user in user_file:
                    user = user.strip("\n")
                    user_dict = eval(user)
                    if user_dict["email"] == member_obj.email:
                        user_dict["favorite_branch"] = member_obj.favorite_branch

                    updated_users.append(str(user_dict))

                # Write updated info to user txt.
                with open("data/user.txt", "w", encoding="utf-8") as user_file:
                    user_file.writelines("\n".join(updated_users))

                interface.print_message("Deleted successfully!")

    def show_favorite_branch(self, member_obj):
        interface = UserInterface()
        while True:
            interface.display_favorite_branch(member_obj)
            interface.favorite_branch_option()
            fb_option = interface.get_user_input("Please enter your option: ")
            if fb_option == "1":
                branch_obj = system.search_favorite_branch(member_obj)
                if branch_obj is not None:
                    pt_obj = system.view_pt(branch_obj)
                    if pt_obj is None:
                        continue
                    else:
                        while True:
                            interface.pt_option()
                            pt_choice = interface.get_user_input("Please enter your option: ")
                            if pt_choice == "1":
                                system.add_favorite_pt(member_obj, pt_obj)

                                # need to add booking function
                            elif pt_choice == "2":
                                break
                            elif pt_choice == "3":
                                interface.display_branch(branch_obj)
                                break
                            else:
                                interface.print_message("Invalid input. Please enter again.")


            elif fb_option == "2":
                system.delete_favorite_branch(member_obj)

            elif fb_option == "3":
                break

            else:
                interface.print_message("Invalid input. Please enter again.")

    def search_favorite_pt(self, member_obj):
        interface = UserInterface()
        number = interface.get_user_input("Please enter the PT's number (see above): ")
        try:
            number = int(number)
        except ValueError:
            interface.print_message("Invalid input. Please enter again.")
            return None

        if int(number) > len(member_obj.favorite_pt) or int(number) - 1 < 0:
            interface.print_message("Invalid input. Please enter again.")
            return None

        else:
            pt_name = member_obj.favorite_pt[len(member_obj.favorite_pt) - number]

            # Search the PT in pt txt.
            with open("data/pt.txt", "r", encoding="utf-8") as pt_file:
                for pt in pt_file:
                    pt = pt.strip("\n")
                    pt_dict = eval(pt)
                    pt_full_name = pt_dict['first_name'] + " " + pt_dict['last_name']
                    if pt_full_name == pt_name:
                        pt_obj = Pt(pt_dict["first_name"], pt_dict["last_name"], pt_dict["specialisation"],
                                    pt_dict["gender"], pt_dict["branch"], pt_dict["portfolio"])

                        interface.print_message("\n" + pt_obj.get_first_name())
                        interface.print_message(pt_obj.get_last_name())
                        interface.print_message(pt_obj.get_specialisation())
                        interface.print_message(pt_obj.get_portfolio())
                        return pt_obj

    def delete_favorite_pt(self, member_obj):
        interface = UserInterface()
        number = interface.get_user_input("Please enter the PT's number (see above): ")
        try:
            number = int(number)
        except ValueError:
            interface.print_message("Invalid input. Please enter again.")
            return None

        if int(number) > len(member_obj.favorite_pt) or int(number) - 1 < 0:
            interface.print_message("Invalid input. Please enter again.")
            return None

        else:
            pt_name = member_obj.favorite_pt[len(member_obj.favorite_pt) - number]
            member_obj.favorite_pt.remove(pt_name)
            updated_users = []
            with open("data/user.txt", "r", encoding="utf-8") as user_file:
                for user in user_file:
                    user = user.strip("\n")
                    user_dict = eval(user)
                    if user_dict["email"] == member_obj.email:
                        user_dict["favorite_pt"] = member_obj.favorite_pt

                    updated_users.append(str(user_dict))

                # Write updated info to user txt.
                with open("data/user.txt", "w", encoding="utf-8") as user_file:
                    user_file.writelines("\n".join(updated_users))

                interface.print_message("Deleted successfully!")

    def show_favorite_pt(self, member_obj):
        """
            Display and manage a member's favorite personal trainers.

            Args:
                member_obj (object): The member object for whom favorite personal trainers are being managed.
            """
        interface = UserInterface()
        while True:
            interface.display_favorite_pt(member_obj)
            interface.favorite_pt_option()
            fp_option = interface.get_user_input("Please enter your option: ")
            if fp_option == "1":
                pt_obj = system.search_favorite_pt(member_obj)
                if pt_obj is None:
                    continue
                else:
                    # Extract the reason (specialization) from pt_obj
                    reason = pt_obj.get_specialisation().split(': ')[1]

                    # Extract the branch name from pt_obj
                    branch_name = pt_obj.get_branch().split(': ')[1]

                    # Search for the branch_obj associated with the branch_name in branch.txt
                    branch_obj = self.search_branch_by_name(branch_name)

                while True:
                    interface.pt_option()
                    pt_choice = interface.get_user_input("Please enter your option: ")
                    if pt_choice == "1":
                        system.add_favorite_pt(member_obj, pt_obj)
                    elif pt_choice == "2":
                        self.book_appointment_with_favorite_pt(member_obj, pt_obj, branch_obj)
                    elif pt_choice == "3":
                        break
                    else:
                        interface.print_message("Invalid input. Please enter again.")

            elif fp_option == "2":
                system.delete_favorite_pt(member_obj)
                # Add the code to call the booking function here if needed

            elif fp_option == "3":
                break

            else:
                interface.print_message("Invalid input. Please enter again.")

    def search_branch_by_name(self, branch_name):
        """
            Search for a branch object associated with a given branch name in the branch.txt file.

            Args:
                branch_name (str): The name of the branch to search for.

            Returns:
                Branch or None: The branch object if found, or None if not found.
            """
        # Search for the branch_obj associated with the branch_name in branch.txt
        with open("data/branch.txt", "r", encoding="utf-8") as branch_file:
            for branch in branch_file:
                branch = branch.strip("\n")
                branch_dict = eval(branch)
                if branch_dict["name"] == branch_name:
                    return Branch(branch_dict["name"], branch_dict["street"], branch_dict["suburb"],
                                  branch_dict["state"], branch_dict["postcode"], branch_dict["phone"],
                                  branch_dict["opening_hours"], branch_dict["pts"])
        return None

    def initialize_pts_with_time_slots(self, list_of_pts):
        """
            Initializes PT objects with time slots from a list of PT dictionaries.

            Args:
                list_of_pts (list): A list of dictionaries containing PT information.

            Returns:
                list: A list of initialized PT objects with time slots.
            """
        pt_objects = []
        for pt_dict in list_of_pts:
            pt = Pt(
                pt_dict['first_name'],
                pt_dict['last_name'],
                pt_dict['specialisation'],
                pt_dict['gender'],
                pt_dict['branch'],
                pt_dict['portfolio']
            )
            pt_objects.append(pt)
        return pt_objects

    def book_appointment(self, member_obj, pt_obj, branch_obj, reason):
        """
            Books an appointment for a member with a preferred personal trainer (PT) at a specific branch.

            Args:
                member_obj (Member): The member object requesting the appointment.
                pt_obj (Pt): The PT object selected by the member.
                branch_obj (Branch): The branch object where the appointment will take place.
                reason (str): The reason for the appointment.

            Returns:
                None
            """
        interface = UserInterface()

        # Ensure that the selected PT is available at the selected branch
        if pt_obj.branch != branch_obj.name:
            interface.print_message(f"{pt_obj.first_name} {pt_obj.last_name} is not available at this branch.")
            return

        # Calculate and display the dates for the next two weeks
        today = datetime.now()
        available_dates = [today + timedelta(days=i) for i in range(14)]

        interface.print_message("Available dates for the next two weeks:")
        for i, date in enumerate(available_dates, start=1):
            # append to date list
            interface.print_message(f"{i}. {date.strftime('%Y-%m-%d')} ({date.strftime('%A')})")

        while True:
            date_choice = interface.get_user_input(
                "Enter the number of the date you want to book (or 'Q' to cancel): ")

            if date_choice.upper() == "Q":
                return

            try:
                date_choice = int(date_choice)
                if 1 <= date_choice <= len(available_dates):
                    chosen_date = available_dates[date_choice - 1]
                    time_slots = pt_obj.generate_time_slots(chosen_date)

                    if not time_slots:
                        interface.print_message(
                            f"No available time slots for {chosen_date.strftime('%A')} at this branch.")
                    else:
                        # Display available time slots for the selected PT and date
                        interface.print_message(
                            f"Available time slots for {pt_obj.first_name} {pt_obj.last_name} on {chosen_date.strftime('%A, %Y-%m-%d')}:")
                        for i, time_slot in enumerate(time_slots, start=1):
                            interface.print_message(f"{i}. {time_slot}")

                        time_slot_choice = interface.get_user_input(
                            "Enter the number of the time slot you want to book (or 'Q' to cancel): ")

                        if time_slot_choice.upper() == "Q":
                            break

                        try:
                            time_slot_choice = int(time_slot_choice)
                            if 1 <= time_slot_choice <= len(time_slots):
                                # Book the appointment
                                selected_time_slot = time_slots[time_slot_choice - 1]

                                appointment = Appointment(member_obj.first_name,
                                                          None,
                                                          self.reasons[reason],
                                                          str(chosen_date.strftime(
                                                              '%Y-%m-%d')) + " " + selected_time_slot,
                                                          branch_obj.name,
                                                          pt_obj.first_name)
                                with open("data/appointment.txt", "a", encoding="utf-8") as user_file:
                                    user_file.write(f"{str(appointment.__dict__)}\n")
                                self.list_of_appointments.append(appointment)
                                interface.print_message("Appointment booked successfully!")
                                interface.print_message(f"Your appointment details are:{str(appointment.__dict__)}")
                                break
                            else:
                                interface.print_message("Invalid time slot choice. Please enter a valid number.")
                        except ValueError:
                            interface.print_message("Invalid input. Please enter a valid number or 'Q' to cancel.")
                else:
                    interface.print_message("Invalid date choice. Please enter a valid number.")
            except ValueError:
                interface.print_message("Invalid input. Please enter a valid number or 'Q' to cancel.")

    def show_appointments(self, member_obj):
        app_list = []
        interface = UserInterface()
        with open("data/appointment.txt", "r", encoding="utf-8") as app_file:
            for app in app_file:
                app = app.strip("\n")
                app_dict = eval(app)
                if app_dict["member_name"] == member_obj.first_name:
                    app_obj = Appointment(app_dict["member_name"], app_dict["member_status"], app_dict["reason"],
                                          app_dict["datetime"],
                                          app_dict["branch_name"], app_dict["pt_name"], app_dict["checkin"])

                    app_list.append(app_obj)

        interface.display_appointments(app_list)

    def check_in(self, member_obj):
        interface = UserInterface()
        app_list = []
        check_list = []
        with open("data/appointment.txt", "r", encoding="utf-8") as app_file:
            for appointment in app_file:
                appointment = appointment.strip("\n")
                app_dict = eval(appointment)
                if app_dict["member_name"] == member_obj.first_name:
                    app_obj = Appointment(app_dict["member_name"], app_dict["member_status"], app_dict["reason"],
                                          app_dict["datetime"], app_dict["branch_name"], app_dict["pt_name"],
                                          app_dict["checkin"])
                    app_list.append(app_obj)

        while True:
            system.show_appointments(member_obj)
            check_in_option = interface.get_user_input(
                "\nEnter the booking number you want to check-in or 'Q' to go back: ")
            if check_in_option == 'Q' or not check_in_option.isdigit():
                break  # Exit the loop if 'Q' is entered or an invalid input

            check_in_option = int(check_in_option) - 1  # Convert to zero-based index
            if 0 <= check_in_option < len(app_list):
                appointment_to_check_in = app_list[check_in_option]
                check_list.append(appointment_to_check_in)
                app_list.remove(appointment_to_check_in)  # Remove the selected appointment

                # Write the updated list back to the file
                book_dict = []
                for book_obj in app_list:
                    book_dict.append(book_obj.__dict__)
                with open("data/appointment.txt", "w", encoding="utf-8") as app_file:
                    app_file.writelines("\n".join(map(str, book_dict)))

                interface.display_check_in(check_list)

                interface.get_user_input("\nEnter 'Q' to go back: ")
                if check_in_option == 'Q':
                    break

    def cancel_booking(self, member_obj):
        interface = UserInterface()
        app_list = []

        with open("data/appointment.txt", "r", encoding="utf-8") as app_file:
            for appointment in app_file:
                appointment = appointment.strip("\n")
                app_dict = eval(appointment)
                if app_dict["member_name"] == member_obj.first_name:
                    app_obj = Appointment(app_dict["member_name"], app_dict["member_status"], app_dict["reason"],
                                          app_dict["datetime"], app_dict["branch_name"], app_dict["pt_name"],
                                          app_dict["checkin"])
                    app_list.append(app_obj)

        while True:
            system.show_appointments(member_obj)
            cancel_option = interface.get_user_input(
                "\nEnter the booking number you want to cancel or 'Q' to go back: ")
            if cancel_option == 'Q' or not cancel_option.isdigit():
                break  # Exit the loop if 'Q' is entered or an invalid input

            cancel_option = int(cancel_option) - 1  # Convert to zero-based index
            if 0 <= cancel_option < len(app_list):
                appointment_to_cancel = app_list[cancel_option]
                app_list.remove(appointment_to_cancel)  # Remove the selected appointment

                # Write the updated list back to the file
                book_dict = []
                for book_obj in app_list:
                    book_dict.append(book_obj.__dict__)
                with open("data/appointment.txt", "w", encoding="utf-8") as app_file:
                    app_file.writelines("\n".join(map(str, book_dict)))

                interface.print_message("\nYour booking has been successfully CANCELLED!")
            break

    def manage_appointments(self, member_obj):
        interface = UserInterface()
        interface.manage_appointment_menu()
        while True:
            interface.manage_appointment_menu()
            choice = interface.get_user_input("\nPlease enter your choice: ")
            if choice == "1":
                system.show_appointments(member_obj)

            elif choice == "2":
                system.check_in(member_obj)

            elif choice == "3":
                system.cancel_booking(member_obj)

            elif choice == "4":
                break

    def system_implementation(self):
        interface = UserInterface()
        system = MonashSportsSystem()
        while True:
            interface.main_menu()
            choice = interface.get_user_input("\nPlease enter your choice: ")
            if choice == "1":
                member_obj = system.login()
                if member_obj == None:
                    continue
                while True:
                    if member_obj is not None:
                        interface.login_menu(member_obj)
                        login_choice = interface.get_user_input("\nPlease enter your choice: ")
                        if login_choice == "1":
                            system.make_an_appointment(member_obj)

                        elif login_choice == "2":
                            system.manage_appointments(member_obj)

                        elif login_choice == "3":
                            interface.print_message("Successful logout!")
                            break

                        else:
                            interface.print_message("Invalid input. Please enter again.")


            elif choice == "2":
                break

            else:
                interface.print_message("Invalid input. Please try again.")

    def book_appointment_with_favorite_pt(self, member_obj, pt_obj, branch_obj):
        """
            Books an appointment for a member with a favorite personal trainer (PT) at a specific branch.

            Args:
                member_obj (Member): The member object requesting the appointment.
                pt_obj (Pt): The PT object selected by the member.
                branch_obj (Branch): The branch object where the appointment will take place.

            Returns:
                None
            """
        interface = UserInterface()

        # Ensure that the selected PT is available at the selected branch
        if pt_obj.branch != branch_obj.name:
            interface.print_message(f"{pt_obj.first_name} {pt_obj.last_name} is not available at this branch.")
            return

        # Calculate and display the dates for the next two weeks
        today = datetime.now()
        available_dates = [today + timedelta(days=i) for i in range(14)]

        interface.print_message("Available dates for the next two weeks:")
        for i, date in enumerate(available_dates, start=1):
            interface.print_message(f"{i}. {date.strftime('%Y-%m-%d')} ({date.strftime('%A')})")

        while True:
            date_choice = interface.get_user_input("Enter the number of the date you want to book (or 'Q' to cancel): ")

            if date_choice.upper() == "Q":
                return

            try:
                date_choice = int(date_choice)
                if 1 <= date_choice <= len(available_dates):
                    chosen_date = available_dates[date_choice - 1]
                    time_slots = pt_obj.generate_time_slots(chosen_date)

                    if not time_slots:
                        interface.print_message(
                            f"No available time slots for {chosen_date.strftime('%A')} at this branch.")
                    else:
                        # Display available time slots for the selected PT and date
                        interface.print_message(
                            f"Available time slots for {pt_obj.first_name} {pt_obj.last_name} on {chosen_date.strftime('%A, %Y-%m-%d')}:")
                        for i, time_slot in enumerate(time_slots, start=1):
                            interface.print_message(f"{i}. {time_slot}")

                        time_slot_choice = interface.get_user_input(
                            "Enter the number of the time slot you want to book (or 'Q' to cancel): ")

                        if time_slot_choice.upper() == "Q":
                            break

                        try:
                            time_slot_choice = int(time_slot_choice)
                            if 1 <= time_slot_choice <= len(time_slots):
                                # Book the appointment
                                selected_time_slot = time_slots[time_slot_choice - 1]

                                # Extract the reason (specialization) from pt_obj and remove "Specialisation :"
                                reason = pt_obj.get_specialisation().replace("Specialisation : ", "")

                                # Create a list for the reason
                                reason_list = [reason]

                                appointment = Appointment(member_obj.first_name,
                                                          None,
                                                          reason_list,
                                                          str(chosen_date.strftime(
                                                              '%Y-%m-%d')) + " " + selected_time_slot,
                                                          branch_obj.name,
                                                          pt_obj.first_name)
                                with open("data/appointment.txt", "a", encoding="utf-8") as user_file:
                                    user_file.write(f"{str(appointment.__dict__)}\n")
                                self.list_of_appointments.append(appointment)
                                interface.print_message("Appointment booked successfully!")
                                interface.print_message(f"Your appointment details are:{str(appointment.__dict__)}")
                                break
                            else:
                                interface.print_message("Invalid time slot choice. Please enter a valid number.")
                        except ValueError:
                            interface.print_message("Invalid input. Please enter a valid number or 'Q' to cancel.")
                else:
                    interface.print_message("Invalid date choice. Please enter a valid number.")
            except ValueError:
                interface.print_message("Invalid input. Please enter a valid number or 'Q' to cancel.")


system = MonashSportsSystem()
# system.add_favorite_branch()
# elif search_choice == "3":
# search_branch_by_postcode()
