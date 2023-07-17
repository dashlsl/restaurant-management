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