import hashlib


users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register function
def register():
    print("\n--- REGISTER ---")
    username = input("Enter username: ")

    if username in users_db:
        print("Username already exists!\n")
        return

    password = input("Enter password: ")

    hashed_pw = hash_password(password)
    users_db[username] = hashed_pw

    print("Account created successfully!\n")

def login():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users_db:
        print("User not found!\n")
        return

    hashed_pw = hash_password(password)

    if users_db[username] == hashed_pw:
        print("Login successful! Welcome,", username, "\n")
    else:
        print("Incorrect password!\n")

def main():
    while True:
        print("====== SECURE LOGIN SYSTEM ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()