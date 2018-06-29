


class register:

    def __init__(self):
      self.dictionary = {}

      self.usercomments = []

    def registration(self):
        first_name = input ("Enter Your First Name: ")
        second_name = input ("Enter Your Second Name: ")
        email = input ("Enter Your Email: ")
        username = input ("Enter Yo ur Username: ")
        password = input ("Enter Password: ")
        password2 = input ("Confirm Password: ")

        self.dictionary.update({username:[password, first_name, second_name, email]})
        print ("Account successfully created for " + username)

    def login (self):

        username = input ("Enter Username: ")
        password = input("Enter Password: ")
        if len(username) <= 0:
            print ("Username cannot be blank")
        else:
            if len(password) <= 0:
                print("Password cannot be blank")
            else:
                if username in self.dictionary:
                    if password == self.dictionary [username][0]:
                        print("Login successful")
                    else:
                        print("incorrect password")
                else:
                    print("ERROR: Unregistered User, Please register to login")

    def login_validation(username, password):
        if username in self.dictionary:
            if password == self.dictionary[username]["password"]:
                print("Login successful, welcome" + username)

            else:
                print ("Incorrect password")

        else:
            print ("User not registered")

    def postcomment(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in self.dictionary:

            if password != self.dictionary [username][0]:
                print ("Incorect user password")
            else:
                self.usercomments.append (input ("Write a comment: "))

        else:
            print ("You have not registered. Please register to post comments")


    def fetchallcomments(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in self.dictionary:
            if password == self.dictionary [username][0]:
                  print (self.usercomments)
            else:
               print ("Incorect password")

        else:
            print ("You cannot fetch comments when not registered")
























