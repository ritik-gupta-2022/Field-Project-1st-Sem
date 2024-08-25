
NamesOFClients = ['RAHUL', 'RITIK', 'RITIKA', 'RISHABH', 'RAUNAK']
ClientPins = ['0001', '0002', '0003', '0004', '0005']
ClientBalances = [10000, 20000, 30000, 40000, 50000]
ClientMobile= [9568537327,9658438534,5875984345,5487943753,5734900323]
ClientEmail=['rahul123@gmail.com','ritik123@gmail.com','ritika123@gmail.com','rishabh123@gmail.com','raunak123@gmail.com']
ClientAddress=['Agra','Mathura','Bareilly','Kanpur','Lucknow']
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 5
u = 0
while True:
    
    print("***********************************************************************")
    print("===========         WELCOME TO GLA BANKING SYSTEM          ============")
    print("***********************************************************************")
    print("===========         (A). New Account opening               ============")
    print("===========         (B). Money Withdrwal                   ============")
    print("===========         (C). Money Deposition                  ============")
    print("===========         (D). Balance Enquiry                   ============")
    print("===========         (E). Update Details                    ============")
    print("===========         (F). Balance Enquiry of all Account    ============")
    print("===========         (G). View User Details                 ============")
    print("===========         (H). Closing an Account                ============")
    print("===========         (I). Quit                              ============")
    print("***********************************************************************")

    
    def again_update_mobile():
        Mobile_no=int(input("Please enter your Mobile No. : "))
        if len(str(Mobile_no)) !=10:
            print("Enter Valid Mobile Number : ")
            again_update_mobile()
        if str(Mobile_no)[0]==0:
            print("Invalid Mobile Number")
            again_update_mobile()
    def again_deposit(c):
        n=c
        deposition=int(input("Enter amount to deposit : "))
        if deposition<n:
            print("Please enter required amount : ",c)
            again_deposit(n)
        return deposition
            
    def again_update_pin():
        pin = str(input("Please Write a four Pin to Secure your Account : "))
        if len(str(pin))!=4:
            print("Enter Valid Pin:")
            again_update_pin()
    global deposition
    
    EnterLetter = input("Select a Letter from the Above Box menu : ")
    if EnterLetter in ("a","A"):
        print(" New Account Opening")
        NumberOfClient= int(input("Number of Clients : "))
        u = u + NumberOfClient

        if u > 5:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            u = u - NumberOfClient
        else:
            while disk1 <= u:
                name = input("Write Your Fullname : ")
                name = name.upper()
                NamesOFClients.append(name)
                pin = str(input("Please Write a four Pin to Secure your Account : "))
                if len(str(pin))!=4:
                    print("Enter Valid Pin:")
                    again_update_pin()
                
                ClientPins.append(pin)
                Mobile_no=int(input("Please enter your Mobile No. : "))
                
                if len(str(Mobile_no)) !=10:
                    print("Enter Valid Mobile Number : ")
                    again_update_mobile()
                if str(Mobile_no)[0]==0:
                    print("Invalid Mobile Number : ")
                    again_update_mobile()
                
                ClientMobile.append(Mobile_no)
                Email=str(input("Enter your email to be registered : "))
                ClientEmail.append(Email)
                Address=str(input("Enter your permanent address : "))
                ClientAddress.append(Address)
                ClientBalance = 0
                ClientDeposition = int(input("Please Insert a Money to Deposit to Start an Account : "))
                ClientBalance = ClientBalance + ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\nName=", end=" ")
                print(NamesOFClients[disk2])
                print("Pin=", end=" ")
                print(ClientPins[disk2])
                print("Mobile No=",end=" ")
                print(ClientMobile[disk2])
                print("Email=",end=" ")
                print(ClientEmail[disk2])
                print("Address=",end=" ")
                print(ClientAddress[disk2])
                print("Balance=", "Rs", end=" ")
                print(ClientBalances[disk2], end=" ")
                disk1 = disk1 + 1
                disk2 = disk2 + 1
                print("\n")
                print("----New Client account created successfully !----")
                print("\n")
                print("Your Name is Available on the Client list now : ")
                print(NamesOFClients)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter in ("b","B"):
        v = 0
        print(" Cash Withdrawl ")
        while v < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        v = v + 1
                        print("Your Current Balance:","Rs", end=" ")
                        print(ClientBalances[w], end=" ")
                        print("\n")
                        ClientBalance = (ClientBalances[w])
                        ClientWithdrawal = int(input("Insert value to Withdraw : "))
                        if ClientWithdrawal > ClientBalance:
                            c=ClientWithdrawal-ClientBalance
                            print("Insufficient Funds")
                            print("Please Deposit a higher Value because your Balance mentioned above is not enough : ")
                            deposition = int(input("Enter Money to deposit"))
                            if(deposition<c):
                                print("Sorry....\nPlease Enter required Amount :",c)
                                deposition=again_deposit(c)
                                
                            ClientBalances[w] = ClientBalance + deposition
                            print("Your Current Balance:","Rs", end=" ")
                            print(ClientBalances[w], end=" ")
                            ClientBalances[w] = ClientBalances[w] - ClientWithdrawal
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            print("Your New Balance: ","Rs", ClientBalances[w], end=" ")
                            print("\n\n")
                        else:
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ","Rs", ClientBalance, end=" ")
                            print("\n")
            if v < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter in ("c","C"):
        print("Cash Deposition")
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("Your Current Balance: ", "Rs",end=" ")
                        print(ClientBalances[w], end=" ")
                        ClientBalance = (ClientBalances[w])
                        print("\n")
                        ClientDeposition = int(input("Enter the value you want to deposit : "))
                        ClientBalance = ClientBalance + ClientDeposition
                        ClientBalances[w] = ClientBalance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", "Rs", ClientBalance, end=" ")
                        print("\n")
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter in ("d","D"):
        print("Balance Enquiry")
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("Your Current Balance: ", "Rs",end=" ")
                        print(ClientBalances[w], end=" ")
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        print("\n")   
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

    elif EnterLetter in ("e","E"):
        v = 0
        print(" Update Details")
        
        while v < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        v=v+1
                        Updt_name=input("Enter New Name : ")
                        Updt_name = Updt_name.upper()
                        Updt_pin=str(input("Enter New Pin : "))
                        if len(str(Updt_pin))!=4:
                            print("Enter Valid Pin :")
                            again_update_pin()
                        
                        Updt_Mobile=int(input("Enter New Mobile No. : "))
                        if len(str(Updt_Mobile)) !=10:
                            print("Enter Valid Mobile Number")
                            again_update_mobile()
                        if str(Updt_Mobile)[0]==0:
                            print("Invalid Mobile Number")
                            again_update_mobile()
                        Updt_Add=input("Enter New Address : ")
                        Updt_Add=Updt_Add.upper()
                    
                        NamesOFClients[w]=Updt_name
                        ClientPins[w]=Updt_pin
                        ClientMobile[w]=Updt_Mobile
                        ClientAddress[w]=Updt_Add
                        print("Details Updated successfully")
                        
            if v<1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter in ("f","F"):
        print("Balance Enquiry of all Accounts is selected by the Client")
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        while w <= len(NamesOFClients) - 1:
            print("->.Customer =", NamesOFClients[w])
            print("->.Balance =", "Rs", ClientBalances[w], end=" ")

            print("\n")
            w = w + 1
        print("\n")   
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif EnterLetter in ('g','G'):
        print("View User Details")
        x=0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("USER NAME      : ",NamesOFClients[w])
                        print("USER MOBILE_NO : ", ClientMobile[w])
                        print("USER EMAIL ID  : ", ClientEmail[w])
                        print("USER ADDRESS   : ",ClientAddress[w])
                        
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        print("\n")   
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")

    elif EnterLetter in ("h","H"):
        print("Closing Account Permanently")
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            name = name.upper()
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("Please Confirm You want to close your Account")
                        ans=input("Enter A for YES - \n and B for NO - ")
                        ans=ans.upper()
                        if ans in("a","A"):
                            NamesOFClients.pop(w)
                            ClientPins.pop(w)
                            ClientBalances.pop(w)
                            ClientMobile.pop(w)
                            ClientEmail.pop(w)
                            ClientAddress.pop(w)
                            print("Your Account has been successfully Deleted")
                            print("Thank you for using our Services")
                        elif ans in("b","B"):
                            print("You have selected not to delete the account")
                        else:
                            print("Invalid Choice")
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        print("\n")   
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        
    elif EnterLetter in ("i","I"):
        print("Exit")
        print("Thank you for using our banking system!")
        print("\n")
        print("Thank You and Come again")
        print("Have a Nice Day")
        break            
    else:
        print("Invalid option selected by the Client")
        print("Please Try again!")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")





