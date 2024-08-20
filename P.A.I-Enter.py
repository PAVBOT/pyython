import os
import random
import shutil
import json
import secrets
import string

# Directory for storing passwords and locations
PASSWORDS_DIR = 'D:\\Automate\\Password'
LOCATIONS_FILE = 'locations.json'
PASSWORDS_FILE = os.path.join(PASSWORDS_DIR, 'passwords.json')

# Ensure the directory for passwords exists
if not os.path.exists(PASSWORDS_DIR):
    os.makedirs(PASSWORDS_DIR)

# Load existing data
def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return {}

# Save data to file
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

passwords = load_data(PASSWORDS_FILE)
locations = load_data(LOCATIONS_FILE)

def sort_files():
    path = input("Enter the directory path: ")
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                ext = file.split('.')[-1]
                ext_dir = os.path.join(path, ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.move(os.path.join(root, file), os.path.join(ext_dir, file))
        print("Files sorted by extension.")
    else:
        print("Path does not exist.")

def delete_random_files():
    path = input("Enter the directory path: ")
    if os.path.exists(path):
        files = [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]
        random_file = random.choice(files)
        confirm = input(f"Do you want to delete {random_file}? (yes/no): ")
        if confirm.lower() == 'yes':
            os.remove(random_file)
            print(f"{random_file} deleted.")
        else:
            print("File not deleted.")
    else:
        print("Path does not exist.")

def save_password():
    website = input("Enter the website name: ")
    password = input("Enter the password: ")
    passwords[website] = password
    save_data(PASSWORDS_FILE, passwords)
    print("Password saved.")

def get_password():
    website = input("Enter the website name: ")
    if website in passwords:
        print(f"The password for {website} is {passwords[website]}")
    else:
        print("No password found for this website.")

def delete_password():
    website = input("Enter the website name: ")
    if website in passwords:
        del passwords[website]
        save_data(PASSWORDS_FILE, passwords)
        print("Password deleted.")
    else:
        print("No password found for this website.")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if length_ok and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length_ok and (has_upper or has_lower) and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

def open_text_file():
    filename = input("Enter the filename (with .txt extension): ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f.read())
    else:
        print("File does not exist.")

def save_text():
    directory = 'D:\\Automate\\Text'
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it does not exist

    title = input("Enter the title for the text: ")
    text = input("Enter the text: ")
    file_path = os.path.join(directory, f'{title}.txt')  # Save in the specified directory
    with open(file_path, 'w') as f:
        f.write(text)
    print(f"Text saved at {file_path}")

def save_location():
    item = input("Enter the item name: ")
    location = input(f"Enter the location for {item}: ")
    locations[item] = location
    save_data(LOCATIONS_FILE, locations)
    print("Location saved.")

def get_location():
    item = input("Enter the item name: ")
    if item in locations:
        print(f"The last location of {item} is {locations[item]}")
    else:
        print("No location found for this item.")

def update_location():
    item = input("Enter the item name: ")
    if item in locations:
        location = input(f"Enter the new location for {item}: ")
        locations[item] = location
        save_data(LOCATIONS_FILE, locations)
        print("Location updated.")
    else:
        print("No location found for this item.")

def main():
    while True:
        print("\nChoose a task number:")
        print("1: Delete Password")
        print("2: Save Password")
        print("3: Get Password")
        print("4: Generate Password")
        print("5: Check Password Strength")
        print("6: Sort Files")
        print("7: Delete Random File")
        print("8: Save Custom Text")
        print("9: Open .txt File")
        print("10: Save Item Location")
        print("11: Get Item Location")
        print("12: Update Item Location")
        print("0: Exit")
        
        choice = input("Enter task number: ")

        if choice == '1':
            delete_password()
        elif choice == '2':
            save_password()
        elif choice == '3':
            get_password()
        elif choice == '4':
            length = int(input("Enter the length of the password: "))
            print(f"Generated password: {generate_password(length)}")
        elif choice == '5':
            password = input("Enter the password to check: ")
            print(f"Password strength: {check_password_strength(password)}")
        elif choice == '6':
            sort_files()
        elif choice == '7':
            delete_random_files()
        elif choice == '8':
            save_text()
        elif choice == '9':
            open_text_file()
        elif choice == '10':
            save_location()
        elif choice == '11':
            get_location()
        elif choice == '12':
            update_location()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid task number.")

if __name__ == "__main__":
    main()
