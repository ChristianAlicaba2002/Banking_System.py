class transaction:
    #Transaction_User
        def __init__(self,category,account_no,balance,date,time):
            self.category = category
            self.account_no = account_no
            self.balance = balance
            self.date = date
            self.time = time
            
            
        def transaction_all(self):
            print("===========================================")
            print(f"-Category   : {self.category}")      
            print(f"-Account no : {self.account_no}")          
            print(f"-Balanced   : {self.balance}")
            print(f"-Date       : {self.date}")
            print(f"-Time       : {self.time}")
            
    

class userAccount:
        #Create_USer
        def __init__(self,account_no,username,age,gender,address,balance):
            self.account_no = account_no
            self.username = username
            self.age = age
            self.gender = gender
            self.address = address
            self.balance = balance
            
                

        def information(self):     
            print(f"\t-Account no : {self.account_no}")          
            print(f"\t-Username   : {self.username}")
            print(f"\t-Age        : {self.age}")        
            print(f"\t-Gender     : {self.gender}")
            print(f"\t-Addrerss   : {self.address}")
            print(f"\t-Balanced   : {self.balance}")
        
