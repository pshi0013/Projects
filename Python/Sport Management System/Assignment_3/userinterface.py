import datetime
class UserInterface:
    def main_menu(self):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n   *** Main Menu ***    \n")
        print("1. Login")
        print("2. Quit")

    def login_menu(self, member_obj):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n     Hi, " + member_obj.first_name +"!")
        print("\n     *** Menu ***      \n")
        print("1. Make an appointment")
        print("2. Manage my appointments")
        print("3. Logout")

    def booking_menu(self):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Booking Menu *** \n")
        print("1. Search Branches")
        print("2. Show Favorite Branches")
        print("3. Show Favorite PTs")
        print("4. Back")

    def search_menu(self):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Search Branches *** \n")
        print("1. By Current Address")
        print("2. By Suburb")
        print("3. By Postcode")
        print("4. Back")

    def branch_option(self):
        print("\nOptions: ")
        print("1. Add this branch as favorite")
        print("2. View PT's information and available time")
        print("3. Back")

    def pt_option(self):
        print("\nOptions: ")
        print("1. Add this PT as favorite")
        print("2. Book an appointment")
        print("3. Back")

    def get_user_input(self, message):
        user_input = input(message).strip()
        return user_input

    def display_address(self, object):
        address = object.street + ", " + object.suburb + ", " + object.state + ", " + object.postcode
        print("Address : " + address)

    def display_opening_hours(self, opening_hours, day_of_week):
        print("\nOpening Hours:")

        for i in range(7):
            index = (day_of_week + i) % 7
            if i == 0:
                print(f"[{opening_hours[index]}]")
            else:
                print(f"{opening_hours[index]}")

    def display_pts(self, list_of_pts):
        sorted_list_of_pts = sorted(list_of_pts)
        #print(sorted_data)

        print("\nPTs : ")
        for i in range(len(sorted_list_of_pts)):
            print(str(i+1) + "." + sorted_list_of_pts[i][0] + " " + sorted_list_of_pts[i][1])

    def display_branch(self, branch_obj):
        interface = UserInterface()
        print("\n" + branch_obj.get_name())
        interface.display_address(branch_obj)
        print(branch_obj.get_phone())

        # The current day will be displayed on top
        current_date = datetime.datetime.now()
        day_of_week = current_date.weekday()
        opening_hours = eval(branch_obj.get_opening_hours())
        interface.display_opening_hours(opening_hours, day_of_week)
        pts = eval(branch_obj.get_list_of_pts())
        interface.display_pts(pts)

    def display_favorite_branch(self, member_obj):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Favorite Branches *** \n")
        with open("data/user.txt", "r", encoding="utf-8") as user_file:
            for user in user_file:
                user = user.strip("\n")
                user_dict = eval(user)
                if user_dict['email'] == member_obj.email:
                    member_obj.set_favorite_branch(user_dict['favorite_branch'])

        branch_list = member_obj.favorite_branch
        if len(branch_list) == 0:
            print("No favorite branch.")
        else:
            for i in range(1, len(branch_list) + 1):
                print(f"{i}. {branch_list[-i]}")

    def favorite_branch_option(self):
        print("\nOptions: ")
        print("1. Book an appointment")
        print("2. Delete a favorite branch")
        print("3. Back")

    def print_message(self, message):
        print(message)

    def display_favorite_pt(self, member_obj):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Favorite PTs *** \n")
        with open("data/user.txt", "r", encoding="utf-8") as user_file:
            for user in user_file:
                user = user.strip("\n")
                user_dict = eval(user)
                if user_dict['email'] == member_obj.email:
                    member_obj.set_favorite_pt(user_dict['favorite_pt'])

        pt_list = member_obj.favorite_pt
        if len(pt_list) == 0:
            print("No favorite PT.")
        else:
            for i in range(1, len(pt_list) + 1):
                print(f"{i}. {pt_list[-i]}")

    def favorite_pt_option(self):
        print("\nOptions: ")
        print("1. Book an appointment")
        print("2. Delete a favorite PT")
        print("3. Back")


    def display_appointment_reason(self):
        print("\nPlease select your desired reason \n"
              "1. Reduce Weight Appointment \n"
              "2. General Health Appointment \n"
              "3. Recovery Appointment \n")

    def display_appointments(self, app_list):
        for app_obj in app_list:
            print("\n" + str((app_list.index(app_obj)+1))+".")
            print(app_obj.get_branch_name())
            print(app_obj.get_pt_name())
            print(app_obj.get_datetime())
            print("Reason : " + app_obj.reason[0])
            #print(app_obj.get_reason())

    def manage_appointment_menu(self):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Management Menu *** \n")
        print("1. Show My Booking")
        print("2. Check-in Booking")
        print("3. Cancel Booking")
        print("4. Back")

    def bookings_option(self):
        print("\nManagement options: \n")
        print("1. Show My Booking")
        print("2. Check-in Booking")
        print("3. Cancel Booking")
        print("4. Back")

    def display_show_my_booking(self, app_list):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** My Bookings *** \n")
        print("Your bookings:")
        for app_obj in app_list:
            print("\n" + str((app_list.index(app_obj)+1))+". " +
                  app_obj.get_datetime() + ' @ ' + app_obj.get_branch_name())
            print(app_obj.get_pt_name())

    def display_check_in(self, check_list):
        print("\n===========================")
        print("      Monash Sports        ")
        print("===========================")
        print("\n  *** Booking Check-in *** \n")
        print("Check-in Successful!")
        for app_obj in check_list:
            print(app_obj.member_name)
            print(app_obj.datetime)
            print(app_obj.pt_name)
            print(app_obj.branch_name)

a = UserInterface()
#a.main_menu()
#a.login_menu()
#a.booking_menu()