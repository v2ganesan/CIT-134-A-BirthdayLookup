def seatingChart():
    import json

    try:
        with open("monthly_sales.txt", 'r') as current_file:
            list1 = []
            list2 = []
            for line in current_file.readlines():
                
                stripped_line = line.strip()
                list2 = stripped_line.split()
                list1.append(list2)

        return list1[1:]

    except OSError:
        print("ERROR: Unable to open the file.")
def viewSeating(chart):
    print(chart)
def orderTix(chart):
    tickets = 0
    totalPrice = 0
    while True:
            
        row = int(input("what row would you like? "))
        seatNumber = int(input("what number seat would you like? "))
        if  0<= row <= 4:
            price = 80 
        elif 5<= row <= 10:
            price = 50 
        else :
            price = 25
        tickets += 1
        totalPrice += price
        chart[row][seatNumber] = "X"
        choice = input("Would you like another ticket?")
        if choice == "Yes":
            continue
        else:
            break
        totalPrice = totalPrice *0.725 +5

    n = "Row: " + str(row) + ", " + "Seat Number: " + str(seatNumber) + ", " + "$" + str(totalPrice *1.0725 +5)
    nameEmail = input("name and email: ")
    print("Receipt: " + n + " " + "Name/Email " +nameEmail)
    def display():
        dict = {}
        dict[nameEmail] = n
        user = input("Would you like to see all purchases?")
        if user == "Yes":
            print(dict)
        else:
            user2 = input("would you like to search for a name?")
            if user2 == "Yes":
                search = input("what is the name you would like to see?")
                if search in dict.keys():
                    print (dict[search])
            else:
                print("exit")

    
    


chart = seatingChart()

while True:
    print("welcome to the outdoor park concert /n V - view /n B - buy (display and search are nested within this function) Q- quit.")
    selection = input("what would you like to do?")
    if selection == "V":
        viewSeating(chart)
    elif selection == "B":
        orderTix(chart)
    elif selection == "Q":
        print("exit")
        break