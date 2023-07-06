import random
import datetime
import os


# Opens file containing reservation information
with open("reservation_21094230.txt", "r+") as f:
    resDetails = f.readlines()

# Opens file containing list of menu items
with open("menuItems_21094230.txt", "r") as g:
    menuItems = g.readlines()


def mainProgram():
    retry = True
    while retry == True:
        print(f"[1] Add reservation"
              f"\n[2] Cancel reservation"
              f"\n[3] Update/edit reservation"
              f"\n[4] Display reservation"
              f"\n[5] Generate meal recommendation"
              f"\n[6] Exit")
        selection = int(input("Enter your selection: "))
        print("")
        match selection:
            case 1:
                addReservation()
            case 6:
                print("Program closed")
                retry = False


def addReservation():
    retry = True
    while retry == True:
        print(f"Adding new reservation... ")
        date = input("Enter date of reservation (YYYY-MM-DD): ")
        slot = int(input("Enter slot to reserve (1-4): "))
        name = input("Enter name for reservation: ")
        email = input("Enter email for reservation: ")
        phone = input("Enter phone number for reservation: ")
        pax = int(input("Enter number of pax (maximum 4): "))
        entry1 = f"{date}|Slot {slot}|{name}|{email}|{phone}|{pax}"
        resDetails.append(entry1)
        """with open("reservation_21094230.txt", "a") as f:
            f.write(f"{entry1}\n")"""
        retry = False
    return



def cancelReservation():
    print("dozenuts")


def editReservation():
    print("derenuts")


def displayReservation():
    print("dennuts")


def mealRecommendation():
    print("nownuts")


mainProgram()