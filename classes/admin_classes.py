# Module to store Privileges & Admin classes

from user_class import User

class Privileges:
    """Defines & shows privileges for Admin class"""

    def __init__(self):
        """Initializes attribute for Privileges Class"""
        self.privileges = ["can add post", "can delete post", 
                        "can edit post", "can ban user", "can approve user"]

    def show_privileges(self):
        """Prints list of admin privileges"""
        print(self.privileges)

class Admin(User):
    """Creates a specialized Admin type of User w/ unique privileges"""

    def __init__(self, first_name, last_name, age, location):
        """
        Initializes attributes of parent class
        Then initializes attributes specific to Admin
        """
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
