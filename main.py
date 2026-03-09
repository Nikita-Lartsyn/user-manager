def add_user():
    name = input("Enter user name: ").strip()

    if not name:
        print("Name cannot be empty")
        return

    with open("users.txt", "a") as f:
        f.write(name + "\n")


def show_users():
    try:
        with open("users.txt", "r") as f:
            for i, line in enumerate(f, start=1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("\nNo users yet.")


def delete_user():
    with open("users.txt", "r") as f:
        users = f.readlines()

        for i, user in enumerate(users, start=1):
            print(f"{i}. {user.strip()}")

    try:
        index = int(input("\nWho do you want to delete? ")) - 1
    except ValueError:
        print("\nThis isn't a number")
        return

    if 0 <= index < len(users):
        del users[index]
    else:
        print("\nInvalid user number")
        return

    with open("users.txt", "w") as f:
        f.writelines(users)
    print("\nUser deleted")


def menu():
    while True:
        print("\n1. Add user")
        print("2. Show users")
        print("3. Delete user")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            break
        else:
            print("Invalid option")


menu()
