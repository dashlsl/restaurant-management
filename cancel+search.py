def cancel_reservation():
    while (True):
        try:
            print("**Cancel Reservation**")
            # Get the reservation number the user wants to cancel
            numUpdate = input("Enter the number of the reservations you want to cancel: ")
            # To check errors
            while not numUpdate.isdigit() or not (1 <= int(numUpdate)):
                print("Error, please input a valid number.")
                numUpdate = input("Enter the number of the reservation you want to cancel: ")
            # Convert the input to an integer
            numUpdate = int(numUpdate)
            matching_reservations = []
            q = 0

            # If user wants to delete only 1 reservation
            if numUpdate == 1:
                # Call search_reservation() and unpack the returned values
                matching_reservations = search_reservation(resDetails)

                if matching_reservations:
                    # If search found exactly one result
                    if len(matching_reservations) == 1:
                        # Ask for confirmation
                        confirm = input("Are you sure you want to delete this reservation? [Y/N] ").upper()
                        if confirm == "Y":
                            # Delete Line which matches
                            del resDetails[matching_reservations[0]]
                            print("Reservation Deleted.\n")
                        elif confirm == "N":
                            print("Reservation Not Deleted.\n")
                        else:
                            print("Invalid Input\n")
                        break

                    # If search found more than one results
                    elif len(matching_reservations) > 1:
                        # Ask which reservation to delete
                        choice = int(input("Which reservation would you like to delete?: "))

                        # Ask for confirmation
                        confirm = input("Are you sure you want to delete this reservation? [Y/N]").upper()
                        if confirm == "Y":
                            # Delete Line which matches
                            del resDetails[matching_reservations[choice-1]]
                            print("Reservation Deleted.\n")
                        elif confirm == "N":
                            print("Reservation Not Deleted.\n")
                        else:
                            print("Invalid Input\n")
                        break

                    # No search results
                    else:
                        print("No results were found\n")
                        break

                else:
                    print(f"Reservation not found! Please check again")
                    print("-------------------------------------------------------------------------------------------------------")


      
            '''vvv
            I didn't change this part
            Not sure how to include the search function in here
            since it searches multiple times
            my brain hurty
            vvv
            '''
                  
            # If user wants to delete more than 1 reservation
            elif numUpdate > 1:
                name_search = []

                # Ask for name reservations is under
                for x in range(numUpdate):
                    name = input("["+str(x+1)+"]Enter the name the reservation is under:").upper()
                    name_search.append(name)

                # Search for reservation
                for reservations in resDetails:
                    # The line splits the reservations item using the pipe symbol (|) as the separator and assigns the resulting split parts to the reservation variable
                    info = reservations.split("|")
                    # Is 2 because in the list 2 is the name of the reservation
                    for i in range(len(name_search)):
                        if info[2] == name_search[i]:
                            matching_reservations.append(q)
                    q += 1

                # Display Result found
                count = 1
                print("Search Found!")
                for i, index in enumerate(matching_reservations):
                    print("[" + str(count) + "] " + f" {resDetails[index]}")
                    count += 1

                # Ask for confirmation
                confirm = input("Are you sure you want to delete these reservation? [Y/N]: ").upper()
                if confirm == "Y":
                    # Delete Lines which matches
                    a = 0
                    for i in range(len(matching_reservations)):
                        del resDetails[matching_reservations[i] - a]
                        a += 1
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

