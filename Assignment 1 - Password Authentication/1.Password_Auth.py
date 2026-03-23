# Password Authentication – All in One File

import hashlib

users = {}  # stores username: hashed_password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users[username] = hash_password(password)
    print(f"User {username} registered successfully!")

def authenticate(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login successful ✅")
    else:
        print("Login failed ❌")

def main():
    while True:
        choice = input("Do you want to (1) Register, (2) Login, or (3) Exit? ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticate(username, password)
        elif choice == '3':
            print("Exiting…")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()