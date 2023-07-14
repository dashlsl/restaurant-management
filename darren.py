#update/edit reservation
import datetime
def edit_reservation():
    name = input("Enter your name for the reservation: ").upper()
    reservationFound = []
    reservationSelect = []
    numFound = []

    q = 0
    # to append new reservation into the list
    for reservations in reserve:
        q += 1
        # the line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
        reservations = reservations.split("|")
        # is 2 because in the list 2 is the name of the reservation
        if reservations[2] == name:
            reservations.append(reservations)
            numFound.append[q]
    
    # to check if reservations found or not found
    # to furthur edit the reservation if reservation is found
    if len(reservationFound) >= 1:
        print(f"Reservation found.")
        #emumerate() is used to access both the index and the item of a sequence simultaneously
        for i, index in enumerate(numFound):
            print(f"[{q + 1}] {reserve[index - 1]}")

        # to let user choose the reseravation that they want to update by looking at the index
        numUpdate = int(input("Enter the number of the reservation to update: "))

        # to check errors
        # isnumeric() is used to check if the input consists of only numeric characters.
        while not numUpdate.isnumeric() or not (1 <= int(numUpdate) <= len(reservationFound)):
            print("Error, please input your number again.")
            numUpdate = int(input("Enter the number of the reservation to update: "))
    
        # to change the date of the reservations
        dateReplace = input("Enter the new date of the reservation (DD-MM-YYYY): ")
        dateNew = datetime.strptime(dateReplace, '%d-%m-%Y').date()
        dateToday = dateNew - dateNow
        day = dateToday.days
        
        # to let user change the date of reservations because the date chosen is less than 5 days
        while day < 5:
            print(f"Error! Please make reservations at least 5 days in advance.\n")
            dateReplace = input(f"Select a date (dd-mm-yyyy): ")
            dateNew = datetime.strptime(dateNew, '%d-%m-%Y').date()
            dateToday = dateNew - dateNow
            day = dateToday.days

        print (f"[1] 12.00pm - 2.00pm"
            f"\n[2] 02.00pm - 04.00pm"
            f"\n[3] 06.00pm - 08.00pm"
            f"\n[4] 08.00pm - 10.00pm")
    else:
        print(f"Reservation not found! Please check again")
