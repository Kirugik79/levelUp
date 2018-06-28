

class register:

    def __init__(self):
      self.dictionary = {}

    def registration(self):
        first_name = input ("Enter Your First Name: ")
        second_name = input ("Enter Your Second Name: ")
        email = input ("Enter Your Email: ")
        username = input ("Enter Your Username: ")
        password = input ("Enter Password: ")
        password2 = input ("Confirm Password: ")

        self.dictionary.update({username:[password, first_name, second_name, email]})
        print ("You haves successfully registered")

    def login (self):

        username = input ("Enter Username: ")

        if len(username) <= 0:
            print ("Username cannot be blank")
        else:
            password = input("Enter Password: ")
            if len(password) <= 0:
                print("Password cannot be blank")

                if user in self.dictionary:
                    if password == self.dictionary [username][0]:
                        print("login was successful")
                    else:
                        print("incorrect password")
                else:
                    print('unregistered user')

    def login_validation(username, password):
        if username in users:
            if password == users[username]["password"]:
                print("Welcome" + username)
                return True
        return False
























