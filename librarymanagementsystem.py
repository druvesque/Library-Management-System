#LIBRARY MANAGEMENT SYSTEM

#MENU DRIVEN PROGRAM

import book
import admin
import borrow
import staff
import return_book


print('''
|||||  WELCOME TO ALL ELITE LIBRARY  |||||
''')


def library():     #MAIN PROGRAM

    print('''Please choose:-

1. ADMINISTARATOR
2. STAFF MEMBER
3. CUSTOMER

''')

    while True:
        u=int(input('''Enter your choice: '''))
        if u==1 or u==2 or u==3:
            break
        else:
            print("Please input 1,2 or 3.")
            print("\n")

    if u==1:
        admin.admin()

    elif u==2:
        staff.staff()

    elif u==3:
        outsider()





def outsider():
    print('''Please choose from the following:

1. BORROW A BOOK
2. RETURN THE BOOK
3. EXIT THE LIBRARY

Enter the corresponding number:-
''')
    while True:

        number=int(input("Enter your choice: "))

        if number==1:
            borrow.borrow()
            print("\n")
            print("Thanks for borrowing book from our library")
            print("\n")
            break

        elif number==2:
            return_book.return_book()
            print("\n")
            print("Thanks for using our library.")
            print("\n")
            break

        elif number==3:
            print("Thanks for visiting our library.")
            break

        else:
            print("Please input either 1,2 or 3.")



library()

