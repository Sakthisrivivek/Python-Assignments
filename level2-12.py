def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for i in range(3):
        retype_password = input("Re-type password: ")
        if retype_password == password:
            print("Login successful!")
            return
        else:
            print("Password incorrect. Please try again.")
    
    print("Too many incorrect attempts. Please try again later.")

def main():
    print("Welcome to the login page.")
    login()

if __name__ == "__main__":
    main()
