file = open("chronic_banking.txt", "r")
account_name = file.readline().split(", ") #creating list of NAMES
str_account_balance = file.readline(). split(", ") #creating list of AMOUNTS
file.close()

account_balance = []

num_of_accounts = len(account_name)
for x in range(num_of_accounts):
    account_balance.append(float(str_account_balance[x]))

clear_page = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

account_obj = []

for x in range(num_of_accounts): #create the object names
    y = str(x)
    account_obj.append("account_" + y)

for x in range(num_of_accounts): #creates the objects and adds parameters
    account_obj[x] = Account(account_name[x], account_balance[x])

print(clear_page)
print("\n═══════════════════════════════════════")
print("   ______              __   __)        ")
print("  (, /    )           (, ) /  ,        ")
print("    /---(  _  __        /(     __   _  ")
print(" ) / ____)(_(_/ (_   ) /  \__(_/ (_(_/_")
print("(_/ (               (_/           .-/  ")
print("═════════════════════════════════(_/═══\n")

input("Press any key to continue.")

def menu():
    on = True

    available_options = [
        "View accounts",
        "Edit account balance",
        "Quit program"
    ]

    while on:
        print("\n\n══════════════════════════════════")
        print("||          M  E  N  U          ||")
        print("══════════════════════════════════\n")

        for i, option in enumerate(available_options):
            print(f"{i + 1}. {option}\n")

        print("\n\n\n\n\n\n\n\n")

        choice = input(f"Select an option (1-{len(available_options)}): ")

        if choice == "1": #view money
            view_accounts()
        elif choice == "2": #input paycheck
            edit_account()
        elif choice == "3": #quit
            on = False #option to close menu
            if on == False:
                break
        else: # error handling
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**ERROR: Please select an option from the list above.\n\n\n\n\n\n\n\n\n\n\n\n\n")
            input("Press any button to retry.")

def back_menu():
    input("Press enter to return to the menu.")
    menu()

def view_accounts():
    print("\n\n")

    for obj in account_obj:
        if(obj.name == "Cash"):
            print("========== CASH ===========")
            print(f"{obj.name.strip()}: $" + "{:0,.2f}".format(obj.balance))
        elif(obj.name == "Chequing Account"):
            print(f"{obj.name.strip()}: $" + "{:0,.2f}".format(obj.balance))
            print("===========================\n\n")
            print("========= SAVINGS =========")   
        else: #ACCOUNTS: investments, rent, food, emergency funds
            print(f"{obj.name.strip()}: $" + "{:0,.2f}".format(obj.balance))
    
    print("===========================\n\n")
    
    total_balance = sum(account_balance)
    print("======= TOTAL MONEY =======")
    print("Total Money: $" + "{:0,.2f}".format(total_balance))
    print("===========================\n\n")
    
    back_menu()

def edit_account():
    on = True
    print("\nWhich account would you like to edit?\n")
    
    for i, obj in enumerate(account_obj):
        print(f"{i+1}." + obj.name)

    available_options = [
        "Deposit to account",
        "Withdraw from account",
        "Edit account balance",
        "Return to menu"
    ]

    choice_a = int(input(f"Select an option (1-{len(available_options)}). ")) - 1

    print("=================")
    print("Available Options:")
    print("=================")
    for i, option in enumerate(available_options):
        print(f"{i + 1}. {option}\n")

    choice_b = input("Choose an option: ")

    while on:

        if choice_b == "1":
            current = float(account_obj[choice_a].balance)
            
            print("How much would you like to deposit?")
            to_deposit = float(input("Enter amount here: "))
            
            new_balance = current + to_deposit

            account_obj[choice_a].balance = new_balance

            save()

            return
        
        elif choice_b == "2":
            current = float(account_obj[choice_a].balance)

            print("How much would you like to withdraw?")
            to_withdraw = float(input("Enter amount here: "))

            new_balance = current - to_withdraw

            account_obj[choice_a].balance = new_balance

            save()

            return
        
        elif choice_b == "3":
            print(f"Current balance: {account_obj[choice_a].balance}")
            edited_balance = float(input("What would you like to edit this balance to?"))
            
            print(f"New balance: ${account_obj[choice_a].balance}")
            print("Are you sure you want to keep these changes?")
            choice = input("Y/N\nEnter here: ")

            if choice == "Y" or "y":
                account_obj[choice_a].balance = edited_balance
            elif choice == "N" or "n":
                print("Returning to menu ...")
                back_menu()
            else:
                print("Invalid response. Returning to menu...")
                back_menu()

            return
        
        elif choice_b == "4":
            on = False
            print("Returning to menu...")
            back_menu()
        
        else: 
            print("Invalid option.")

def save():
    file = open("chronic_banking.txt", "w")

    for i in range(num_of_accounts):
        if i == num_of_accounts - 1:
            file.write(f"{account_obj[i].name}")
        else:
            file.write(f"{account_obj[i].name}, ")

    for i in range(num_of_accounts):
        if i == num_of_accounts - 1:
            file.write(f"{account_obj[i].balance}")
        else: 
            file.write(f"{account_obj[i].balance}, ")

    file.close()

menu()
