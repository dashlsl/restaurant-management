print (f"hello world")
### update/edit reservation
with open("reservation_21094230.txt", "r+") as f:
    contents = f.readlines()

def update():
    for i in contents:
        print(i)
    change = input("Which line is yous? ")
    repeat = True
    while repeat:
        print ("Fuck")
