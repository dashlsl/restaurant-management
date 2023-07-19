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


########################################################################################################

def add_reservation():
    print(f"Adding new reservation... "
          f"\nNote: Reservation must be at least 5 days in advance")

    retry = True
    while retry:
        # Receives and checks date input
        date_now = datetime.datetime.now().date()
        date_res = ""
        while date_res == "":
            try:
                date_res = input("Enter date of reservation (YYYY-MM-DD): ")
                if date_res != datetime.datetime.strptime(date_res, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
            except ValueError:
                print("\n"
                      "Invalid date format, please try again")
                date_res = ""
            else:
                date_res = datetime.datetime.strptime(date_res, "%Y-%m-%d").date()
                days_between = date_res - date_now
                # Checks whether reservation is at least 5 days in advance
                if days_between.days < 5:
                    print(f"\n"
                          f"Reservation must be at least 5 days in advance, please try again")
                    date_res = ""
                else:
                    print("")
                    confirm_date = input(f"Enter 'Y' to confirm the date {date_res}: ").upper()
                    if confirm_date == "Y":
                        print("\n"
                              "Reservation date set!")
                    else:
                        print("\n"
                              "Choosing a different date...")
                        date_res = ""

        # Receives and checks slot input
        slot = 0
        while slot == 0:
            print("[1] 12:00pm - 02:00pm"
                  "\n[2] 02:00pm - 04:00pm"
                  "\n[3] 06:00pm - 08:00pm"
                  "\n[4] 08:00pm - 10:00pm")
            slot = int(input("Enter slot to reserve (1-4 only): "))
            if slot < 1 or slot > 4:
                print("\nInvalid slot, please try again")
                slot = int(input("Enter slot to reserve (1-4 only): "))

            # Displays people that made reservations for the chosen slot
            clash = []
            for reservation in resDetails:
                info = reservation.split("|")
                if info[0] == str(date_res) and info[1][5] == str(slot):
                    clash.append(info)
            print("\n"
                  "This slot was reserved by: ")
            if not clash:
                print("N/A")
            else:
                for i in clash:
                    print(i[2], end=", ")
                print(" ")

            # Checks if reservation slot is available or not
            if len(clash) >= 8:  # Slot full
                print("Slot can only accommodate 8 reservations, please choose a different slot"
                      "\n[1] Change date"
                      "\n[2] Change slot")
                clash.clear()  # Resets the clash list
                changer = 0
                while changer == 0:
                    changer = int(input("Enter your selection: "))
                    if changer == 1:
                        print("\n"
                              "Choosing a different date...")
                        retry = True  # Re-trigger the loops to enter date and slot again
                    elif changer == 2:
                        print("\n"
                              "Choosing a different slot...")
                        slot = 0
                    else:
                        print("\n"
                              "Invalid selection, please try again")
                        changer = 0
            else:  # Slot available
                print("Slot is available, you may start entering details"
                      "\n")

                # Start taking reservation details
                name = input("Enter name for reservation: ").upper()
                email = input("Enter email for reservation: ")
                phone = input("Enter phone number for reservation: ")
                pax = 0
                while pax == 0:
                    pax = int(input("Enter number of pax (maximum 4): "))
                    if pax < 1 or pax > 4:
                        print("\nInvalid number of pax, please try again")
                        pax = int(input("Enter number of pax (maximum 4): "))

                # Concatenating reservation info as a string
                entry1 = f"{date_res}|Slot {slot}|{name}|{email}|{phone}|{pax}\n"

                # Confirming reservation info
                print(f"Please reconfirm the reservation details: "
                      f"\n{entry1}")
                confirm = input("Enter Y to confirm reservation: ")
                if confirm.upper() == "Y":
                    resDetails.append(entry1)
                    resDetails.sort()
                    print("Reservation added!"
                          "\n")
                else:
                    print("Reservation not confirmed, please try again"
                          "\n")

                # Checks if user wants to add another reservation
                print("[1] Add another reservation"
                      "\n[2] Return to main menu")
                new_res = 0
                while new_res == 0:
                    new_res = int(input("Enter your selection: "))
                    if new_res == 1:
                        print("Adding new reservation...")
                        retry = True
                    elif new_res == 2:
                        print("\n"
                              "Returning to main menu...")
                        retry = False
                    else:
                        print("\n"
                              "Invalid selection, please try again")
                        new_res = 0
    print("-----------------------------------------------------------------------------------------------------------")
    return resDetails


########################################################################################################

def cancel_reservation():
    try:
        loop=True
        while loop:
            print("**Cancel Reservation**")
            num=int(input("How many reservation do you want to delete?: "))
            num_result = []
            q = 0

            if num==1:
                name = input("Enter the name the reservation is under:").upper()
                # Search file for reservation with that name
                # to append new reservation into the list

                for reservations in resDetails:
                    # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
                    temp = reservations.split("|")
                    # Is 2 because in the list 2 is the name of the reservation
                    if temp[2] == name:
                        num_result.append(q)
                    q += 1

                # If search found exactly one result
                if len(num_result) == 1:
                    print("Search Found!")
                    # Display Search
                    for i, index in enumerate(num_result):
                        print(f"[{1}] {resDetails[index]}")
                    # Ask for confirmation
                    confirm = input("Are you sure you want to delete this reservation? [Y/N]").upper()
                    if confirm == "Y":
                        # Delete Line which matches
                        del resDetails[num_result[0]]
                        print("Reservation Deleted.\n")


                    elif confirm == "N":
                        print("Reservation Not Deleted.\n")

                    else:
                        print("Invalid Input\n")

                # If search found more than one results
                elif len(num_result) > 1:
                    print(str(len(num_result))+" Results Were Found!")
                    # Display Search
                    count = 1
                    for i, index in enumerate(num_result):
                        print("["+str(count)+"] "+f" {resDetails[index]}")
                        count += 1

                    # Ask which reservation to delete
                    choice = int(input("Which reservation would you like to delete?: "))

                    # Ask for confirmation
                    confirm = input("Are you sure you want to delete this reservation? [Y/N]").upper()
                    if confirm == "Y":
                        # Delete Line which matches
                        del resDetails[num_result[choice-1]]
                        print("Reservation Deleted.\n")

                    elif confirm == "N":
                        print("Reservation Not Deleted.\n")

                    else:
                        print("Invalid Input\n")

                else:
                    print("No Result were found\n")
                loop=False

            # If user wants to delete more than 1 reservation
            elif num>1:
                name_search=[]
                num_result=[]
                i = 0
                q = 0

                # Ask for name reservations is under
                for x in range (num):
                    name=input("["+str(x+1)+"]Enter the name the reservation is under:").upper()
                    name_search.append(name)

                # Search for reservation
                for reservations in resDetails:
                    # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
                    temp = reservations.split("|")
                    # Is 2 because in the list 2 is the name of the reservation
                    for i in range (len(name_search)):
                        if temp[2] == name_search[i]:
                            num_result.append(q)
                    q += 1

                # Display Result found
                count = 1
                for i, index in enumerate(num_result):
                    print("[" + str(count) + "] " + f" {resDetails[index]}")
                    count += 1

                # Ask for confirmation
                confirm=input("Are you sure you want to delete these reservation? [Y/N]: ").upper()
                if confirm == "Y":
                    # Delete Lines which matches
                    for i in range (len(num_result)):
                        del resDetails[num_result[i]]
                    print("Reservations Deleted.\n")

                elif confirm == "N":
                    print("Reservations Not Deleted.\n")

                else:
                    print("Invalid Input\n")
                loop=False

    # Ask user to try again in error happen
    except:
        print("Invalid Input, Try Again.\n")
    print("------------------------------------------------------------------------------------------------------")


########################################################################################################

def edit_reservation():
    name = input("Enter your name for the reservation: ").upper()
    slot = input("Enter your slot for the reservation (Slot X?): ")

    q = 0
    reservationFound = []
    numFound = []

    # to append new reservation into the list
    for reservations in resDetails:
        q += 1
        # Splits the reservations item using "|" as the separator and assigns the resulting split parts
        reserve = reservations.split("|")
        # Is 2 because in the list 2 is the name of the reservation
        if reserve[2] == name and reserve[1] == slot:
            reservationFound.append(reserve)
            date1, slot, name, email, phone, pax = reserve
            numFound.append(q)
    
    # To check if reservations found or not found
    # To further edit the reservation if reservation is found
    if len(reservationFound) >= 1:
        print(f"Reservation found.")
        # Enumerate() is used to access both the index and the item of a sequence simultaneously
        for q, numFound in enumerate(numFound):
            print(f"[{q + 1}] {resDetails[numFound - 1]}")
            q += 1

        # To let user choose the reservation that they want to update by looking at the index
        numUpdate = (input("Enter the number of the reservation to update: "))

        # To check errors
        # isnumeric() is used to check if the input consists of only numeric characters.
        while not numUpdate.isnumeric() or not (1 <= int(numUpdate) <= len(reservationFound)):
            print("Error, please input your number again.")
            numUpdate = int(input("Enter the number of the reservation to update: "))
    
        # To change the date of the reservations
        # To validate the date entered
        loop = True
        while loop:
            try:
                dateReplace = input("Enter the new date for the chosen reservation (YYYY-MM-DD): ")
                if dateReplace != datetime.datetime.strptime(dateReplace, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
            except ValueError:
                print(f"Invalid input, please try again!")
            else:
                dateNew = datetime.datetime.strptime(dateReplace, '%Y-%m-%d').date()
                dateOld = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
                dateToday = dateNew - dateOld
                day = dateToday.days
                loop = False
        
        # To let user change the date of reservations because the date chosen is >5 days or the user went back in time
        while day >= 5 or day < 0:
            print(f"Sorry but reservation needs to be booked 5 days in advance or the date is invalid.\n")
            dateReplace = input(f"Select another date (YYYY-MM-DD): ")
            dateNew = datetime.datetime.strptime(dateReplace, '%Y-%m-%d').date()
            dateToday = dateNew - dateOld
            day = dateToday.days

        # To let user choose another time slot
        # To validate whether the chosen time slot is within the range
        repeat = True
        while repeat:
            print("[1] 12.00pm - 2.00pm",
                  "\n[2] 02.00pm - 04.00pm",
                  "\n[3] 06.00pm - 08.00pm",
                  "\n[4] 08.00pm - 10.00pm")
            slotNew = int(input("Choose a new slot: "))
            # To make sure that input is within 1 and 4
            if slotNew >= 5 or slotNew <= 0:
                print("Please check again.")
            else:
                # Ask for a confirmation input to make sure that the user wants this slot
                # To validate the confirmation
                confirmation = input(f"Confirm?(Y/N): ").upper()
                if confirmation == "N":
                    print(f"Please choose again")
                elif confirmation == "Y":
                    editedDetails = f"{dateNew}|Slot {slotNew}|{name.upper()}|{email}|{phone}|{pax}\n"
                    resDetails.append(editedDetails)
                    repeat = False

        print(f"Your reservation has been updated. Thank you!")
        print("------------------------------------------------------------------------------------------------------")

    else:
        print(f"Reservation not found! Please check again")
        

########################################################################################################

def display_reservation():
    # Define column widths and headers
    columnWidths = [12, 8, 20, 30, 12, 8]
    headers = ["Date", "Slot", "Name", "Email", "Phone", "Number of Pax"]

    # Create header row
    headerRow = " | ".join(f"{header:<{width}}" for header, width in zip(headers, columnWidths))
    # Create dash line
    dashLine = "-" * len(headerRow)

    # Print headers and dash line
    print(headerRow)
    print(dashLine)

    # Iterate over each line in the reservation details text file
    for line in resDetails:
        # Split the line by '|' to extract the reservation information
        reservation = line.strip().split("|")

        # Extract the reservation details
        date = reservation[0]
        slot = reservation[1]
        name = reservation[2]
        email = reservation[3]
        phone = reservation[4]
        pax = reservation[5]

        # Print the reservation details in the given format
        print(" | ".join(f"{detail:<{width}}" for detail, width in zip([date, slot, name, email, phone, pax], columnWidths)))

    print("------------------------------------------------------------------------------------------------------")


########################################################################################################

def meal_recommendation():
    # Asks for number of recommendations user would like
    numRecommendation = int(input("How many menu recommendations do you want? (Choose 1-5): "))
    # Default number recommendation if input is not in range 1-5
    if numRecommendation < 1:
        numRecommendation = 1
        print("Invalid value. Defaulted to 1.")
    elif numRecommendation > 5:
        numRecommendation = 5
        print("Invalid value. Defaulted to 5.")

    # Generates recommendations
    print("Recommendations:")
    recommendationList = []
    # Generates recommendations up to the number the user has chosen
    while len(recommendationList) < numRecommendation:
        recommendation = random.choice(menuItems)
        if recommendation not in recommendationList:  # Avoids duplicate recommendations
            recommendationList.append(recommendation)
            print(f"- {recommendation}", end="")

    print("------------------------------------------------------------------------------------------------------")


########################################################################################################

main_program()
