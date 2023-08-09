import sys



def valid_user(account_No,pin):
    accounts={
        "1234567890":{"pin":"1234","balance":1000},
        "2345678901":{"pin": "2345", "balance":100}
    }
    if account_No in accounts and accounts[account_No]["pin"] == pin:
        return True,accounts[account_No]["balance"]
    return False,None

def menu():
    print("1.Deposit\n"
          "2.Withdraw\n"
          "3.Check Balance\n"
          "4.Exit\n")
    return input("Select an option: ")

def deposit(account_No,current_balance):
    amount = float(input("Enter the amount you wanted to deposit: "))
    if amount > 0:
        current_balance += amount
        print("Deposit successful!\n"
              "Your updated balance: ", current_balance)
        return current_balance
    else:
        print("Invalid input.\n"
              "Please! try again.")



def withdraw(account_No,current_balance):
    amount= float(input("Enter the amount you want to withdraw: "))
    if amount > current_balance:
        print("Insufficient balance!")
    else:
        current_balance -= amount
        print("withdrawal successfull!\n"
              "Your updated balance: ",current_balance)
    return current_balance

def check_balance(current_balance):
    print("Your current balance: ",current_balance)

def exit():
    print("Thank you sir for using the ATM :)")
    sys.exit(0)


if __name__=="__main__":
    while True:
        account_No = input("Enter Your account number: ")
        pin= input("Enter your PIN : ")

        valid,balance=valid_user(account_No,pin)

        if valid:
            print("Welcome sir into your own virtual aacount :) ")
            while True:
                choice=menu()
                if choice == "1":
                    balance = deposit(account_No,balance)
                elif choice == "2":
                    balance = withdraw(account_No, balance)
                elif choice == "3":
                    check_balance(balance)
                elif choice == "4":
                    exit()
                else:
                    print("Invalid option.\n"
                          "Please! try again.")
        else:
            print("Validation failed.\n"
                  "Please! try again.")

