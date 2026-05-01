def get_credentials():
    while True:
        email = input("Enter your email address: ")
        if "@" in email and ".com" in email:
            print("Email received successfully.")
            break
        else:
            print("Invalid email! Please enter a valid email address.")

    while True:
        password = input("Enter your password: ")
        if len(password) >= 6:
            print("Password saved successfully.")
            break
        else:
            print("Password must be at least 6 characters long. Try again!")

    return email, password

def register(email, password):
    # 'with' ensures the file is closed automatically
    with open("database.txt", "a", encoding="utf-8") as file:
        file.write(f"{email}:{password}\n")
    print("Registration complete.")

def login(email, password):
    try:
        with open("database.txt", "r", encoding="utf-8") as file:
            users = file.read()
            if f"{email}:{password}" in users:
                return True
            else:
                return False
    except FileNotFoundError:
        return False

def main():
    print("--- Authentication System ---")
    print("1- Register\n2- Login")
    
    try:
        choice = int(input("Your choice: "))
        email, password = get_credentials()

        if choice == 1:
            register(email, password)
        elif choice == 2:
            if login(email, password):
                print("Login successful! Welcome.")
            else:
                print("Login failed! Invalid email or password.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a number (1 or 2).")
