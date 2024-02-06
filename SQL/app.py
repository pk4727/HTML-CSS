import sys
from dbhelper import DBhelper

class database:
    def __init__(self):
        # connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
                            1. enter to register
                            2. enter to login
                            3. anything else to leave                           
                            """)
        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(1000)