Database={
    'eddygrant':{
        'name': 'Sachin',
        'age':22,
        'email':'eddyXXXXgmail.com',
        'password':'red@123',
        'amount':20000
    },
    'sachin':{
        'name':'Tanuj',
        'age':25,
        'email':'tanuj@gmail.com',
        'password':'red@123',
        'amount':10000
    }
}
while(1<3):
    user_input=int(input('''Enter your Choice:
    1.Sign in
    2.Sign Up
    3.Exit '''))
    if(user_input==1):
        username=input("Enter username: ")
        if((username in Database)==True):
            user_password=input("Enter password: ")
            if((user_password in Database[username]['password'])==True):
                print("Welcome",Database[username]['name'])
                while(1<4):
                    user_input1=int(input('''Enter your Choice:
                    1. Check Balance
                    2. Deposit Balance
                    3. Withdrawl
                    4. Change Password
                    5. Log out    '''))
                    if(user_input1==1):
                        print('Current Balance:',Database[username]['amount'])
                    elif(user_input1==2):
                        depositamt=int(input("Enter amount: "))
                        Database[username]['amount']=Database[username]['amount']+depositamt
                    elif(user_input1==3):
                        withdrawlamt=int(input("Enter amount: "))
                        print("Collect your Cash ",withdrawlamt)
                        Database[username]['amount']=Database[username]['amount']-withdrawlamt
                    elif(user_input1==4):
                        while(1<5):
                            old_password=input("Enter old password:")
                            if(old_password==Database[username]['password']):
                                New_password=eval(input("Enter new password:"))
                                Confirm_password=eval(input("Enter confirm new password:"))
                                if(New_password==Confirm_password):
                                    Database[username]['password']=New_password
                                    print("Password successfully changed")
                                    break
                                else:
                                    print("Password not matched")
                            else:
                                print("Enter password correctly")
                    elif(user_input1==5):
                        break
            elif((user_password in Database[username]['password'])==False) :
                print('Forgot password')
                user_email=input( 'Enter the email:')
                if(user_email in Database[username]['email']==True):
                    Database[username]['password']=input('New password:')
        else:
            print("Username is Not Found")
    elif(user_input==2):
        username=eval(input("Enter your username: "))
        name=eval(input("Enter your name: "))
        age=eval(input("Enter your age: "))
        email=eval(input("Enter your email: "))
        password=eval(input("Enter your password: "))
        amount=eval(input("Enter your amount: "))
        Database[username]={'name':name,'age':age,'email':email,'password':password,'amount':amount}
        print("Username successfully created")
    elif(user_input==3):
        break
            












        
