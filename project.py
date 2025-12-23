import sys
import time
import mysql.connector as mycon
con=mycon.connect(host='localhost',user='',password='',database="Project")
from tabulate import tabulate
import csv
import matplotlib.pyplot as mpt
from PIL import Image

#Random modules   
    
def welcome():
    time.sleep(1)
    print("-"*116)
    f1=open("welcome.txt","w+")
    l1=["Welcome to the BeatBlitz Awards Voting System. This project was made by C.V.Akshaya of class 12A."]
    for i in l1:
        f1.writelines(l1)
    f1.close()
    f1=open("welcome.txt","r+")
    rec=f1.readlines()
    for j in rec:
        print(j)
    f1.close()
    time.sleep(1)
    print("-"*116)

#welcome()
    
def instructions():
    time.sleep(1)
    print("-"*116)
    f1=open("instructions.txt","w+")
    l1=["General instructions: \n1. The voter must vote for at least one category \n2. During login, if the wrong password is entered more than three times, you will be removed from the programme \n3. During signup, the password entered must be at least 8 characters"]
    for i in l1:
        f1.writelines(l1)
    f1.close()
    f1=open("instructions.txt","r+")
    rec=f1.readlines()
    for j in rec:
        print(j)
    f1.close()
    time.sleep(1)
    print("-"*116)
    
#instructions()
    
def thankyou():
    print()
    time.sleep(1)
    print("-"*116)
    f1=open("thankyou.txt","w+")
    l1=["Thank you for your time, have a great day!"]
    for i in l1:
        f1.writelines(l1)
    f1.close()
    f1=open("thankyou.txt","r+")
    rec=f1.readlines()
    for j in rec:
        print(j)
    f1.close()
    time.sleep(1)
    print("-"*116)
    
#thankyou()
    
def table():
    data=cursor.fetchall()
    cursor.close()
    tab=tabulate(data)
    print(tab)
    
#table()
    
def vote(T_Name,T_ID):
    cursor=con.cursor()
    cursor.execute("update {} set Count=Count+1 where ID={}".format(T_Name,T_ID))
    con.commit()
    
#vote()
    
def winner_tab1():
    con=mycon.connect(host='localhost',user='',password='',database="Project")
    cursor=con.cursor()
    cursor.execute("select * from Song_of_the_Year")
    data=cursor.fetchall()
    l=[]
    l.append(data)
    max=0          
    for i in l[0]:
        if i[4]>=max:
            max=i[4]
    list=[]
    for i in l[0]:
        if i[4]==max: 
            list.append([i[1],i[2],i[3]])
    if len(list)>1:
        print("Multiple winners:")
        for i in list:
            print(i) 
    else:
        print(list[0])
        
#winner_tab1()
        
def winner_tab2():
    con=mycon.connect(host='localhost',user='',password='',database="Project")
    cursor=con.cursor()
    cursor.execute("select * from Best_Music_Video")
    data=cursor.fetchall()
    l=[]
    l.append(data)
    max=0          
    for i in l[0]:
        if i[4]>=max:
            max=i[4]
    list=[]
    for i in l[0]:
        if i[4]==max: 
            list.append([i[1],i[2],i[3]])
    if len(list)>1:
        print("Multiple winners:")
        for i in list:
            print(i) 
    else:
        print(list[0])

#winner_tab2()
        
def winner_tab3():
    con=mycon.connect(host='localhost',user='',password='',database="Project")
    cursor=con.cursor()
    cursor.execute("select * from Album_of_the_Year")
    data=cursor.fetchall()
    l=[]
    l.append(data)
    max=0          
    for i in l[0]:
        if i[3]>=max:
            max=i[3]
    list=[]
    for i in l[0]:
        if i[3]==max: 
            list.append([i[1],i[2]])
    if len(list)>1:
        print("Multiple winners:")
        for i in list:
            print(i) 
    else:
        print(list[0])
        
#winner_tab3()
        
def suggestions():
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    cursor.execute("select * from Credentials")
    data=cursor.fetchall()
    usernames=[]
    for i in data:
        usernames.append(i[0])
    user=input("Enter username: ")
    while True:
        if user in usernames:
            break
        else:
            user=input("Enter correct username: ")
    suggestion=input("Please enter your suggestions if any: ")
    with open('suggestions.csv',mode="a",newline='') as f:
        write=csv.writer(f,delimiter=',')
        write.writerow([user,suggestion])
        print("Thank you for your suggestion!")
        
#suggestions()

def append_table(tbname):
    cursor=con.cursor()
    cursor.execute("use Project")
    cursor.execute("select * from " + tbname)
    data=cursor.fetchall()
    a_ids=[]
    for i in data:
        a_ids.append(i[0])
    return a_ids
        
#def append_table()

def plt1():
    cursor=con.cursor()
    cursor.execute("select * from Song_of_the_Year")
    data=cursor.fetchall()
    count=[]
    artist=[]
    for i in data:
        count.append(i[4])
    for i in data:
        artist.append(i[1])
    mpt.title("Song of the Year")
    mpt.pie(count,labels=artist,autopct="%2.1f%%",)
    mpt.show()
    
#plt1()
    
def plt2():
    cursor=con.cursor()
    cursor.execute("select * from Best_Music_Video")
    data=cursor.fetchall()
    count=[]
    artist=[]
    for i in data:
        count.append(i[4])
    for i in data:
        artist.append(i[1])
    mpt.title("Best Music Video")
    mpt.pie(count,labels=artist,autopct="%2.1f%%",)
    mpt.show()
    
#plt2()
    
def plt3():
    cursor=con.cursor()
    cursor.execute("select * from Album_of_the_Year")
    data=cursor.fetchall()
    count=[]
    artist=[]
    for i in data:
        count.append(i[3])
    for i in data:
        artist.append(i[1])
    mpt.title("Album of the Year")
    mpt.pie(count,labels=artist,autopct="%2.1f%%",)
    mpt.show()

#plt3()

#Voter signin/signup

def signup():
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    cursor.execute("select * from Credentials")
    data=cursor.fetchall()
    usernames=[]
    for i in data:
        usernames.append(i[0])
    username=input("Create username: ")
    while (username in usernames):
        print("Username already exists.")
        username=input("Re-enter username: ")     
    password=input("Create password: ")
    cp=""
    while (cp!=password):
        while len(password)<8:
            print("Password must contain atleast 8 characters")
            password=input("Please re-enter password: ")
        cp=input("Confirm password: ")
        if (cp!=password):
            print("Passwords do not match, please confirm password again: ")
            cp=input("Re-enter confirm password: ")
    cursor=con.cursor()
    cursor.execute("use Project")
    query="insert into Credentials (Username,Password) values(%s,%s)"
    val=(username,password)
    cursor.execute(query,val)
    con.commit()
    
#signup()

def signin():
    username=input("Enter username: ")
    password=input("Enter password: ")
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    cursor.execute("select * from Credentials")
    data=cursor.fetchall()
    rep=""
    
    for i in data:
        if i[0]==username:
            if i[1]!=password:
                for j in range(3):
                    print("Password is wrong")
                    rep=input("Re-enter password: ")
                    if (rep==i[1]):
                        print("Signed in successfully")
                        return ""
                print("Number of tries exceeded")
                sys.exit()
            elif i[1]==password:
                print("Signed in successfully")
                return ""                        
    print("Username doesn't exist")
    sys.exit()
    
#signin()    
    
    
#Admin module
    
def admin_signin():
    username=input("Enter admin username: ")
    password=input("Enter admin password: ")
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    cursor.execute("select * from Admin")
    data=cursor.fetchall()
    for i in data:
        if i[0]==username:
            if i[1]!=password:
                for j in range(3):
                    print("Password is wrong")
                    rep=input("Re-enter password: ")
                    if (rep==i[1]):
                        print()
                        print("Signed in successfully")
                        return ""
                print("Number of tries exceeded")
                sys.exit()
            elif i[1]==password:
                print()
                print("Signed in successfully")
                return ""
    print("Username doesn't exist")
    sys.exit()
    
#admin_signin()

def admin_add():
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    print("Choose the table in which a row is to be added")
    print()
    print("Options:\n1. Song of the Year\n2. Best Music Video\n3. Album of the Year")
    print()
    ch=int(input("Enter choice: "))
    print()
    if ch==1:
        id=int(input("Enter award ID: "))
        artist=input("Enter artist: ")
        song=input("Enter song: ")
        album=input("Enter album: ")
        count=0
        query="insert into Song_of_the_Year (id,artist,song,album,count) values(%s,%s,%s,%s,%s)"
        val=(id,artist,song,album,count)
        cursor.execute(query,val)
        con.commit()
        print()
        print("Row added successfully")
        print()
    elif ch==2:
        id=int(input("Enter award ID: "))
        artist=input("Enter artist: ")
        song=input("Enter song: ")
        album=input("Enter album: ")
        count=0
        query="insert into Best_Music_Video (id,artist,song,album,count) values(%s,%s,%s,%s,%s)"
        val=(id,artist,song,album,count)
        cursor.execute(query,val)
        con.commit()
        print()
        print("Row added successfully")
        print()
    elif ch==3:
        id=int(input("Enter award ID: "))
        artist=input("Enter artist: ")
        album=input("Enter album: ")
        count=0
        query="insert into Album_of_the_Year (id,artist,album,count) values(%s,%s,%s,%s)"
        val=(id,artist,album,count)
        cursor.execute(query,val)
        con.commit()
        print()
        print("Row added successfully")
        print()
    else:
        sys.exit()
        
#admin_add()

def admin_delete():
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    ch=0
    print("Choose the table from which a row is to be deleted")
    print()
    print("Options:\n1. Song of the Year\n2. Best Music Video\n3. Album of the Year")
    print()
    ch=int(input("Enter choice: "))
    print()
    if ch==1:
        id=int(input("Enter award id from which the row is to be deleted: "))
        while True:
            a_ids=append_table("Song_of_the_Year")
            if id in a_ids:
                query="delete from Song_of_the_Year where ID=%s"
                val=(id,)
                cursor.execute(query,val)
                con.commit()
                print("Row deleted successfully")
                break
            else:
                id=int(input("Enter existing award id: "))
        print()
    elif ch==2:
        id=int(input("Enter award id from which the row is to be deleted: "))
        while True:
            a_ids=append_table("Best_Music_Video")
            if id in a_ids:
                query="delete from Best_Music_Video where ID=%s"
                val=(id,)
                cursor.execute(query,val)
                con.commit()
                print("Row deleted successfully")
                break
            else:
                id=int(input("Enter existing award id: "))
        print()
    elif ch==3:
        id=int(input("Enter award id from which the row is to be deleted: "))
        while True:
            a_ids=append_table("Album_of_the_Year")
            if id in a_ids:
                query="delete from Album_of_the_Year where ID=%s"
                val=(id,)
                cursor.execute(query,val)
                con.commit()
                print("Row deleted successfully")
                break
            else:
                id=int(input("Enter existing award id: "))
        print()
    else:
        print("Please enter an existing option(1/2/3): ")
    
#admin_delete()

def view():
    con=mycon.connect(host='localhost',user='',password='')
    cursor=con.cursor()
    cursor.execute("use Project")
    print("Options:")
    print()
    print("1.Song of the Year")
    print("2.Best Music Video")
    print("3.Album of the Year")
    print()
    ch=int(input("Enter choice: "))
    if ch==1:
        print("ID\t  Artist\tSong\t          Album\t     Count")
        cursor.execute("select * from Song_of_the_Year")
        data=cursor.fetchall()
        cursor.close()
        tab=tabulate(data)
        print(tab)
    elif ch==2:
        print("ID\t  Artist\tSong\t          Album\t        Count")
        cursor.execute("select * from Best_Music_Video")
        data=cursor.fetchall()
        cursor.close()
        tab=tabulate(data)
        print(tab)
    elif ch==3:
        print("ID\t  Artist\tAlbum\t       Count")
        cursor.execute("select * from Album_of_the_Year")
        data=cursor.fetchall()
        cursor.close()
        tab=tabulate(data)
        print(tab)

#view()

#MAIN CODE
 
img=Image.open('poster.png')
img.show()

time.sleep(1)
print("-"*116)
print()
print()
time.sleep(1)
print("                                              BEATBLITZ AWARDS VOTING SYSTEM                                       ")
print()
print()
time.sleep(1)
print("-"*116)

print()
print()


time.sleep(1)
welcome()

print()
print()

time.sleep(1)
instructions()


#SIGN IN

print()
while True:
    print("Options: \n1. Admin\n2. Voter")
    print()
    ch=int(input("Enter choice: "))
    if ch==1:
        print()
        print("Please sign in to continue")
        admin_signin()
        print()
        print("What would you like to do?")
        print()
        print("Options: \n1. Add a row \n2. Delete a row \n3. View tables\n4. Exit")
        print()
        ch=int(input("Enter choice: "))
        if ch==1:
            admin_add()
        elif ch==2:
            admin_delete()
        elif ch==3:
            view()
        elif ch==4:
            sys.exit()
        else:
            print("No such option. Exiting...")
            sys.exit()
    elif ch==2:
        print()
        print("Options: \n1.Sign up\n2.Signin")
        print()
        ch=int(input("Enter choice: "))
        if ch==1:
            signup()
            break
        elif ch==2:
            signin()
            break
    else:
        sys.exit()
    

print("                                                                                                                                                                               ")
print("          MENU          ")
print("                                                                                                                                                                               ")


print("Award Name\t   Award ID")
cursor=con.cursor()
cursor.execute("select * from Awards")
data=cursor.fetchall()
cursor.close()
tab=tabulate(data)
print(tab)
cursor=con.cursor()

flag=[1,2,3]
used=[]
ctr=0

while (ctr==0):
    print()
    print("Options:")
    con.cursor()
    print("1. Vote")
    print("2. Exit")
    print()
    ch=int(input("Enter choice: "))
    f=[]
    if (ch==1):
        A_id=int(input("Please enter the Award ID of the category you'd like to vote for(1/2/3): "))
        print()
        if A_id in flag:
            if A_id==1:
                f.append(1)
                a_ids=append_table("Song_of_the_Year")
                print("ID\t  Artist\tSong\t          Album")
                cursor=con.cursor()
                cursor.execute("select ID,Artist,Song,Album from Song_of_the_Year")
                table()
                img=Image.open('song.jpg')
                img.show()
                T_id=int(input("Enter ID of the artist you'd like to vote for: "))
                while True:
                    if T_id in a_ids:
                        vote("Song_of_the_Year",T_id)
                        print("Your vote has been registered, thank you!")
                        plt1()
                        flag.remove(A_id)
                        used.append(A_id)
                        break
                    else:
                        T_id=int(input("Enter acceptable award id: "))
            elif A_id==2:
                f.append(2)
                a_ids=append_table("Best_Music_Video")
                print("ID\t  Artist\tSong\t          Album")
                cursor=con.cursor()
                cursor.execute("select ID,Artist,Song,Album from Best_Music_Video")
                table()
                img=Image.open('video.jpg')
                img.show()
                T_id=int(input("Enter ID of the artist you'd like to vote for: "))
                
                while True:
                    if T_id in a_ids:
                        vote("Best_Music_Video",T_id)
                        print("Your vote has been registered, thank you!")
                        plt2()
                        flag.remove(A_id)
                        used.append(A_id)
                        break
                    else:
                        T_id=int(input("Enter acceptable award id: "))
            elif A_id==3:
                f.append(3)
                a_ids=append_table("Album_of_the_Year")
                print("ID\t  Artist\tAlbum\t")
                cursor=con.cursor()
                cursor.execute("select ID,Artist,Album from Album_of_the_Year")
                table()
                img=Image.open('album.jpg')
                img.show()
                T_id=int(input("Enter ID of the artist you'd like to vote for: "))
                
                while True:
                    if T_id in a_ids:
                        vote("Album_of_the_Year",T_id)
                        print("Your vote has been registered, thank you!")
                        plt3()
                        flag.remove(A_id)
                        used.append(A_id)
                        break
                    else:
                        T_id=int(input("Enter acceptable award id: "))
            if flag==[]:
                ctr=1
        elif A_id in used:
            print("Please vote for each category only once")
        else:
            print("Please enter an acceptable value(1/2/3)")
    elif (ch==2):
        if (len(used)>0):
            print("Thank you for voting!")
            ctr=1
        elif (len(used)==0):
            print("Kindly vote for atleast one category")
            

ans=""
ans=input("Would you like to give any suggestions? (y/n): ")
if ans=='y':
    suggestions()
else:
    thankyou()
    img=Image.open('ty.png')
    img.show()
    sys.exit()
    
thankyou()
img=Image.open('ty.png')
img.show()
sys.exit()







