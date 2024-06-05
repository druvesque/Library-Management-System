#MEMBERS MODULE

import pickle
import datime



def members_new():                  #TO ENTER DUMMY RECORDS IN THE BEGINNING
    f=open("members.dat","wb")
    f1=open("member_ID.dat","wb")
    record=[]
    m_id=[]
    member_id=10001
    while True:
        print("Member id: ",member_id)
        m_id.append(member_id)

        member_name=input('''Enter name of the member:
>   ''')

        member_dob=datime.date()


        member_book=input('''Enter the name of book:
>   ''')

        data=[member_id,member_name,member_dob,member_book]
        record.append(data)
        print("\n")

        ch=input("Do you want to add more records? (y/n): ")
        if ch in "nN":
            break
        member_id+=1

    pickle.dump(record,f)
    pickle.dump(m_id,f1)
    
    f.close()
    f1.close()



def member_record():            #[[id,name,date of borrow,book borrowed],[id2,name2,dob2,bb2]]
    f=open("members.dat","rb")
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
    f.close()
    return a




def member_Id():                  #[id1,id2,id3]
    f=open("member_ID.dat","rb")
    while True:
        try:
            a=pickle.load(f)
        except EOFError:
            break
    f.close()
    return a



def member_display():           #JUST TO DISPLAY
    f=open("members.dat","rb")
    while True:
        try:
            a=pickle.load(f)
            for i in a:
                print(i)
        except EOFError:
            break
    f.close()




def members():
    global member_name_list
    global member_id_list
    global dob_list
    global book_list

    member_name_list=[]
    member_id_list=[]
    dob_list=[]
    book_list=[]

    f=open("member.dat","rb")
    while True:
        try:
            a=pickle.load(f)
            for i in a:
                member_id_list.append(i[0])
                member_name_list.append(i[1])
                dob_list.append(i[2])
                book_list.append(i[3])
        except EOFError:
            break
    f.close()


def mem_nam():
    return(member_name_list)


def mem_id():
    return(member_id_list)


def dob_l():
    return(dob_list)


def book_list():
    return(book_list)



