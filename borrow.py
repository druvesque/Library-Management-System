#BORROW MODULE

import pickle
import book
import datime
import search
import MEMBERS


def borrow():         #THE MAIN PROGRAM OF BORROWING THE BOOK
    print('''

FEW INSTRUCTIONS...
1. YOU CAN BORROW ONLY 1 BOOK AT A TIME

2. YOU HAVE TO RETURN THE BOOK IN 2 WEEKS

3. WARNING !!!!! THERE IS A PENALTY FOR RETURNING THE BOOK AFTER 2 WEEKS

''')
    global customer_name
    customer_name=input("Enter your name (in capital letters): ")

    customer()




def customer():             #PROGRAM TO CHECK WHETHER THE CUSTOMER IS A MEMBER OR A NEW CUSTOMER
    
    while True:
        ch=input("Are you a new customer? (y/n): ")
        if ch in "nNyY":
            break
        else:
            print("Please input either y or n.")
            print("\n")

    if ch in "nN":
        member_borrow()

    elif ch in "yY":
        new_customer()

    else:
        pass





def new_customer():        #IF THE USER IS A NEW CUSTOMER
    con=search.searching() #con IS NAME OF THE BOOK
    y=0
    while y==0:
        if con==None:
            y=1
            break
        else:
            d=borrow_date()
            s=add_member(customer_name,d,con)
            remove_book(s,con)
            print("\n")
            print("Here is your book.")
            y=1
            break


def add_member(x,y,z):        #TO ADD THE MEMBER IN THE FILE    x=name of the member  y=date of borrowing of the book  z=name of the book borrowed
     
    a=MEMBERS.member_record()
    b=MEMBERS.member_Id()
    m_id=b[len(b)-1]+1

    b.append(m_id)

    member_name=x
    member_dob=y
    member_book=z

    data=[m_id,member_name,member_dob,member_book]
    a.append(data)

    f=open("members.dat","wb")
    f1=open("member_ID.dat","wb")
    pickle.dump(a,f)
    pickle.dump(b,f1)
    f.close()
    f1.close()

    print("Your membership id is: ",m_id,". Please remember it.")
    print("\n")
    return m_id




def borrow_date():     #TO FIND OUT THE DATE OF BORROWING
    c=datime.date()
    return c




def return_removed_book():    #DATA IS STORED IN THIS FILE IN THE FORMAT [[[member id,name],[book id, name,author,cost]],[[member id2,name2],[book id2, name2,author2,cost2]]] 
    f=open("book_borrow.dat","rb")                                          #[[[10001,HP:DH],[1095,HP:DH,JK,400]],[[10002,HP:PS],[2045HP:PS,JK,500]]]                   
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
    f.close()
    return a





def remove_book(x,y):    #x=member id and y=book name  #I have to add data to book_borrow.dat in the required form [[member id,name],[book details]]    #DATA IS REMOVED FROM THE STOCK
    
    a=book.book_record()     #REMOVAL OF BOOK IS 
    b=book.book_Id()
    c=return_removed_book()
    list3=[x,customer_name]
    
    for i in a:
        if y==i[1]:
            list4=[list3,i]
            c.append(list4)
            var=i[0]
            a.remove(i)
            break
        
    for j in b:
        if var==j[0] and y==j[1]:
            b.remove(j)
            break

    f=open("book_stock.dat","wb")
    f1=open("book_ID.dat","wb")
    f2=open("book_borrow.dat","wb")         # DATA IS STORED IN THE FORM [[[mid1,name1],[id1,book1,author1,cost1]],[[mid2,name2],[id2,book2,author2,cost2]]]

    pickle.dump(a,f)
    pickle.dump(b,f1)
    pickle.dump(c,f2)

    f.close()
    f1.close()
    f2.close()




def member_borrow():                       # IF THE USER IS ALREDY A MEMBER THEN THS FUNCTION COMES INTO USE
    a=MEMBERS.member_record()
    list10=[]
    for j in a:
        list10.append(j[1])

    if customer_name in list10:
        for i in a:
            if customer_name==i[1]:
                global t
                t=int(input("Enter your membership id: "))
                if customer_name==i[1] and t==i[0]:

                    if i[3]!=None:
                        print('''You've alredy borrowed a book.
In order to borrow another one please RETURN the older book.''')
                        break

                    elif i[3]==None:
                        con=search.searching()
                        remove_book(t,con)
                        i[2]=borrow_date()   #CHANGES DATE OF BORROWING FROM NONE TO CURRENT DATE
                        i[3]=con            #CHANGES BOOK NAME FROM NONE TO BOOK HE BORROWED  #EARLIER i[3]=None

                        f=open("members.dat","wb")
                        pickle.dump(a,f)
                        f.close()

                    else:
                        pass
                else:
                    print("Your ID doesn't match.")
                    customer()
    else:
        print("Your name doesn't exist in our record.") 
            


