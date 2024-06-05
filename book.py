#BOOKS MODULE


import pickle
#from matplotlib import pyplot as plt      #CORRECT IT!!!!!!!!!!!!!!!!!


def book_new():             #THIS IS TO PRELIMINARILY ADD DATA INTO FILE
    f=open("book_stock.dat","wb")
    f1=open("book_ID.dat","wb")
    
    record=[]
    b_id=[]
    book_id=1011
    
    while True:
        print("Book ID: ",book_id)

        book_name=input('''Enter name of the book:
>   ''')
        data1=[book_id,book_name]
        b_id.append(data1)
        
        author_name=input('''Enter name of author:
>   ''')
        
        cost=int(input('''Enter cost of the book:
>   '''))
        list_book=[book_id,book_name,author_name,cost]
        record.append(list_book)

        ch=input('''Do you want to enter more records (y/n):
>   ''')
        print("\n")
        if ch in "nN":
            break
        book_id+=1

    pickle.dump(b_id,f1)
    pickle.dump(record,f)

    f1.close()
    f.close()



def book_record():               # VALUE IS BEING STORED LIKE [[id1,name1,author1,cost1],[id2,name2,author2,cost2]]
    
    f=open("book_stock.dat","rb")
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return a



def book_Id():               # VALUE IS BEING STORED LIKE [[id1,name1],[id2,name2]]         #STORES BOTH ID AND NAME 
    f=open("book_ID.dat","rb")                                                              # TO ACCOMODATE SAME BOOKS WITH DIFFERENT ID'S
    
    while True:
        try:
            s=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return s



def add_book():            #TO APPEND DATA IN THE FILE
    b=book_record()        #WE DO NOT USE THE APPEND METHOD, BUT THE WRITE METHOD OF FILE TO APPEND DATA
    p=book_Id()
    lst=[]
    
    for j in p:
        lst.append(j[0])
        
    b_id=lst[len(lst)-1]+1
    while True:
        print("Book ID: ",b_id)

        book_name=input('''Enter name of the book:
>   ''')
        data2=[b_id,book_name]
        p.append(data2)             # FOR BOOK ID
        
        author_name=input('''Enter name of author:
>   ''')
        
        cost=int(input('''Enter cost of the book:
>   '''))
        list_book=[b_id,book_name,author_name,cost]
        b.append(list_book)             #FOR BOOK STOCK

        ch=input('''Do you want to enter more records (y/n):
>   ''')
        print("\n")
        if ch in "nN":
            break
        b_id+=1

    f=open("book_stock.dat","wb")    # INSTEAD OF USING APPEND MODE WE CHOSE THIS METHOD
    f1=open("book_ID.dat","wb")   #[[book id,name],[book id2,name2]]
    
    pickle.dump(b,f)
    pickle.dump(p,f1)
    
    f.close()
    f1.close()

    print("Data has been added.")

    
def book_display():                #JUST TO DISPLAY THE EXISTING DATA
    f=open("book_stock.dat","rb")
    while True:
        try:
            a=pickle.load(f)
            for i in a:
                print(i)
        except EOFError:
            break
    f.close()



def quantity():                    #TO COUNT THE NUMBER OF BOOKS BY PARTICULAR NAME
    b=book_record()               #for book stock
    record=[]
    book_name=[]
    
    for i in b:
        book_name.append(i[1])     # [[book_name1,qty1],[book_name2,qty2]]
    for j in book_name:
        quantity=[j,book_name.count(j)]
        record.append(quantity)

    f=open("quantity.dat","wb")
    pickle.dump(record,f)
    f.close()




def return_quantity():        #RETURNS THE QUANTITY IN ONE VARIABLE        DATA IS STORED LIKE [[name,quantity][name1,quantity1]]
    quantity()
    qty=[]
    f=open("quantity.dat","rb")
    while True:
        try:
            a=pickle.load(f)
            for i in a:
                qty.append(i)
        except EOFError:
            break
    f.close()
    return qty



def book():                   #JUST ANOTHER METHOD TO READ AND RETURN TO VARIABLE
    global book_id_list
    global book_name_list
    global author_name_list
    global book_cost_list
    
    book_id_list=[]
    book_name_list=[]
    author_name_list=[]
    book_cost_list=[]

    f=open("book_stock.dat","rb")
    while True:
        try:
            s = pickle.load(f)
            for i in s:
                book_id_list.append(i[0])
                book_name_list.append(i[1])
                author_name_list.append(i[2])
                book_cost_list.append(i[3])

        except EOFError:
            break
        
    f.close()

def books_id():
    return(book_id_list)

def books_list():
    return(book_name_list)

def authors_list():
    return(author_name_list)

def books_cost():
    return(book_cost_list)


def hybrid():            #TO STORE DATA IN THE FORMAT  [[name,author,quantity,cost],[name2,author2,quantity2,cost2]]
    a=book_record()      #for book stock  [id,name,author,cost]
    b=return_quantity()  #for quantity       [name,quantity]
    search=[]            #[name,author,quantity,cost]
    
    for i in a:          #TO FUSE BOOKNAME,AUTHORNAME,QUANTITY,COST IN FILE
        for j in b:
            if i[1]==j[0]:
                record=[i[1],i[2],j[1],i[3]]
        search.append(record)

    f=open("hybrid.dat","wb")
    pickle.dump(search,f)
    f.close()
    


def return_hybrid():            #IT IS RETURNING DATA FROM THE FILE
    hybrid()
    f=open("hybrid.dat","rb")
    while True:
        try:
            s=pickle.load(f)
        except EOFError:
            break
        
    f.close()
    return s

 
def book_Id_Display():        #JUST TO SEE THE DATA IN BOOK ID
    f=open("book_ID.dat","rb")
    while True:
        try:
            s=pickle.load(f)
            for i in s:
                print(i)
        except EOFError:
            break
    f.close()


def bar_graph():      
    x=return_quantity()
    record=[]
    for j in x:               #TO SELECT DISTINCT BOOKS FROM THE BOOK STOCK
        if j not in record:
            record.append(j)
    
    list_book=[]
    list_qty=[]
    
    for i in record:
        list_book.append(i[0])
        list_qty.append(i[1])
        
    fig=plt.figure()
    ax=fig.add_axes([0,1,3,3])
    ax.bar(list_book,list_qty)
    plt.show()



