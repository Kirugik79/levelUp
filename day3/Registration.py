

username = "Robert"

password = 456

attempt = 0

while attempt !=3:
    username = input ("Enter Username: ")

    if username != username:
        print ("Incorrect username")

    else:
        password = input ("Enter Password: ")
        if password == password:
            print ("Welcome " + username)
            break
        else:
            print ("Welcome " + username)
            attempt = attempt +1
            if attempt == 3:
                    print ("You have reached maximum login attempts")






