import random
import datetime
import os

# Opens file containing reservation information
with open("reservation_21094230.txt", "r") as f:
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
                print("Saving details and closing program... ")
                with open("reservation_21094230.txt", "w") as rewrite:
                    rewrite.writelines(resDetails)
                print("Details saved successfully, program closed!")
                retry = False
            case _:
                print("Please try again with a valid response (1-6)\n")


def add_reservation():
    clash = []  # List showing all reservations occupying the same date and slot

    retry = True
    while retry:
        print(f"Adding new reservation... ")

        # Receive input for date and slot to reserve
        date = input("Enter date of reservation (YYYY-MM-DD): ")
        slot = input("Enter slot to reserve (1-4 only): ")

        # Displays people that made reservations for the chosen slot
        for reservation in resDetails:
            info = reservation.split("|")
            if info[0] == date and info[1][5] == slot:
                clash.append(info)
        print("\nThis slot was reserved by: ")
        for i in clash:
            print(i[2], end=", ")
        print("\n")

        # Checks if reservations slot is available or not
        if len(clash) >= 8:  # Slot full
            print("Slot can only accommodate 8 reservations, please choose a different slot \n")
            clash = []  # Resets the clash list
        else:  # Slot available
            print("Slot is available, you may start entering details")

            # Start taking reservation details
            name = input("Enter name for reservation: ")
            email = input("Enter email for reservation: ")
            phone = input("Enter phone number for reservation: ")
            pax = int(input("Enter number of pax (maximum 4): "))

            # Concatenating reservation info as a string
            entry1 = f"{date}|Slot {slot}|{name.upper()}|{email}|{phone}|{pax}\n"

            # Confirming reservation info
            print(f"Please reconfirm the reservation details: "
                  f"\n{entry1}")
            confirm = input("Enter Y to confirm reservation: ")
            if confirm.upper() == "Y":
                resDetails.append(entry1)
                resDetails.sort()
                print("Reservation added! Returning to main menu...\n")
                retry = False
            else:
                print("Reservation not confirmed, please try again")
    return resDetails


def cancel_reservation():
    print("doze nuts")


def edit_reservation():
    name = input("Enter your name for the reservation: ").upper()
    reservationFound = []
    reservationSelect = []
    numFound = []

    q = 0
    # to append new reservation into the list
    for reservations in reserve:
        q += 1
        # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
        reservations = reservations.split("|")
        # Is 2 because in the list 2 is the name of the reservation
        if reservations[2] == name:
            reservations.append(reservations)
            numFound.append[q]
    
    # To check if reservations found or not found
    # To further edit the reservation if reservation is found
    if len(reservationFound) >= 1:
        print(f"Reservation found.")
        # Enumerate() is used to access both the index and the item of a sequence simultaneously
        for i, index in enumerate(numFound):
            print(f"[{q + 1}] {reserve[index - 1]}")

        # To let user choose the reservation that they want to update by looking at the index
        numUpdate = int(input("Enter the number of the reservation to update: "))

        # To check errors
        # isnumeric() is used to check if the input consists of only numeric characters.
        while not numUpdate.isnumeric() or not (1 <= int(numUpdate) <= len(reservationFound)):
            print("Error, please input your number again.")
            numUpdate = int(input("Enter the number of the reservation to update: "))
    
        # To change the date of the reservations
        dateReplace = input("Enter the new date of the reservation (DD-MM-YYYY): ")
        dateNew = datetime.strptime(dateReplace, '%d-%m-%Y').date()
        dateToday = dateNew - dateNow
        day = dateToday.days
        
        # To let user change the date of reservations because the date chosen is less than 5 days
        while day < 5:
            print(f"Error! Please make reservations at least 5 days in advance.\n")
            dateReplace = input(f"Select a date (dd-mm-yyyy): ")
            dateNew = datetime.strptime(dateNew, '%d-%m-%Y').date()
            dateToday = dateNew - dateNow
            day = dateToday.days

        print(f"[1] 12.00pm - 2.00pm"
              f"\n[2] 02.00pm - 04.00pm"
              f"\n[3] 06.00pm - 08.00pm"
              f"\n[4] 08.00pm - 10.00pm")
    else:
        print(f"Reservation not found! Please check again")


def display_reservation():
    print("den nuts")


def meal_recommendation():
    print("now nuts")


main_program()
