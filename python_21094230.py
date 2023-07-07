import random
import datetime
import os

# Opens file containing reservation information
with open("reservation_21094230.txt", "r+") as f:
    resDetails = f.readlines()

# Opens file containing list of menu items
with open("menuItems_21094230.txt", "r") as g:
    menuItems = g.readlines()


def main_program():
    retry = True
    while retry:
        print(f"Charming Thyme Trattoria Reservation Management Program"
              f"\n[1] Add reservation"
              f"\n[2] Cancel reservation"
              f"\n[3] Update/edit reservation"
              f"\n[4] Display reservation"
              f"\n[5] Generate meal recommendation"
              f"\n[6] Exit")
        selection = int(input("Enter your selection: "))
        print("")
        match selection:
            case 1:
                add_reservation()
            case 2:
                cancel_reservation()
            case 3:
                edit_reservation()
            case 4:
                display_reservation()
            case 5:
                meal_recommendation()
            case 6:
                print("Program closed")
                retry = False
            case _:
                print("Please try again with a valid response (1-6)\n")


def add_reservation():
    retry = True
    while retry:
        print(f"Adding new reservation... ")

        # Inputting reservation information
        date = input("Enter date of reservation (YYYY-MM-DD): ")
        slot = int(input("Enter slot to reserve (1-4 only): "))
        name = input("Enter name for reservation: ")
        email = input("Enter email for reservation: ")
        phone = input("Enter phone number for reservation: ")
        pax = int(input("Enter number of pax (maximum 4): "))

        # Concatenating reservation details as a string
        entry1 = f"{date}|Slot {slot}|{name}|{email}|{phone}|{pax}"

        # Confirming reservation details
        print(f"Please reconfirm the reservation details: "
              f"\n{entry1}"
              f"\n")
        confirm = input("Enter Y to confirm reservation: ")
        if confirm.upper() == "Y":
            resDetails.append(entry1)
            """with open("reservation_21094230.txt", "a") as f:
                f.write(f"{entry1}\n")"""
            print("Reservation added! Returning to main menu...\n")
            retry = False
        else:
            print("Reservation not confirmed, please try again")

    return


def cancel_reservation():
    print("doze nuts")


def edit_reservation():
    print("dere nuts")


def display_reservation():
    print("den nuts")


def meal_recommendation():
    print("now nuts")


main_program()
