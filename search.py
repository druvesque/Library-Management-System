#search module

import pickle
import book
from prettytable import PrettyTable

def searching():
    a=book.return_hybrid()   # DATA IS IN THE FORM  [[name,author,quantity,cost],[name2,author2,quantity2,cost2]]
    x=0
    temp_list=[]
    while x==0:
        book_name=input('''Enter name of the book you want to search

(Please enter the name in capital letters)
>   ''')
       
        for i in a:
            if book_name==i[0]:
                temp_list = i
       
                x=1
                break
            else:
                temp_list=[]
                x=1
                continue
           
        if len(temp_list)==0:
            print("Sorry the book is unavailable.")
            print("\n")
        elif len(temp_list)!=0 and (temp_list[2]<=0):
            print("Sorry the book is out of stock.")
    

        else:
            book_name=[temp_list[0]]
            author=[temp_list[1]]
            qt=[temp_list[2]]
            cost=[temp_list[3]]
           
            tb=PrettyTable(["BOOK","AUTHOR","QUANTITY","COST"])
            for i in range(0,1):
                tb.add_row([book_name[0],author[0],qt[0],cost[0]])
            print(tb)


            return book_name[0]
       
        while True:
            ch = input("Do you want to continue(y/n)?    ")
            if ch in 'yY':
                break
            elif ch in 'nN':
                break
            else:
                print("Please avoid mistyping characters. ")
                
        if ch in "nN":
            break
        else:
            x=0


               


