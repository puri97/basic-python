 known_users=["ALICE","LILY","BILL","LOONEY"]

while True:
    print("Hi I am Travis")
    name=input("Hi what is your name").strip().upper()
    if name in known_users:
        print("Welcome {}".format(name))
        remove=input("Would you like to be removed from the system?[y/n]").lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)
    else:
        print("Sorry we could not recognize you!")
