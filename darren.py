#update/edit reservation
import datetime

resDetails = []
with open("reservation_21094230.txt", "r") as f:
    a = 0
    for content in f:
        a += 1
        resDetails.append(content.strip('\n'))
        #resDetails = f.readlines()
    

def edit_reservation():
    name = input("Enter your name for the reservation: ").upper()
    reservationFound = []
    numFound = []

    q = 0
    # to append new reservation into the list
    for reservations in resDetails:
        q += 1
        # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
        reserve = reservations.split('|')
        # Is 2 because in the list 2 is the name of the reservation
        if reserve[2] == name:
            reservationFound.append(reserve)
            numFound.append[q]
    
    # To check if reservations found or not found
    # To further edit the reservation if reservation is found
    if len(reservationFound) == 0:
        print(f"Reservation not found! Please check again")

    else:
        print(f"Reservation found.")
        q = 0
        # Enumerate() is used to access both the index and the item of a sequence simultaneously
        for q, numFound in enumerate(numFound):
            #print(list(enumerate(resDetails)))
            print(f"[{q + 1}] {resDetails[numFound - 1]}")

        # To let user choose the reservation that they want to update by looking at the index
        numUpdate = int(input("Enter the number of the reservation to update: "))

        # To check errors
        # isnumeric() is used to check if the input consists of only numeric characters.
        while not numUpdate.isnumeric() or not (1 <= int(numUpdate) <= len(reservationFound)):
            print("Error, please input your number again.")
            numUpdate = int(input("Enter the number of the reservation to update: "))
    
        # To change the date of the reservations
        dateReplace = input("Enter the new date for the chosen reservation (YYYY-MM-DD): ")
        dateNew = datetime.strptime(dateReplace, '%Y-%m-%d').date()
        dateToday = dateNew - resDetails[0]
        day = dateToday.days
        
        # To let user change the date of reservations because the date chosen is less than 5 days
        while day < 5:
            print(f"Sorry but reservation needs to be booked 5 days in advance.\n")
            dateReplace = input(f"Select another date (YYYY-MM-DD): ")
            dateNew = datetime.strptime(dateNew, '%Y-%m-%d').date()
            dateToday = dateNew - resDetails[0]
            day = dateToday.days

        print(f"[1] 12.00pm - 2.00pm"
              f"\n[2] 02.00pm - 04.00pm"
              f"\n[3] 06.00pm - 08.00pm"
              f"\n[4] 08.00pm - 10.00pm")

edit_reservation()

######################################################################################
def edit_reservation():
    #Name input
    name_res = input("Enter your name for the reservation: ").upper()
    #Date input. Checks whether date in correct format
    date_res = ""
    while date_res == "":
            try:
                date_res = input("Enter your date for the reservation (YYYY-MM-DD): ")
                if date_res != datetime.datetime.strptime(date_res, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
            except ValueError:
                print("\n"
                      "Invalid date format, please try again")
                date_res = ""
            else:
                date_res = datetime.datetime.strptime(date_res, "%Y-%m-%d").date()
    #Slot input.
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

    # to append new reservation into the list
    for reservations in resDetails:
        count += 1
        # Splits the reservations item using "|" as the separator and assigns the resulting split parts
        reserve = reservations.split("|")
        # Check if user inputs are in resDetails
        if (reserve[2] == name_res 
            and reserve[1][5] == str(slot_res) 
            and datetime.datetime.strptime(reserve[0], "%Y-%m-%d").date() == date_res):
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

        # Variables for editing reservation
        dateNew = None
        slotNew = None
        nameNew = None
        emailNew = None
        phoneNew = None
        paxNew = None

        editing = True
        while editing:
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
                #Change date
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
                        
                        #Confirm date
                        userConfirmation = input(f"Your new date is {dateNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldDate = False

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
                                    print("Slot is available.")
                                    checking = False

                        # Ask for a confirmation input to make sure that the user wants this slot
                        # To validate the confirmation
                        userConfirmation = input(f"Your new slot is {slotNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldSlot = False

                # Change name
                case 3:
                    oldName = True
                    while oldName:
                        nameNew = input("Enter the new name for the reservation: ").upper()

                        userConfirmation = input(f"The new name is {nameNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldName = False

                # Change email
                case 4:
                    oldEmail = True
                    while oldEmail:
                        emailNew = input("Enter the email for the reservation: ").lower()

                        userConfirmation = input(f"The new email is {emailNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldEmail = False

                # Change phone number
                case 5:
                    oldPhone = True
                    while oldPhone:
                        phoneNew = input("Enter the phone number for the reservation: ")

                        userConfirmation = input(f"The new phone number is {phoneNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldPhone = False

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

                        userConfirmation = input(f"The new number of pax is {paxNew}. Would you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            checking = True
                        elif userConfirmation == "Y":
                            oldPax = False

                # Exit editing
                case 7:
                    # Modify the specified reservation with the edited details
                    if len(reservationFound) >= numUpdate:
                        index_to_edit = numUpdate - 1
                        reservation_to_edit = resDetails[index_to_edit].split("|")

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

                    #Confirm details
                    final = True
                    while final:
                        userConfirmation = input("Your edited reservation is " + "|".join(reservation_to_edit) + "\nWould you like to confirm? [Y/N]: ").upper()
                        if userConfirmation == "N":
                            final = True
                        elif userConfirmation == "Y":
                            resDetails[index_to_edit] = "|".join(reservation_to_edit)
                            print("Reservation successfully updated!")
                            final = False
                    print("------------------------------------------------------------------------------------------------------")
                    editing = False

    else:
        print(f"Reservation not found! Please check again")