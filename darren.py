#update/edit reservation
with open("reservation_21094230.txt", "r+") as f:
    contents = f.readlines()

def update():
    name = input("Enter your name for the reservation: ").upper()
    reservationFound = []
    reservationSelect = []
    numFound = []

    q = 0
    #to append new reservation into the list
    for reservations in reserve:
        q += 1
        reservations = reservations.split("|")
        #is 2 because in the list 2 is the name of the reservation
        if reservation[2] == name:
            reservations.append(reservations)
            numFound.append[q]
    


