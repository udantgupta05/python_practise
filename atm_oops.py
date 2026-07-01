class Atm:
  def __init__(self):
    self.pin = ""
    self.balance = 0

    self.menu()

  
  def menu(self):
    print("Welcome User to the ATM Machine, how would you like to proceed?")
    while True:
        user_input = input("""
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        
        if user_input == "1":
            self.create_pin()
            
        elif user_input == "2":
            self.deposit()
            
        elif user_input == "3":
            self.withdraw()
        
        elif user_input == "4":
            self.check_balance()
        
        elif user_input == "5":
            print("")
            print("Thank You for using the ATM, visit again!")
            break
              
        else:
            print("")
            print("Invalid Choice, please try again!")
  
  
  def create_pin(self):
     print("")
     self.pin = input("Enter the PIN you want to set: ")
     if len(self.pin) == 4:
         print("PIN set up successful")
     
     else:
        print("Please enter 4 digit PIN only")
        self.pin = ""
        print("")
  

  def deposit(self):
      print("")
      if self.pin == "":
          print("Please Set-Up your pin first")
          return
      
      temp = input("Enter your PIN: ")
      if temp == self.pin:
          print("PIN Verification Successful")
          print("")
          amount = int(input("Enter the amount: "))
          self.balance = self.balance + amount
          print("Deposit Successful")
          
            
      else:
          print("Invalid PIN entered")
          


  def withdraw(self):
      print("")
      if self.pin == "":
          print("Please Set-Up your pin first")
          return
      
      temp = input("Enter your PIN: ")
      if temp == self.pin:
          print("Pin Verification Successful")
          print("")
          amount = int(input("Enter the amount: "))
          if amount <= self.balance:
              self.balance = self.balance - amount
              print("Amount Withdrawn Successfully")
              
      
          else: 
              print("Amount entered exceeds balance")
              
                
      else:
          print("Invalid PIN")
          
    

  def check_balance(self):
      print("")
      temp = input("Enter your pin: ")
      if temp == self.pin:
          print("Print Verification Successful")
          print(f"Your Balance is ${self.balance}")
    
      else: 
          print("Invalid PIN")


atm = Atm()

          