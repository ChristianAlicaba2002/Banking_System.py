import  DataofBanking as data_bank
import random
import datetime
listOfAccount = []
all_transaction = []

def CreateAccount():
        print()
        while True:
            try:
                print("===========================================")
                print("\tCreate Account")
                account_no = random.randint(111111,999999)
                username   = input("Enter your Username : ")
                age =    int(input("Enter your Age      : "))
                gender =     input("Enter your Gender   : ")
                address =    input("Enter your Address  : ")
            
                balance = 0
                account = data_bank.userAccount(account_no,username,age,gender,address,balance)
                listOfAccount.append(account)
               

                print("===========================================")
                print("\tCreate Account Successfully")
                print()
                print(f"Account no : {account_no}")
                print(f"Username   : {username}")
                print(f"Age        : {age}")
                print(f"Gender     : {gender}")
                print(f"Address    : {address}")
                print(f"Balance    : {balance}")
                return 
                
            except Exception:
                print("===========================================\n")
                print("\tEnter your age not a words.")
                print("\tSorry we need you to choose again.")
                return
        
            # return listOfAccount
            
                        
def UseExistingAccount(user):
    print("===========================================")
    print("\tUse Existing Account")
    if not user:
        print("===========================================\n")
        print("\tNo Account exist ")
        main()
    print()
    check_AccountNumber = int(input("Enter Account no: "))
    print()  
    while True:
        for acc_user in listOfAccount:
            if check_AccountNumber == acc_user.account_no:
                while True:
                    print("===========================================")     
                    print("\tHello "+ acc_user.username)
                    print("1.Deposit")
                    print("2.Withdraw")
                    print("3.Transaction")
                    print("4.Return")
                    
                    
                    choice = int(input("Choice Category (1/2/3): "))
                    choice in [1,2,3,4]     
                        
                    if choice == 1:
                        print("===========================================")
                        print("\tDeposit")
                        deposit_Amount = int(input("Enter the amount: Php"))
                        if  deposit_Amount <= 0:
                            print("===========================================\n")
                            print("\tPlease enter valid amount\n")
                        elif deposit_Amount < 500:
                            print("===========================================\n")
                            print("\tPlease Deposit more than Php500\n")
                        else:
                            acc_user.balance += deposit_Amount
                            
                            dates = datetime.datetime.now()
                            depoist_date = dates.date()
                            time = dates.strftime("%H:%M:%p")
                            deposit_category = "Deposit"
                            deposit_account_no = acc_user.account_no
                            depoist_balance = acc_user.balance
                            
                            print("===========================================\n")
                            print("\tDeposit Amount Successfully")
                            print("\n===========================================")
                            print(f"Amount: {deposit_Amount}\n")
                            
                            deposit = data_bank.transaction(deposit_category,deposit_account_no,depoist_balance,depoist_date,time)
                            all_transaction.append(deposit)
                            acc_user.information()      
                            # return deposit_Amount , all_transaction
                    elif choice == 2:
                        print("===========================================")
                        print("\tWithdraw")
                        withdraw_amount = int(input("Enter the amount: Php"))
                        
                        if not withdraw_amount or withdraw_amount <= 0:
                            print("===========================================\n")
                            print("\tPlease enter valid amount\n")
                        elif withdraw_amount < 99:
                            print("===========================================\n")
                            print("\tPlease Withdraw more than Php100\n")
                        elif withdraw_amount > acc_user.balance:
                            print("===========================================\n")
                            print("\tInsufficient balance..\n")
                        else:
                            acc_user.balance -= withdraw_amount
                        
                            date1 = datetime.datetime.now()
                            withdraw_date = date1.date()
                            times = date1.strftime("%H:%M:%p")
                            withdraw_category = "Withdraw"
                            withdraw_account_no = acc_user.account_no
                            withdraw_balance = acc_user.balance
                        
                            
                            print("===========================================\n")
                            print("\tWithdraw Amount Successfully\n")
                            print("===========================================")
                            print(f"Amount: {withdraw_amount}\n")
                            
                            withdraw = data_bank.transaction(withdraw_category,withdraw_account_no,withdraw_balance,withdraw_date,times)
                            all_transaction.append(withdraw)
                            acc_user.information()
                        
                            # return withdraw_amount , all_transaction
                    elif choice == 3:
                        print("===========================================")
                        print("\tTransaction logs")
                        for transac in all_transaction:
                            if check_AccountNumber == transac.account_no:
                                transac.transaction_all()
                            else:
                                print("No Transaction yet")
                    elif choice == 4:
                        main()
                    else:
                        print("===========================================\n")
                        print("\tChoice only 1 - 3\n")
        else:
            print("===========================================\n")
            print("\tAccount not found")
            return
    
               
                       
                
def DisplayAccount():
        count = 1
        if not listOfAccount:
                print("===========================================\n")
                print("\tNo account exist.")
           
        else:        
            for data_user in listOfAccount:
                print("\n===========================================")
                print(f"Account # {count}")
                data_user.information()
                count += 1

 

def UpdateAccount():
    print("===========================================")
    print("\tUpdate Accounts")
    Update_acc = int(input("Enter Account no: "))
    
    for acc_number in listOfAccount:
        if Update_acc == acc_number.account_no:
            print("===========================================")
            print("\tYour all details\n")
            print(f"1.Account no  : {acc_number.account_no}")          
            print(f"2.Username    : {acc_number.username}")
            print(f"3.Age         : {acc_number.age}")        
            print(f"4.Gender      : {acc_number.gender}")
            print(f"5.Addrerss    : {acc_number.address}")
            print("6.Updates all")
            print("7.Return")
            
            choice = int(input("Enter the number you'd like to update: "))
            
            choice in [1,2,3,4,5,6,7]

            if choice == 1:
                print("===========================================")
                new_Account_no = int(input("Enter your new Account number: "))
                print("===========================================")
                print()
                print("\tUpdate new account number success.")
                acc_number.account_no = new_Account_no
                return new_Account_no
            
            elif choice == 2:
                print("===========================================")
                new_Account_name = input("Enter your new Account name: ")
                print("===========================================")
                print()
                print("\tUpdate new Account name success.")
                acc_number.username = new_Account_name
                return new_Account_name
            
            elif choice == 3:
                print("===========================================")
                new_Account_age = int(input("Enter your new age: "))
                print("===========================================")
                print()
                print("\tUpdate new age success")
                acc_number.age = new_Account_age
                return new_Account_age
            
            elif choice == 4:
                print("===========================================")
                new_Account_gender = input("Enter your new gender: ")
                print("===========================================")
                print()
                print("\tUpdate new gender sucess.")
                acc_number.gender = new_Account_gender
                return new_Account_gender
            
            elif choice == 5:
                print("===========================================")
                new_Account_Addrerss = input("Enter your new Addrerss: ")
                print("===========================================")
                print()
                print("\tUpdate new address success.")
                acc_number.address = new_Account_Addrerss
                return new_Account_Addrerss
            elif choice == 6:
                print("===========================================")
                newAccount_no =   int(input("Enter your new Account number : "))
                newAccount_name =     input("Enter your new Account name   : ")
                newAccount_age =  int(input("Enter your new age            : "))
                newAccount_gender =   input("Enter your new gender         : ")
                newAccount_address =  input("Enter your new address        : ")
                print("===========================================")
                print()
                print("\tUpdate your all details success.\n")
                acc_number.account_no = newAccount_no
                acc_number.username = newAccount_name
                acc_number.age = newAccount_age
                acc_number.gender = newAccount_gender
                acc_number.address = newAccount_address
                acc_number.information()
                return
            elif choice == 7:
                main()
            else:
                print("Choose valid choices")
    else:
        print("===========================================\n")
        print("\tAccount not found.")
                
                    
    

def BestAccounts(user,amount):

    print("===========================================")
    print("\tTop 3 Best Accounts for Php50,000")
    
    if not user:
        print("\t\tNo Top 3 Accounts")
    else:
        for data_user in listOfAccount:
            if data_user.balance >= amount:
               print(f"Username: {data_user.username}")
               print(f"Balanced: {data_user.balance}")       
                        
                        
def VIPAccounts(user):
    print("===========================================")
    print("\t\tVIP ACCOUNTS")
    if not user:
        print("\tDon't have Accounts exist")
    else:
        for balance_user in listOfAccount:
            if balance_user.balance >= 100000:
                print("===========================================")
                print("Category: PLATINUM")
                print(f"Account_no : {balance_user.account_no}")
                print(f"Username   : {balance_user.username}")
                print(f"Balanced   : {balance_user.balance}")
            elif  balance_user.balance >= 70000:
                print("Category: GOLD")
                print(f"Account_no : {balance_user.account_no}")
                print(f"Username   : {balance_user.username}")
                print(f"Balanced   : {balance_user.balance}")
            elif  balance_user.balance >= 50000:
                print("Category: SILVER")
                print(f"Account_no : {balance_user.account_no}")
                print(f"Username   : {balance_user.username}")
                print(f"Balanced   : {balance_user.balance}")
            else:
                print("Category: BRONZE")
                print(f"Account_no : {balance_user.account_no}")
                print(f"Username   : {balance_user.username}")
                print(f"Balanced   : {balance_user.balance}")
                                                        
def DeleteAccounts(Account_user):
    print("===========================================")
    print("\tDelete Account")
    if not Account_user:
        print("\tNo account exist")
    else:
        Acc_no = int(input("Enter your Account no: "))
        for check_user in listOfAccount:
            if Acc_no == check_user.account_no:
                print("===========================================\n")
                print("\tDelete Account Successfully")
                listOfAccount.remove(check_user)
                return
        else:
            print("===========================================\n")
            print("\tAccount not found")
            
               
def main():
    still_Progresing = True
     
    while still_Progresing:
        print()
        print("===========================================")
        print("\tChoice Category")
        print("1.Create Account")
        print("2.Use Existing Account")
        print("3.Display Accounts")
        print("4.Update Account")
        print("5.Best Accounts")
        print("6.VIP Accounts")
        print("7.Delete Accounts")
        print("8.Exit")
    
        try:        
            choice = int(input("Enter Choice Category: "))
            choice in [1,2,3,4,5,6,7,8]

            if choice == 1:
                CreateAccount()
            elif choice == 2:
                UseExistingAccount(listOfAccount)
            elif choice == 3:
                DisplayAccount()
            elif choice == 4: 
                UpdateAccount()
            elif choice == 5:
                BestAccounts(listOfAccount,50000)
            elif choice == 6:
                VIPAccounts(listOfAccount)
            elif choice == 7:
                DeleteAccounts(listOfAccount)
            elif choice == 8:
                print("===========================================\n")
                print("Programmed by: Christian Dave L. Alicaba")
                print("\n===========================================\n")
                return False
            else:
                print("===========================================\n")
                print("\tChoose only number exist..")
        except:
            print("===========================================\n")
            print("\tEnter valid number not WORDS..")

main()
                       