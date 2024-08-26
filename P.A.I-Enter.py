import os
import random
import shutil
import json
import hashlib
import platform
import requests
import datetime
from googletrans import Translator
from plyer import notification
import time

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

# Translation function
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# New Feature: Translation Interface
def translate_to():
    text = input("Enter the text to translate: ")
    print("Choose a target language:")
    print("1: Oriya")
    print("2: Hindi")
    print("3: English")
    print("4: Korean")
    print("5: Russian")
    print("6: Spanish")
    print("7: French")
    print("8: German")
    print("9: Japanese")
    print("10: Chinese (Simplified)")
    print("11: Italian")
    print("12: Portuguese")
    print("13: Arabic")
    print("14: Bengali")
    print("15: Tamil")
    language_choice = input("Enter choice: ")

    language_mapping = {
        '1': 'or',  # Oriya
        '2': 'hi',  # Hindi
        '3': 'en',  # English
        '4': 'ko',  # Korean
        '5': 'ru',  # Russian
        '6': 'es',  # Spanish
        '7': 'fr',  # French
        '8': 'de',  # German
        '9': 'ja',  # Japanese
        '10': 'zh-cn',  # Chinese (Simplified)
        '11': 'it',  # Italian
        '12': 'pt',  # Portuguese
        '13': 'ar',  # Arabic
        '14': 'bn',  # Bengali
        '15': 'ta'   # Tamil
    }

    target_language = language_mapping.get(language_choice)
    if target_language:
        translated_text = translate_text(text, target_language)
        print(f"Translated Text: {translated_text}")
    else:
        print("Invalid language choice.")

# Reminder handling functions
def set_reminder():
    reminders = load_data('reminders.json')
    title = input("Enter the reminder title: ")
    message = input("Enter the reminder message: ")
    time_str = input("Enter the reminder time (YYYY-MM-DD HH:MM:SS): ")
    
    try:
        reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        reminders[title] = {
            "message": message,
            "time": reminder_time.isoformat()
        }
        save_data('reminders.json', reminders)
        print("Reminder set successfully.")
    except ValueError:
        print("Invalid time format. Please use YYYY-MM-DD HH:MM:SS.")

def check_reminders():
    now = datetime.datetime.now()
    reminders = load_data('reminders.json')
    
    # Create a list of keys to iterate over
    reminder_keys = list(reminders.keys())
    
    for title in reminder_keys:
        reminder = reminders[title]
        reminder_time = datetime.datetime.fromisoformat(reminder['time'])
        if now >= reminder_time:
            notification.notify(
                title=title,
                message=reminder['message'],
                timeout=10
            )
            # Remove the reminder after notifying
            del reminders[title]
            save_data('reminders.json', reminders)


# Existing functions...

# Main function
def main():
    while True:
        print("\nChoose a task number:")
        print("1: List Saved Passwords")
        print("2: Search Password")
        print("3: Generate Random Text")
        print("4: Save Encrypted Password")
        print("5: Get File Size")
        print("6: Check File Existence")
        print("7: Rename File")
        print("8: Move File")
        print("9: Copy File")
        print("10: Backup Data")
        print("11: Show Recent Activity")
        print("12: Set Reminder")
        print("13: Check File Permissions")
        print("14: Get File Creation Date")
        print("15: List Files in Directory")
        print("16: Search Text in File")
        print("17: Count Words in File")
        print("18: Calculate File Checksum")
        print("19: Display System Info")
        print("20: Download File from URL")
        print("21: Log Activity")
        print("22: Set User Preferences")
        print("23: Send Notification")
        print("24: Generate Report")
        print("25: Translate Text")
        print("0: Exit")
        
        choice = input("Enter task number: ")

        if choice == '1':
            list_saved_passwords()
        elif choice == '2':
            search_password()
        elif choice == '3':
            length = int(input("Enter the number of words: "))
            print(f"Generated text: {generate_random_text(length)}")
        elif choice == '4':
            save_encrypted_password()
        elif choice == '5':
            get_file_size()
        elif choice == '6':
            check_file_existence()
        elif choice == '7':
            rename_file()
        elif choice == '8':
            move_file()
        elif choice == '9':
            copy_file()
        elif choice == '10':
            backup_data()
        elif choice == '11':
            show_recent_activity()
        elif choice == '12':
            set_reminder()
        elif choice == '13':
            check_file_permissions()
        elif choice == '14':
            get_file_creation_date()
        elif choice == '15':
            list_files_in_directory()
        elif choice == '16':
            search_text_in_file()
        elif choice == '17':
            count_words_in_file()
        elif choice == '18':
            calculate_file_checksum()
        elif choice == '19':
            display_system_info()
        elif choice == '20':
            download_file_from_url()
        elif choice == '21':
            action = input("Enter action to log: ")
            log_activity(action)
        elif choice == '22':
            set_user_preferences()
        elif choice == '23':
            send_notification()
        elif choice == '24':
            generate_report()
        elif choice == '25':
            translate_to()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
        
        # Check for reminders
        check_reminders()
        # Sleep for a while to avoid high CPU usage
        time.sleep(60)

if __name__ == "__main__":
    main()
