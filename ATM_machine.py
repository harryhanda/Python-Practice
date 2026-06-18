user_pin = "1124"
Balance  = int(10000)
count = 0
while True:
    pin = input("Enter your pin: ")
    if pin == user_pin:
        print("Welcome , what do you want to do?")
        print("1. check balance")
        print("2. withdraw")
        print("3. Deposit")
        print("4. Exit")
        while True:
         choice = int(input("Enter your choice: "))
         if choice == 1:
            print(f"Your balance is: ₹{Balance:.2f}")
         elif choice == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > Balance:
                print("Insufficient Balance")
            else:
                Balance -= amount
                print(f"You hav withdrawn ₹{amount:.2f} and your new balance is ₹{Balance:.2f}")
         elif choice == 3:
            amount = int(input("Enter the amount you wanbt to add: "))
            Balance += amount 
            print(f"Your new balance is ₹{Balance:.2f}")
         elif choice == 4:
            print("Thank you for using our ATM machine. Have a nice day sir/madam! ")
            break
    else:   
         print("Invalid pin try again ")
         count += 1 
         if count == 3:
             print("Too many attempts. Your accoubt have been locked. please contact your bank for more information. ")
             break