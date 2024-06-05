#STAFF MODULE


import pickle
import search
import book
from prettytable import PrettyTable



def staff_new():                  #THIS IS TO ADD DATA PRELIMINARILY
    f=open("staff.dat","wb")
    f1=open("staff_ID.dat","wb")
    
    record=[]
    s_id=[]
    staff_id=201
    
    while True:
        print("Staff ID: ",staff_id)
        s_id.append(staff_id)

        staff_name=input('''Enter name of the staff member:
>   ''')
        
        staff_ph=int(input('''Enter contact number of staff member:
>   '''))
        
        staff_pass=(input('''Enter password of staff:
>   '''))
        list_staff=[staff_id,staff_name,staff_ph,staff_pass]
        record.append(list_staff)

        ch=input('''Do you want to enter more records (y/n):
>   ''')
        print("\n")
        if ch in "nN":
            break
        staff_id+=1

    pickle.dump(s_id,f1)
    pickle.dump(record,f)

    f1.close()
    f.close()



def staff_record():                      #THIS IS TO ADD DATA TO A SINGLE VARIABLE
    f=open("staff.dat","rb")
    
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return a



def staff_Id():                         #THIS STORE ID'S IN A SINGLE VARIABLE
    f=open("staff_ID.dat","rb")
    
    while True:
        try:
            s=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return s




def add_staff():               #THIS IS TO ADD STAFF
    b=staff_record()
    p=staff_Id()
    s_id=p[len(p)-1]+1
    while True:
        print("Staff ID: ",s_id)
        p.append(s_id)

        staff_name=input('''Enter name of the staff member:
>   ''')
        
        staff_ph=int(input('''Enter contact number of staff member:
>   '''))
        
        staff_pass=(input('''Enter password of staff:
>   '''))
        list_staff=[s_id,staff_name,staff_ph,staff_pass]
        b.append(list_staff)

        ch=input('''Do you want to enter more records (y/n):
>   ''')
        print("\n")
        if ch in "nN":
            break
        s_id+=1

    f=open("staff.dat","wb")
    f1=open("staff_ID.dat","wb")
    
    pickle.dump(b,f)
    pickle.dump(p,f1)
    
    f.close()
    f1.close()
    
    print("Record Updated.")
    print("\n")



def delete_staff():              #THIS IS TO DO DELETE DATA OF STAFF
    b=staff_record()             #PEOPLE WITH SAME NAME CAN'T APPOINTED IN THE LIBRARY
    p=staff_Id()
    s=input('''Enter the name of the staff member you want to delete:
>   ''')
    a=[]
    for i in b:
        if i[1]!=s:
            a.append(i)
            
    f=open("staff.dat","wb")
    pickle.dump(a,f)
    f.close()




def update_staff(x):        #x is name    #THIS IS TO UPDATE STAFF'S DATA 
    b=staff_record()
    a=[]
    for i in b:
        if i[1]==x:
            print('''What do you want to update?
1.Your Phone Number
2.Your Password
''')
            
            c=int(input("Enter your choice: "))
            
            if c==1:
                phone=int(input("Enter your phone number: "))
                i[2]=phone
                a.append(i)
            
                
            elif c==2:
                old_pass=input("Enter your old password: ")
                if i[3]==old_pass:
                    new_pass=input("Enter your new password: ")
                    i[3]=new_pass
                    a.append(i)
                    print("Record Updated")
                    
                else:
                    print("Wrong Password")
                    
            else:
                print("Please enter a valid option.")
                
        elif i[1]!=x:
            a.append(i)
            

    f=open("staff.dat","wb")
    pickle.dump(a,f)
    f.close()



def staff_display():             #THIS IS TO DISPLAY DATA OF STAFF
    a=staff_record()
    list_id=[]
    list_name=[]
    list_ph=[]
    list_pass=[]
    for i in a:
        list_id.append(i[0])
        list_name.append(i[1])
        list_ph.append(i[2])
        list_pass.append(i[3])

    columns=["Staff ID","Staff Name","Contact","Password"]      
    myTable=PrettyTable()

    myTable.add_column(columns[0],list_id)
    myTable.add_column(columns[1],list_name)
    myTable.add_column(columns[2],list_ph)
    myTable.add_column(columns[3],list_pass)

    print(myTable)
    


def staff_login():            #THIS IS FOR LOGIN OF STAFF
    d=staff_record()
    list_name=[]
    
    global staff_login_name
    staff_login_name=input("Enter your name (in capital letters): ")

    for j in d:
        list_name.append(j[1])

    if staff_login_name in list_name:
        while True:
            for i in d:
                if staff_login_name==i[1]:
                    password=input("Enter your password: ")
                    if staff_login_name==i[1] and password==i[3]:
                        print("\nYou've successfully logged in.\n")
                        return True

                    else:
                        print("You've entered wrong password.")

                else:
                    pass
    else:
        print('''Login failed
Please try again\n''')
        return False




    
def staff():           #THIS IS THE MAIN PROGRAM OF STAFF MODULE
    g=staff_login()
    p=0
    while p==0:
        if g==True:
            print('''Please choose from the following:

1. UPDATE YOUR CREDENTIALS (PHONE NUMBER OR PASSWORD)
2. ADD BOOKS TO THE DIRECTORY
3. SEE THE BOOK-QUANTITY STATUS
4. SEARCH FOR A PARTICULAR BOOK

Enter the corresponding number
''')
            while True:
                z=int(input("Enter your choice: "))
                print("\n")

                if z==1:
                    update_staff(staff_login_name)
                    break

                elif z==2:
                    book.add_book()
                    break

                elif z==3:
                    book.bar_graph()

                elif z==4:
                    search.searching()
                    break

                else:
                    print("Please choose a valid option.")
                    print("\n")
            while True:
                q=input("Do you want to use the program again? (y/n): ")
                if q in "nN":
                    p=1
                    break
                elif q in "yY":
                    p=0
                    break
                else:
                    print("Please input either y or n.")
        else:
            break



