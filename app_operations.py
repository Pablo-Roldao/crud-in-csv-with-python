import datetime
import os

import crud_operations


def get_app_title():
    return """
        █▀█ █▀▀ █▀█ █▀█ █░░ █▀▀   █▀▀ █▀█ █░█ █▀▄
        █▀▀ ██▄ █▄█ █▀▀ █▄▄ ██▄   █▄▄ █▀▄ █▄█ █▄▀
        """


def get_menu_options():
    return """
    1. Display registered people;
    2. Create a new person;
    3. Delete a person;
    4. Update a person;
    5. Search people;
    6. Exit the program.
    """


def print_function_header(title):
    clear_screen()
    print(f"{str.upper(title)}\n")


def display_people(people):
    print(f"{'Id':5s}\t{'Name':30s}\t{'Birth date':10s}\t{'Gender':6s}\t{'Phone':20s}")
    if len(people) > 0:
        for person in people:
            print(
                f"{person.get('Id'):5s}\t{person.get('Name'):30s}\t{person.get('Birth date'):10s}\t{person.get('Gender')}\t{person.get('Phone'):20s}\n")
    else:
        print('\nNo people found...')


def create_person():
    print_function_header("Create person")

    name = input("Name: ")

    birth_date = input("Birth date (YYYY-MM-DD): ")
    valid_birth_date = validate_birth_date(birth_date)
    while not valid_birth_date:
        birth_date = input("Invalid birth date!\nBirth date (YYYY-MM-DD): ")
        valid_birth_date = validate_birth_date(birth_date)

    gender = input("Gender ('m' for Male - 'f' for Female - 'o' for Other): ")
    valid_gender = validate_gender(gender)
    while not valid_gender:
        gender = input("Invalid gender!\nGender ('m' for Male - 'f' for Female - 'o' for Other): ")
        valid_gender = validate_gender(gender)
    match gender:
        case 'm':
            gender = 'Male'
        case 'f':
            gender = 'Female'
        case _:
            gender = 'Other'

    phone = input("Phone: ")
    valid_phone = validate_phone(phone)
    while not valid_phone:
        phone = input("Invalid phone, must have more than 7 characters!\nPhone: ")
        valid_phone = validate_phone(phone)

    crud_operations.create_person(name, birth_date, gender, phone)


def delete_person():
    print_function_header("Delete person")

    try:
        id_to_delete = int(input("ID of the person to delete: "))
    except ValueError:
        print("Invalid ID!\n")
        return

    crud_operations.delete_person(id_to_delete)


def update_person():
    print_function_header("Update person")

    try:
        id_to_update = int(input("ID of the person to update: "))
    except ValueError:
        print("Invalid ID!\n")
        return

    name = input("Enter updated name: ")
    birth_date = input("Enter updated birth date (YYYY-MM-DD): ")
    valid_birth_date = validate_birth_date(birth_date)
    while not valid_birth_date:
        birth_date = input("Invalid birth date! Enter updated birth date (YYYY-MM-DD): ")
        valid_birth_date = validate_birth_date(birth_date)

    gender = input("Enter updated gender ('m' for Male - 'f' for Female - 'o' for Other): ")
    valid_gender = validate_gender(gender)
    while not valid_gender:
        gender = input("Invalid gender! Enter 'm' for Male, 'f' for Female, or 'o' for Other: ")
        valid_gender = validate_gender(gender)

    phone = input("Enter updated phone number: ")
    valid_phone = validate_phone(phone)
    while not valid_phone:
        phone = input("Invalid phone number! Please enter a valid phone number: ")
        valid_phone = validate_phone(phone)

    crud_operations.update_person(id_to_update, name, birth_date, gender, phone)


def search_people_by_name():
    print_function_header("Search people by name")

    search_term = input("Enter search term: ")

    crud_operations.search_people_by_name(search_term)

    return None


def validate_birth_date(birth_date):
    try:
        datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_gender(gender):
    return gender.lower() in ['m', 'f', 'o']


def validate_phone(phone):
    return len(phone) >= 7


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
