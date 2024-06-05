#RETURN BOOK MODULE 

import pickle
import book
import datetime
import datime
import MEMBERS
import borrow
from prettytable import PrettyTable



def return_book():        #THE MAIN PROGRAM OF RETURN BOOK MODULE

    global customer_name
    customer_name=input("Enter your name (in capital letters): ")
    
    member_check()


 
def member_check():         #TO CHECK WHETHER THE USER IS A MEMBER OF LIBRARY
    a=MEMBERS.member_record()
    list9=[]
    for j in a:
        list9.append(j[1])

    if customer_name in list9:
        for i in a:
            if customer_name in i[1]:
                global t
                t=int(input("Enter your membership ID: "))
                if customer_name==i[1] and t==i[0]:
            
                    member_id=[i[0]]
                    member_name=[i[1]]
                    member_dob=[i[2]]
                    member_book=[i[3]]
                    
                    if member_book[0]==None:
                        print("\n")
                        print("You have no books with you!")
                        break
        
                    tb=PrettyTable(["ID","NAME","DATE OF BORROWING","BOOK BORROWED"])
                    for i in range(0,1):
                        tb.add_row([member_id[0],member_name[0],member_dob[0],member_book[0]])
                    print(tb)

                    edit_stock(t)
                    edit_member()
                    payment(member_dob[0])
                    print("\n")
                    break
                else:
                    print("Your ID doen't match.")
    else:
        print('''Your name doesn't exist in our record.
You've never borrowed a book.''')   
                
            

def edit_stock(x):             #x=member id
    a=book.book_record() #DATA IS IN THE FORM [[id,name,author,cost],[id2,name2,author,cost2]]
    b=book.book_Id()  #DATA IS IN THE FORM [[id,name],[id2,name2]]
    c=borrow.return_removed_book()#DATA IS IN triple nested list

    for i in c:
        if customer_name==i[0][1] and x==i[0][0]:
            global w
            w=i[1]
            a.append(w)
            var1=w[0]
            var2=w[1]
            list3=[var1,var2]
            b.append(list3)
            c.remove(i)
            break
        else:
            pass
        
    a.sort()  #SORTING ACCORDING TO ID
    b.sort()
    book.quantity()

    f=open("book_stock.dat","wb")
    f1=open("book_ID.dat","wb")
    f2=open("book_borrow.dat","wb")

    pickle.dump(a,f)
    pickle.dump(b,f1)
    pickle.dump(c,f2)

    f.close()
    f1.close()
    f2.close()
    
            

def edit_member():
    a=MEMBERS.member_record()
    for i in a:
        if customer_name==i[1] and t==i[0]:
            i[2]=None  #CHANGES DATE FROM SMTH TO NONE
            i[3]=None   # CHANGES BOOK FROM SMTH TO NONE

    f=open("members.dat","wb")
    pickle.dump(a,f)
    f.close()



def payment(x):       #x is borrow date
    cost=w[3]
    y=datime.date()
    if (y-x)/datetime.timedelta(days=1)<=14:
        payment=cost
        print("The total amount to be paid (in Rs) is ",payment)
    else:
        fine=(((y-x)/datetime.timedelta(days=1))-14)*20
        payment=cost+fine
        print("The total amount to be paid (in Rs) is ",payment)

    x=0
    while x==0:
        while True:
            amount_pay=int(input("Enter amount to pay: "))
            if amount_pay==payment:
                break
            elif amount_pay>payment:
                print("Here is your change.")
                break
            else:
                print("Please pay the right amount.")
                print("\n")
        while True:
            confirm=input("Have you paid (y/n): ")
            if confirm in "yY":
                break
            else:
                print("Please confirm.")
        x=1



