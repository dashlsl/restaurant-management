import random
import datetime
import os


# Opens file containing reservation information
with open("reservation_21094230.txt", "r+") as f:
    contents = f.readlines()

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
        match selection:
            case 1:
                addReservation()
            case 6:
                print("Program closed")
                retry = False


def addReservation():
    print("deeznuts")


def cancelReservation():
    print("dozenuts")


def editReservation():
    print("derenuts")


def displayReservation():
    print("dennuts")


def mealRecommendation():
    print("nownuts")


mainProgram()