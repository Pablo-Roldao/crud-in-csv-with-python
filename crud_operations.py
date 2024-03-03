import csv
import random

import app_operations

FILE_NAME = "people.csv"
PERSON_HEADER = ["Id", "Name", "Birth date", "Gender", "Phone"]


def get_people_from_file():
    with open(FILE_NAME, "r") as file:
        people = []
        file.readline()
        for line in file:
            values = line.strip().split(",")
            person = dict(zip(PERSON_HEADER, values))
            people.append(person)
        return people
        pass


def save_people_to_file(people):
    with open(FILE_NAME, "w") as file:
        writer = csv.DictWriter(file, fieldnames=PERSON_HEADER)
        writer.writeheader()
        writer.writerows(people)


def create_person(name, birth_date, gender, phone):
    person = dict(zip(PERSON_HEADER, [get_free_id(), name, birth_date, gender, phone]))
    people = get_people_from_file()
    people.append(person)
    save_people_to_file(people)


def delete_person(id_to_delete):
    people = get_people_from_file()
    found = False

    for person in people:
        if int(person["Id"]) == id_to_delete:
            people.remove(person)
            found = True
            break

    if not found:
        print(f"Person with ID {id_to_delete} not found!\n")
        return

    save_people_to_file(people)
    print(f"Person with ID {id_to_delete} has been deleted.\n")


def update_person(id_to_update, name, birth_date, gender, phone):
    people = get_people_from_file()

    found = False
    for person in people:
        if int(person["Id"]) == id_to_update:
            found = True
            break

    if not found:
        print(f"Person with ID {id_to_update} not found!\n")
        return

    for person in people:
        if int(person["Id"]) == id_to_update:
            person["Name"] = name
            person["Birth date"] = birth_date
            person["Gender"] = gender
            person["Phone"] = phone
            break

    save_people_to_file(people)
    print(f"Person with ID {id_to_update} has been updated.\n")


def search_people_by_name(search_term):
    app_operations.print_function_header("Search people")

    people = get_people_from_file()
    found_people = [person for person in people if search_term.lower() in person["Name"].lower()]

    if found_people:
        print("Matching people:\n")
        app_operations.display_people(found_people)
    else:
        print("No matching people found.")

    return None


def get_free_id():
    ids = [people.get('Id') for people in get_people_from_file()]
    random_id = random.randint(1, 9999)
    while random_id in ids:
        random_id = random.randint(1, 9999)
    return random_id
