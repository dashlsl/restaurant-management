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
                slot = 0

            # Displays people that made reservations for the chosen slot
            clash = []  # List for people with the same reservation
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
            if len(clash) < 8:  # Slot available
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
                        pax = 0

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
            else:  # Slot unavailable
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
    print("-----------------------------------------------------------------------------------------------------------")
    return resDetails


########################################################################################################

def cancel_reservation():
    try:
        while True:
            print("**Cancel Reservation**")
            num = int(input("How many reservations do you want to delete?: "))
            num_result = []
            q = 0

            if num == 1:
                name = input("Enter the name the reservation is under: ").upper()
                # Search file for reservation with that name
                # to append new reservation into the list

                for reservations in resDetails:
                    # The line splits the reservations item using | as the separator and assigns the resulting parts
                    info = reservations.split("|")
                    # Is 2 because in the list 2 is the name of the reservation
                    if info[2] == name:
                        num_result.append(q)
                    q += 1

                # If search found exactly one result
                if len(num_result) == 1:
                    print("Search Found!")
                    # Display Search
                    for i, index in enumerate(num_result):
                        print(f"[{1}] {resDetails[index]}")
                    # Ask for confirmation
                    confirm = input("Are you sure you want to delete this reservation? [Y/N] ").upper()
                    if confirm == "Y":
                        # Delete Line which matches
                        del resDetails[num_result[0]]
                        print("Reservation Deleted.\n")
                    elif confirm == "N":
                        print("Reservation Not Deleted.\n")
                    else:
                        print("Invalid Input\n")
                    break

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
                    break
                else:
                    print("No results were found\n")
                    break

            # If user wants to delete more than 1 reservation
            elif num > 1:
                name_search = []

                # Ask for name reservations is under
                for x in range(num):
                    name = input("["+str(x+1)+"]Enter the name the reservation is under:").upper()
                    name_search.append(name)

                # Search for reservation
                for reservations in resDetails:
                    # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
                    info = reservations.split("|")
                    # Is 2 because in the list 2 is the name of the reservation
                    for i in range(len(name_search)):
                        if info[2] == name_search[i]:
                            num_result.append(q)
                    q += 1

                # Display Result found
                count = 1
                print("Search Found!")
                for i, index in enumerate(num_result):
                    print("[" + str(count) + "] " + f" {resDetails[index]}")
                    count += 1

                # Ask for confirmation
                confirm = input("Are you sure you want to delete these reservation? [Y/N]: ").upper()
                if confirm == "Y":
                    # Delete Lines which matches
                    a=0
                    for i in range(len(num_result)):
                        del resDetails[num_result[i]-a]
                        a+=1
                    print("Reservations Deleted\n")
                elif confirm == "N":
                    print("Reservations Not Deleted\n")
                else:
                    print("Invalid Input\n")
                break
            else:
                print("Invalid Input\n")
                break

    # Ask user to try again in error happen
    except:
        print("Invalid Input, Try Again.\n")
    print("------------------------------------------------------------------------------------------------------")


########################################################################################################

def edit_reservation():
    '''NEEDS TO BE CHANGED TO MULTI SELECTION'''
    # Name input
    name_res = input("Enter your name for the reservation: ").upper()
    # Date input
    date_res = ""
    while date_res == "":
            try:
                date_res = input("Enter your date for the reservation (YYYY-MM-DD): ")
                # Checks if date is in the correct format
                if date_res != datetime.datetime.strptime(date_res, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
            except ValueError:
                print("\n"
                      "Invalid date format, please try again")
                date_res = ""
            else:
                date_res = datetime.datetime.strptime(date_res, "%Y-%m-%d").date()
    # Slot input
    slot_res = 0
    while slot_res == 0:
        print("[1] 12:00pm - 02:00pm"
                "\n[2] 02:00pm - 04:00pm"
                "\n[3] 06:00pm - 08:00pm"
                "\n[4] 08:00pm - 10:00pm")
        slot_res = int(input("Enter your slot for the reservation (Slot X?): "))
        if slot_res < 1 or slot_res > 4:
            print("\nInvalid slot, please try again")
            slot_res = int(input("Enter your slot for the reservation (Slot X?): "))

    count = 0
    reservationFound = []
    numFound = []

    # To append new reservation into the list
    for reservations in resDetails:
        count += 1
        # Splits the reservations item using "|" as the separator and assigns the resulting split parts
        reserve = reservations.split("|")
        # Check if user inputs are in resDetails
        if reserve[2] == name_res:
            reservationFound.append(reserve)
            date, slot, name, email, phone, pax = reserve
            numFound.append(count)
    
    # To check if reservations found or not found
    # To further edit the reservation if reservation is found
    if len(reservationFound) >= 1:
        print(f"Reservation found.")
        # Enumerate() is used to access both the index and the item of a sequence simultaneously
        # Display reservations
        for count, numFound in enumerate(numFound):
            print(f"[{count + 1}] {resDetails[numFound - 1]}")
            count += 1

        # To let the user choose the reservation they want to update by looking at the index
        numUpdate = input("Enter the number of the reservation to update: ")
        # To check errors
        while not numUpdate.isdigit() or not (1 <= int(numUpdate) <= len(reservationFound)):
            print("Error, please input a valid number.")
            numUpdate = input("Enter the number of the reservation to update: ")
        # Convert the input to an integer
        numUpdate = int(numUpdate)

        # User can select what they would like to edit
        editing = True
        while editing:

            # Variables for editing reservation
            dateNew = None
            slotNew = None
            nameNew = None
            emailNew = None
            phoneNew = None
            paxNew = None

            print(f"What do you want to edit?"
                  f"\n[1] Date"
                  f"\n[2] Slot"
                  f"\n[3] Name"
                  f"\n[4] Email"
                  f"\n[5] Phone number"
                  f"\n[6] Number of pax"
                  f"\n[7] Exit")
            selection = int(input("Enter your selection: "))
            print("")
            match selection:
                # Change date
                case 1:
                    # To validate the date entered
                    oldDate = True
                    checking = True
                    while oldDate:
                        while checking:
                            try:
                                dateReplace = input("Enter the new date for the chosen reservation (YYYY-MM-DD): ")
                                if dateReplace != datetime.datetime.strptime(dateReplace, "%Y-%m-%d").strftime('%Y-%m-%d'):
                                    raise ValueError
                            except ValueError:
                                print(f"Invalid input, please try again!")
                            else:
                                dateNew = datetime.datetime.strptime(dateReplace, '%Y-%m-%d').date()
                                dateOld = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                                dateToday = dateNew - dateOld
                                day = dateToday.days
                                checking = False
                        
                        # To let user change the date of reservations because the date chosen is >5 days or the user went back in time
                        while day >= 5 or day < 0:
                            print(f"Sorry but reservation needs to be booked 5 days in advance or the date is invalid.\n")
                            dateReplace = input(f"Select another date (YYYY-MM-DD): ")
                            dateNew = datetime.datetime.strptime(dateReplace, '%Y-%m-%d').date()
                            dateToday = dateNew - dateOld
                            day = dateToday.days
                            
                        # Ask for a confirmation input
                        confirmLoopDate = True
                        while confirmLoopDate:
                            userConfirmation = input(f"Your new date is {dateNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                checking = True
                                confirmLoopDate = False
                            elif userConfirmation == "Y":
                                oldDate = False
                                confirmLoopDate = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopDate = True

                # Change time slot
                case 2:
                    # To validate whether the chosen time slot is within the range
                    oldSlot = True
                    checking = True
                    while oldSlot:
                        while checking:
                            print("[1] 12.00pm - 2.00pm",
                                  "\n[2] 02.00pm - 04.00pm",
                                  "\n[3] 06.00pm - 08.00pm",
                                  "\n[4] 08.00pm - 10.00pm")
                            slotNew = int(input("Choose a new slot: "))
                            # To make sure that input is within 1 and 4
                            if slotNew >= 5 or slotNew <= 0:
                                print("Please choose a valid slot.")
                            else:
                                # Displays people that made reservations for the chosen slot
                                clash = []
                                for reservation in resDetails:
                                    info = reservation.split("|")
                                    if info[0] == str(date) and info[1][5] == str(slot):
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
                                            oldSlot = True  # Re-trigger the loops to enter slot again
                                        elif changer == 2:
                                            print("\n"
                                                  "Choosing a different slot...")
                                            slot = 0
                                        else:
                                            print("\n"
                                                  "Invalid selection, please try again")
                                            changer = 0
                                else:  # Slot available
                                    print("Slot is available.")
                                    checking = False

                        # Ask for a confirmation input
                        confirmLoopSlot = True
                        while confirmLoopSlot:
                            userConfirmation = input(f"Your new slot is {slotNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                checking = True
                                confirmLoopSlot = False
                            elif userConfirmation == "Y":
                                oldSlot = False
                                confirmLoopSlot = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopSlot = True

                # Change name
                case 3:
                    oldName = True
                    while oldName:
                        nameNew = input("Enter the new name for the reservation: ").upper()
                        # Ask for a confirmation input
                        confirmLoopName = True
                        while confirmLoopName:
                            userConfirmation = input(f"Your new name is {nameNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                oldName = True
                                confirmLoopName = False
                            elif userConfirmation == "Y":
                                oldName = False
                                confirmLoopName = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopName = True

                # Change email
                case 4:
                    oldEmail = True
                    while oldEmail:
                        emailNew = input("Enter the email for the reservation: ").lower()
                        # Ask for a confirmation input
                        confirmLoopEmail = True
                        while confirmLoopEmail:
                            userConfirmation = input(f"Your new email is {emailNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                oldEmail = True
                                confirmLoopEmail = False
                            elif userConfirmation == "Y":
                                oldEmail = False
                                confirmLoopEmail = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopEmail = True

                # Change phone number
                case 5:
                    oldPhone = True
                    while oldPhone:
                        phoneNew = input("Enter the phone number for the reservation: ")
                        # Ask for a confirmation input
                        confirmLoopPhone = True
                        while confirmLoopPhone:
                            userConfirmation = input(f"Your new phone number is {phoneNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                oldPhone = True
                                confirmLoopPhone = False
                            elif userConfirmation == "Y":
                                oldPhone = False
                                confirmLoopPhone = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopPhone = True

                # Change number of pax
                case 6:
                    oldPax = True
                    while oldPax:
                        paxNew = 0
                        while paxNew == 0:
                            paxNew = int(input("Enter number of pax (maximum 4): "))
                            if paxNew < 1 or paxNew > 4:
                                print("\nInvalid number of pax, please try again")
                                paxNew = int(input("Enter number of pax (maximum 4): "))
                        # Ask for a confirmation input
                        confirmLoopPax = True
                        while confirmLoopPax:
                            userConfirmation = input(f"Your new pax number is {paxNew}. Would you like to confirm? [Y/N]: ").upper()
                            if userConfirmation == "N":
                                oldPax = True
                                confirmLoopPax = False
                            elif userConfirmation == "Y":
                                oldPax = False
                                confirmLoopPax = False
                            else:
                                print("Invalid input. Please select Y/N.")
                                confirmLoopPax = True

                # Exit editing
                case 7:
                    # Modify the specified reservation with the edited details
                    if len(reservationFound) >= numUpdate:
                        index_to_edit = numUpdate - 1
                        reservation_to_edit = resDetails[index_to_edit].split("|")
                        # To append edited reservation details into a list
                        if dateNew is not None:
                            reservation_to_edit[0] = str(dateNew)
                        if slotNew is not None:
                            reservation_to_edit[1] = f"Slot {slotNew}"
                        if nameNew is not None:
                            reservation_to_edit[2] = nameNew
                        if emailNew is not None:
                            reservation_to_edit[3] = emailNew
                        if phoneNew is not None:
                            reservation_to_edit[4] = phoneNew
                        if paxNew is not None:
                            reservation_to_edit[5] = str(paxNew)

                    # Confirm details
                    final = True
                    while final:
                        userConfirmation = input("Your edited reservation is " + "|".join(reservation_to_edit) + "\nWould you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            final = False
                            editing = True
                        elif userConfirmation == "Y":
                            # To append the edited reservation details to the text file
                            resDetails[index_to_edit] = "|".join(reservation_to_edit)
                            print("Reservation successfully updated!")
                            final = False
                            editing = False
                        else:
                            print("Invalid input. Please select Y/N.")
                            final = True
                    print("-------------------------------------------------------------------------------------------")
                
                # Invalid selection
                case _:
                    print("Please try again with a valid response (1-7)\n")
                    editing = True

    else:
        print(f"Reservation not found! Please check again")
        print("-------------------------------------------------------------------------------------------------------")


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
    print(f"Reservations\n{dashLine}\n{headerRow}\n{dashLine}\n")

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
        # Generates a random item found in menuItems text file
        recommendation = random.choice(menuItems)
        # Avoids duplicate recommendations
        if recommendation not in recommendationList:
            recommendationList.append(recommendation)
            print(f"- {recommendation}", end="")

    print("------------------------------------------------------------------------------------------------------")


########################################################################################################

main_program()
