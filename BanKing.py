divider = "============"

file = open("chronic_banking.txt", "r")
account_name = file.readline().split(", ") #creating lists of NAMES
account_balance = file.readline(). split(", ") #creating lists of AMOUNTS
file.close()

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

account_obj = []
num_of_accounts = len(account_name)

for x in range(num_of_accounts): #create the object names
    y = str(x)
    account_obj.append("account_" + y)

for x in range(num_of_accounts): #creates the objects and adds parameters
    account_obj[x] = Account(account_name[x], account_balance[x])

def menu():
    on = True

    while on:
        print(divider + " BanKing " + divider)
        print("1. View accounts\n2. Edit account balance\n3. Quit program")

        choice = input("Type Here: ")

        if choice == "1": #view money
            view_accounts()
            return
        
        elif choice == "2": #input paycheck
            edit_account()
            return
        
        elif choice == "3": #quit
            on = False #option to close menu
            if on == False:
                break

def back_menu():
    input("Press enter to return to the menu.")

def view_accounts():
    for obj in account_obj:
        print(obj.name + ": " + obj.balance)

def edit_account():
    print("Which account would you like to edit?")    
    choice_a = int(input("Type Here: "))

    available_options = [
        "Add to balance",
        "Subtract from balance",
        "Edit balance",
    ]
    print("Available Options:")
    for i, option in enumerate(available_options):
        print(f"{i + 1}. {option}")

    choice_b = input("Type Here: ")

    if choice_b == "1":
        current = int(account_obj[choice_a].balance)
        
        print("How much would you like to add?")
        to_add = int(input("Enter amount here: "))
        
        new_balance = current + to_add

        account_obj[choice_a].balance = new_balance
        print(account_obj[choice_a].balance)
        return
    
    elif choice_b == "2":
        return
    elif choice_b == "3":
        return
menu()

# #Accounts ARE ALWAYS in this order: cash, rent, food, emergency funds, investing, etc

