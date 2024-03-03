import os

import app_operations
import crud_operations


def main():
    app_operations.clear_screen()
    print(app_operations.get_app_title())
    print(app_operations.get_menu_options())
    try:
        option = int(input("Choose an option: "))
        print()

        match option:
            case 1:
                app_operations.display_people(crud_operations.get_people_from_file())
            case 2:
                app_operations.create_person()
            case 3:
                app_operations.delete_person()
            case 4:
                app_operations.update_person()
            case 5:
                app_operations.search_people_by_name()
            case 6:
                print("Exiting...\n")
                return
            case _:
                print("Invalid option!\n")
    except ValueError:
        print("\nInvalid option!\n")

    input("\nPress enter to return to the main menu...")
    main()


if __name__ == "__main__":
    main()
