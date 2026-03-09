def add_user():
    name = input("Enter user name: ")

    with open("users.txt", "a") as f:
        f.write(name + "\n")


def show_users():
    try:
        with open("users.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No users yet.")


def menu():
    while True:
        print("\n1. Add user")
        print("2. Show users")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            break
        else:
            print("Invalid option")


menu()
