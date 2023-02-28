import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as box
import pickle
import mysql.connector as connect

window=tk.Tk()
window.geometry("600x300")
window.title('Passbook')

#grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

#username label and text entry box
Username=ttk.Label(window,text='Username:')
Username.grid(column=0,row=0,sticky=tk.W,padx=80,pady=10)

Username=ttk.Entry(window)
Username.grid(column=1,row=0,sticky=tk.E,padx=80,pady=10)
#password label and password entry box
Password=ttk.Label(window,text='Password:')
Password.grid(column=0,row=1,sticky=tk.W,padx=80,pady=10)

Password=ttk.Entry(window,show='*')
Password.grid(column=1,row=1,sticky=tk.E,padx=80,pady=10)
#username
username=ttk.Label(window,text='Username:')
username.grid(column=0,row=3,sticky=tk.W,padx=80,pady=10)

username=ttk.Entry(window)
username.grid(column=1,row=3,sticky=tk.E,padx=80,pady=10)

def connects():
    global con
    con=connect.connect(host='localhost',port='3306',user='root',password='sagayasql@123',database='practice')
    print('connection made')
connects()

def submit():
    data=dict()
    file=open('text.txt','wb+')
    data.update(data)
    data.update({Username.get():Password.get()})
    pickle.dump(data,file)
    print(data)
    file.close()
    
    file=open('text.txt','rb')
    data=pickle.load(file)
    file.close()
    
def search():
    #global y
    file=open('text.txt','rb')
    data=pickle.load(file)
    file.close()
    for i in data.keys():
        if i==username.get():
            y=data[i]
            print(data[i])
            print('verified')
            break
    else:
        print('entered username not there in your file')
    list1=[]
    x=username.get()
    list1.append(x)
    list1.append(y)#file.close()
    #print(data)      
    cur=con.cursor()
    query='insert into userpass_details(USERNAME,PASSWORD)values(%s,%s)'
    val=list1
    try:
        cur.execute(query,val)
        con.commit()
        print('Given data saved in database')
    except:
        con.rollback()
#submit
btn_end=ttk.Button(window,text='submit',command=submit)
btn_end.grid(column=1,row=2,sticky=tk.W,padx=50,pady=10)
       
#search
btn_search=ttk.Button(window,text='search',command=search)
btn_search.grid(column=1,row=4,sticky=tk.W,padx=50,pady=10)

window.mainloop()
con.close()



























