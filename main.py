users = {}

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Signup
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            print("User already exists")
        else:
            users[username] = password
            print("Signup successful")

    # Login
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful ✅")
        else:
            print("Invalid details ❌")

    # Exit
    elif choice == "3":
        print("Bye 👋")
        break

    else:
        print("Wrong choice")
