Total_Money = 0
accounts = ["Tuition", "Rent", "Mousepad"]
divider = "============"

def menu():
    on = True

    while on:
        print(divider + divider + divider)
        print(divider + " BanKing " + divider)
        print(divider + divider + divider)
        print("1. View money\n2. Input paycheck\n3. Quit program\n4. View accounts")

        choice = input("Type Here: ")

        if choice == "1": #view money
            print("You have:" + str(Total_Money))
            go_back_to_menu()
        elif choice == "2": #input paycheck
            in_paycheck()
            go_back_to_menu()
        elif choice == "3": #quit
            on = False #option to close menu
            if on == False:
                break
        elif choice == "4": #view accounts
            for x in accounts:
                print("ACCOUNT " + str(accounts.index(x) + 1) + ": " + x)
            go_back_to_menu()
            
def in_paycheck():
    global Total_Money

    paycheck = int(input("How much money did you make?"))
    Total_Money = Total_Money + paycheck

def go_back_to_menu():
    input("Press enter to return to the menu.")

menu()