#ADMIN MODULE


import pickle
import book
import staff



def admin_details():         #THIS IS TO ADD DATA PRELIMINARILY
    f=open("admin.dat","wb")
    
    admin_name=input("Name of the admin (in capital letters): ")
    admin_password=input("Password of the admin: ")
    a=[admin_name,admin_password]
    
    pickle.dump(a,f)
    f.close()



def admin_record():            #THIS RETURNS THE ADMIN'S DATA TO A VARIABLE
    f=open("admin.dat","rb")
    
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return a



def update_admin():          #TO UPDATE ADMIN'S DATA
    b=admin_record()
    
    print('''What do you want to update?:
1. ADMIN CREDENTIALS
2. ADMIN PASSWORD
''')
    
    p=int(input("Enter your choice: "))
    print("\n")
    
    if p==1:
        admin_name=input("Enter the name (in capital letters): ")
        admin_pass=input("Enter the password: ")
        admin=[admin_name,admin_pass]
        f=open("admin.dat","wb")
        pickle.dump(admin,f)
        f.close()
        print("\n")
        print("Credentials have been updated.\n")
        
    elif p==2:
        old_pass=input("Enter old password: ")
        print("\n")
        
        if b[1]==old_pass:
            print('''TIP! To make your password stronger
INCLUDE NUMBERS, SPECIAL CHARACTERS AND CAPITAL LETTERS IN IT''')
            print("\n")
            new_pass=input("Enter new password: ")
            b[1]=new_pass
            
            f1=open("admin.dat","wb")
            pickle.dump(b,f1)
            f1.close()
            print("Password has been successfully changed.\n")
            print("\n")
            
        else:
            print("Your password doesn't match")
            
    else:
        print("Choose a valid option.")




def admin_display():       #TO DISPLAY ADMIN'S DATA
    f=open("admin.dat","rb")
    
    while True:
        try:
            a=pickle.load(f)
            print(a)
        except EOFError:
            break
        
    f.close()




def admin_login():         #LOGIN FOR ADMIN
    z=admin_record()
    
    while True:
        name=input("Enter your name: ")
        
        if name==z[0]:
            password=input("Enter your password: ")
            
            if password==z[1]:
                print("\nYou've successfully logged in")
                print("\n")
                return True
            
            else:
                print("You've entered wrong password")
        
        else:
            print('''Login failed
Please try again\n''')
            return False



def admin():            #THE MAIN PROGRAM OF ADMIN
    x=admin_login()
    t=0
    while t==0:
        if x==True:
            print('''Please choose from the following:

1. UPDATE YOUR CREDENTIALS
2. ADD STAFF MEMBER
3. DELETE STAFF MEMBER
4. DISPLAY THE DATA OF STAFF MEMBERS
5. SEE THE BOOK-QUANTITY STATUS

Enter the corresponding number
''')
            while True:
                y=int(input("Enter your choice: "))
                print("\n")

                if y==1:
                    update_admin()
                    break

                elif y==2:
                    staff.add_staff()
                    print("\n")
                    break

                elif y==3:
                    staff.delete_staff()
                    print("\n")
                    break

                elif y==4:
                    staff.staff_display()
                    print("\n")
                    break

                elif y==5:
                    book.bar_graph()
                    break

                else:
                    print("Please enter a valid option.")

            while True:
                e=input("Do you want to use the program? (y/n): ")
                print("\n")
                if e in "nN":
                    t=1
                    break
                elif e in "yY":
                    t=0
                    break
                else:
                    print("Please input either y or n.")
                    
                
        else:
            break





