import customtkinter
from CTkTable import *
from CTkMessagebox import CTkMessagebox
import mysql.connector
from PIL import ImageTk,Image
import random 
import os

mycon = mysql.connector.connect(host='localhost',user='root',database='neeraj',password='password')

if mycon.is_connected():
    print('Database Connected')
cursor = mycon.cursor()

# RUN THIS CODE THEN COMMENT IT

""" sql1 = '''create table personel_details (
accno varchar(15) primary key,
name varchar(40) not null,
DOB date,
email varchar(50) not null,
phone varchar(10) not null,
address varchar(100)
);'''

sql2 = '''create table bank_details (
accno varchar(15) primary key,
name varchar(40) not null,
balance int default 0,
loggedin varchar(5),
pin int(4));'''

sql3 = '''create table transactions (
accno varchar(15),
type varchar(40) not null,
amount int default 0);'''

cursor.execute(sql3)
cursor.execute(sql1)
cursor.execute(sql2)

mycon.commit() """ 

#Removing all previous logins
cursor.execute('update bank_details set loggedin = "No"')
mycon.commit()

customtkinter.set_appearance_mode("Dark")  

root_tk = customtkinter.CTk()  
root_tk.geometry("1920x1080")
root_tk.title("BANK")

root_tk.after(0,lambda:root_tk.state("zoomed"))

label1_font = customtkinter.CTkFont(family="", size=24)

canvas = customtkinter.CTkCanvas(root_tk,width=500,height=600,highlightthickness=0,scrollregion=(0,0,1500,1500))
canvas.pack(fill="both", expand=True)

#------------------------------------------------------------------------------------------------------
#BACKGROUND
bg = Image.open("ANOTHER BG.png")
resized = bg.resize((1920,1080), Image.LANCZOS)
new_bg = ImageTk.PhotoImage(resized)
canvas.create_image(0,0,image=new_bg,anchor='nw')
#------------------------------------------------------------------------------------------------------
#CORNER ICON
bg1 = Image.open("bank.png")
resized1 = bg1.resize((50,50), Image.LANCZOS)
new_bg1 = ImageTk.PhotoImage(resized1)
canvas.create_image(40,30,image=new_bg1,anchor='nw')
canvas.create_text((190,60),text="BANK",fill="#FA6775",font=("Inter",35))
#------------------------------------------------------------------------------------------------------
#MAIN TEXT ON HOME PAGE
Ttext='''Seamless and secure online banking with EZBank. 
Manage accounts, transfer funds, and pay bills anytime, anywhere.
Join now for convenience and 24/7 support.'''
canvas.create_text((520, 520),text="Made Easier.",fill="#FA6775",font=("Inter",100))
canvas.create_text((580, 400),text="Online Banking",fill="#F52549",font=("Inter",100))
canvas.create_text((550,650),text=Ttext,fill="white",font=("Inter",20))
#------------------------------------------------------------------------------------------------------
#OTHER STUFF
homebtn = canvas.create_text((450,60),text="Home",fill="white",font=("",20),tags="HomeBTN")
Abtbtn = canvas.create_text((700,60),text="About Us",fill="white",font=("",20),tags="AbtBTN")
Serbtn = canvas.create_text((950,60),text="Services",fill="white",font=("",20),tags="SerBTN")
Contbtn = canvas.create_text((1200,60),text="Contact",fill="white",font=("",20),tags="ContBTN")
Logbtn = canvas.create_text((1600,60),text="Login",fill="white",font=("",20),tags="LogBTN")
signuprect = canvas.create_rectangle((1700,30),(1840,90),fill="#F52549",tags='SignBTN')
Signbtn = canvas.create_text((1770,60),text="SignUp",fill="white",font=("",20),tags="SignBTN")

scroll = False
def mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)),"units")

def scrolling(scroll):
    if scroll == True:
        canvas.bind_all("<MouseWheel>",mousewheel)
    elif scroll == False:
        canvas.unbind_all("<MouseWheel>")

def temp_page(height):
    global homebtn,Abtbtn,Serbtn,Contbtn,bg,bg1,resized,resized1,new_bg,new_bg1
    canvas.delete('all')
    #------------------------------------------------------------------------------------------------------
    #BACKGROUND
    bg = Image.open("BGWITHOUTSTUFF.png")
    resized = bg.resize((1920,height), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized)
    canvas.create_image(0,0,image=new_bg,anchor='nw')
    #------------------------------------------------------------------------------------------------------
    #CORNER ICON
    bg1 = Image.open("bank.png")
    resized1 = bg1.resize((50,50), Image.LANCZOS)
    new_bg1 = ImageTk.PhotoImage(resized1)
    canvas.create_image(40,30,image=new_bg1,anchor='nw')
    canvas.create_text((190,60),text="BANK",fill="#FA6775",font=("Inter",35))
    #------------------------------------------------------------------------------------------------------
    #OTHER STUFF
    homebtn = canvas.create_text((450,60),text="Home",fill="white",font=("",20),tags="HomeBTN")
    Abtbtn = canvas.create_text((700,60),text="About Us",fill="white",font=("",20),tags="AbtBTN")
    Serbtn = canvas.create_text((950,60),text="Services",fill="white",font=("",20),tags="SerBTN")
    Contbtn = canvas.create_text((1200,60),text="Contact",fill="white",font=("",20),tags="ContBTN")
    Logbtn = canvas.create_text((1600,60),text="Login",fill="white",font=("",20),tags="LogBTN")
    signuprect = canvas.create_rectangle((1700,30),(1840,90),fill="#F52549",tags='SignBTN')
    Signbtn = canvas.create_text((1770,60),text="SignUp",fill="white",font=("",20),tags="SignBTN")

def home_page(event):
    global homebtn,Abtbtn,Serbtn,Contbtn,bg,bg1,resized,resized1,new_bg,new_bg1
    scroll = False
    scrolling(scroll)
    canvas.delete('all')
    #------------------------------------------------------------------------------------------------------
    #BACKGROUND
    bg = Image.open("ANOTHER BG.png")
    resized = bg.resize((1920,1080), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized)
    canvas.create_image(0,0,image=new_bg,anchor='nw')
    #------------------------------------------------------------------------------------------------------
    #CORNER ICON
    bg1 = Image.open("bank.png")
    resized1 = bg1.resize((50,50), Image.LANCZOS)
    new_bg1 = ImageTk.PhotoImage(resized1)
    canvas.create_image(40,30,image=new_bg1,anchor='nw')
    canvas.create_text((190,60),text="BANK",fill="#FA6775",font=("Inter",35))
    #------------------------------------------------------------------------------------------------------
    #MAIN TEXT ON HOME PAGE
    Ttext='''Seamless and secure online banking with EZBank. 
    Manage accounts, transfer funds, and pay bills anytime, anywhere.
    Join now for convenience and 24/7 support.'''
    canvas.create_text((520, 520),text="Made Easier.",fill="#FA6775",font=("Inter",100))
    canvas.create_text((580, 400),text="Online Banking",fill="#F52549",font=("Inter",100))
    canvas.create_text((550,650),text=Ttext,fill="white",font=("Inter",20))
    #------------------------------------------------------------------------------------------------------
    #OTHER STUFF
    homebtn = canvas.create_text((450,60),text="Home",fill="white",font=("",20),tags="HomeBTN")
    Abtbtn = canvas.create_text((700,60),text="About Us",fill="white",font=("",20),tags="AbtBTN")
    Serbtn = canvas.create_text((950,60),text="Services",fill="white",font=("",20),tags="SerBTN")
    Contbtn = canvas.create_text((1200,60),text="Contact",fill="white",font=("",20),tags="ContBTN")
    Logbtn = canvas.create_text((1600,60),text="Login",fill="white",font=("",20),tags="LogBTN")
    signuprect = canvas.create_rectangle((1700,30),(1840,90),fill="#F52549",tags='SignBTN')
    Signbtn = canvas.create_text((1770,60),text="SignUp",fill="white",font=("",20),tags="SignBTN")

def contact_page(event):
    scroll = False
    temp_page(1080)
    scrolling(scroll)

    canvas.create_rectangle((550,200),(1300,1000),fill="black")
    canvas.create_line((600,450),(700,450),fill="#FA6775",width=4)
    main_text = canvas.create_text(600, 250, anchor="nw", text="Get in touch", fill="#F52549",font=("Inter",60))
    ch='''Put any heading here'''
    text1 = canvas.create_text(600, 350, anchor="nw", text=ch, fill="white",font=("Inter",24))
    ch1='''whatever your want put here'''
    text2 = canvas.create_text(600,500,anchor='nw',text=ch1,fill="white",font=("Inter",24))

def login_page(event):
    scroll = False
    temp_page(1080)
    scrolling(scroll)

    canvas.create_rectangle((550,200),(1300,1000),fill="black")
    canvas.create_line((600,450),(700,450),fill="#FA6775",width=4)
    main_text = canvas.create_text(600, 250, anchor="nw", text="Login", fill="#F52549",font=("Inter",60))
    ch='''Welcome Back!
Login in to view your bank account'''
    text1 = canvas.create_text(600, 350, anchor="nw", text=ch, fill="white",font=("Inter",24))
    text2 = canvas.create_text(600,500,anchor='nw',text="AccountNo:",fill="white",font=("Inter",24))
    text3 = canvas.create_text(600,630,anchor='nw',text="PIN",fill="white",font=("Inter",24))
    un_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="AccountNo.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pw_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')

    pw_entry.configure(show='*')

    un_window = canvas.create_window(600, 550, anchor="nw", window=un_entry)
    pw_window = canvas.create_window(600, 680, anchor="nw", window=pw_entry)

    def login():
        global accno10,pin10
        accno10 = un_entry.get()
        pin10 = pw_entry.get()
        try:
            sql = '''select loggedin from bank_details where accno = '{}' and pin={};'''.format(accno10,pin10)
            cursor.execute(sql)
            data = cursor.fetchall()
            if data == []:
                CTkMessagebox(message='Invalid entries/empty',icon='cancel',option_1='Ok')
            else:
                rec = data[0][0]
                if rec == 'Yes':
                    CTkMessagebox(message="You are already logged in",icon="cancel", option_1="Ok")
                elif rec == 'No':
                    sql1 = '''update bank_details set loggedin='Yes' where accno='{}' and pin={};'''.format(accno10,pin10)
                    CTkMessagebox(message='You have successfully logged in',icon='check',option_1='Ok')
                    cursor.execute(sql1)
                    mycon.commit()

            un_entry.delete(0,'end')
            pw_entry.delete(0,'end')
        except Exception as e:
            CTkMessagebox(message=e,icon="cancel", option_1="Ok")
            print(e)
    
    def log_out():
        try:
            sql3 = f'''select loggedin from bank_details where accno='{accno10}' and pin={pin10}'''
            cursor.execute(sql3)
            print(pin10,'At logout')
            rec = cursor.fetchall()[0][0]
            if rec == 'No':
                CTkMessagebox(message=f"You are not logged in",icon="cancel", option_1="Ok")
            else:
                sql2 = '''update bank_details set loggedin='No' where accno = '{}' and pin={}'''.format(accno10,pin10)
                cursor.execute(sql2)
                mycon.commit()
                CTkMessagebox(message=f"Succcessfully logged out",icon="check", option_1="Ok")
        except Exception as e:
            CTkMessagebox(message=f"You are not logged in",icon="cancel", option_1="Ok")
            print(e)

    login_button = customtkinter.CTkButton(canvas,command=login,width=500,height=50,text="Login",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    login_window = canvas.create_window(600,780,anchor='nw',window=login_button)

    loginout_button = customtkinter.CTkButton(canvas,command=log_out,width=200,height=50,text="Log Out",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    loginout_window = canvas.create_window(1650,980,anchor='nw',window=loginout_button)

def signup_page(event):
    scroll = False
    temp_page(1080)
    scrolling(scroll)

    canvas.create_rectangle((530,120),(1300,1030),fill="black")
    canvas.create_line((600,330),(750,330),fill="#FA6775",width=4)
    main_text = canvas.create_text(600,170,anchor='nw',text="Sign Up",fill="#F52549",font=("Inter",60))
    text='''Its free and only takes a minute.'''
    text1 = canvas.create_text(600,270,anchor='nw',text=text,fill='white',font=("Inter",24))

    text2 = canvas.create_text(600,370,anchor='nw',text="Username",fill="white",font=("Inter",24))
    text3 = canvas.create_text(600,500,anchor='nw',text="DOB",fill="white",font=("Inter",24))
    text4 = canvas.create_text(925,500,anchor='nw',text="Email",fill="white",font=("Inter",24))
    text5 = canvas.create_text(600,630,anchor='nw',text="Phone",fill="white",font=("Inter",24))
    text6 = canvas.create_text(925,630,anchor='nw',text="Address",fill="white",font=("Inter",24))
    text7 = canvas.create_text(600,760,anchor='nw',text="PIN",fill="white",font=("Inter",24))

    name_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your name",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    dob_entry = customtkinter.CTkEntry(canvas, width=240,height=50,placeholder_text="YYYY/MM/DD",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    email_entry = customtkinter.CTkEntry(canvas, width=240,height=50,placeholder_text="Enter your email",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    phno_entry = customtkinter.CTkEntry(canvas, width=240,height=50,placeholder_text="Enter your mobile no.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    add_entry = customtkinter.CTkEntry(canvas, width=240,height=50,placeholder_text="Enter your address",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pw_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')

    pw_entry.configure(show='*')

    name_window = canvas.create_window(600, 420, anchor="nw", window=name_entry)
    dob_window = canvas.create_window(600, 550, anchor="nw", window=dob_entry)
    email_window = canvas.create_window(925, 550, anchor="nw", window=email_entry)
    phno_window = canvas.create_window(600, 680, anchor="nw", window=phno_entry)
    add_window = canvas.create_window(925, 680, anchor="nw", window=add_entry)
    pw_window = canvas.create_window(600, 810, anchor="nw", window=pw_entry)
    #----------------------------------------------------------------------------------------------------------------
    #SQL FOR CREATING ACCOUNT
    def crt():
        accno = random.randint(100000000,9999999999)
        cursor.execute('select accno from bank_details;')
        data = cursor.fetchall()
        for i in data:
            if accno == i[0]:
                accno = random.randint(100000000,999999999)
        
        name = name_entry.get()
        dob = dob_entry.get()
        email = email_entry.get()
        phno = phno_entry.get()
        address = add_entry.get()
        pin = pw_entry.get()

        sql1 = '''
    insert into personel_details
    values
    ('{}','{}','{}','{}','{}','{}');'''.format(str(accno),name,dob,email,phno,address)
        sql2 = '''
insert into bank_details (Accno,Name,pin) values
('{}','{}',{})'''.format(str(accno),name,pin)
        try:
            cursor.execute(sql1)
            cursor.execute(sql2)
            mycon.commit()
        except Exception as e:
            mycon.rollback()
            CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
            print(e)
        else:
            msg = CTkMessagebox(message=f"Successfully created account!\nAccno: {accno}",icon="check", option_1="Ok")
            name_entry.delete(0,'end')
            dob_entry.delete(0,'end')
            email_entry.delete(0,'end')
            phno_entry.delete(0,'end')
            add_entry.delete(0,'end')
            pw_entry.delete(0,'end')
            res1 = msg.get()
            if res1 == "Ok":
                msg1 = CTkMessagebox(message="Do you want to download your user data?",icon="question", option_1="Yes",option_2="No")
                res = msg1.get()
                if res == "Yes":
                    f = open(f"{accno}_Details.txt","w")
                    ch = f'''Name: {name}
Accno: {accno}
DOB: {dob}
Email: {email}
PhoneNo: {phno}
Address: {address}
PIN: {pin}
'''
                    f.write(ch)
                    f.close()
                elif res == "No":
                    pass
    login_button = customtkinter.CTkButton(canvas, width=500,command=crt,height=50,text="SignUp",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    login_window = canvas.create_window(600,910,anchor='nw',window=login_button)

def aboutus_page(event):
    scroll = False
    temp_page(1080)
    scrolling(scroll)
    
    canvas.create_rectangle((550,200),(1300,1000),fill="black")
    text1='''No humans were harmed during the creation 
    of this project.(excluding Neeraj)'''
    canvas.create_text((600,300),text=text1,fill='white',font=("Inter",24),anchor='nw')

def services_page(event):
    global bal,newbal,resizedbal,dep,newdep,resizeddep,send,newsend,resizedsend
    global close,newclose,resizedclose,update,newupdate,resizedupdate,history,resizedhistory,newhistory
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_line((800,400),(1100,400),fill="#FA6775",width=4)
    canvas.create_text(660,200,anchor='nw',text="OUR",fill="white",font=("Inter",60))
    canvas.create_text(860,200,anchor='nw',text="SERVICES",fill="#F52549",font=("Inter",60))
    text1 = '''Tailored Financial Solutions for Your Every Need'''
    canvas.create_text(580,320,anchor='nw',text=text1,fill='white',font=("Inter",24))

    #TOP ROW
    rect1 = canvas.create_rectangle((250,500),(650,900),fill='black',tags='BalanceBTN')
    rect2 = canvas.create_rectangle((750,500),(1150,900),fill='black',tags='DepositBTN')
    rect3 = canvas.create_rectangle((1250,500),(1650,900),fill='black',tags='TransferBTN')

    #BOTTOM ROW
    rect4 = canvas.create_rectangle((250,1000),(650,1400),fill='black',tags='CloseBTN')
    rect5 = canvas.create_rectangle((750,1000),(1150,1400),fill='black',tags='UpdateBTN')
    rect6 = canvas.create_rectangle((1250,1000),(1650,1400),fill='black',tags='TransactionBTN')

    #IMAGES
    #BALANCE
    bal = Image.open("balance.png")
    resizedbal = bal.resize((150,150), Image.LANCZOS)
    newbal = ImageTk.PhotoImage(resizedbal)
    canvas.create_image(370,570,image=newbal,anchor='nw',tags='BalanceBTN')
    canvas.create_text(330,750,anchor='nw',text="Balance",fill='#F52549',font=("Inter",45),tags='BalanceBTN')

    #Deposit
    dep = Image.open("deposit.png")
    resizeddep = dep.resize((150,150), Image.LANCZOS)
    newdep = ImageTk.PhotoImage(resizeddep)
    canvas.create_image(870,570,image=newdep,anchor='nw',tags='DepositBTN')
    canvas.create_text(830,750,anchor='nw',text="Deposit",fill='#F52549',font=("Inter",45),tags="DepositBTN")

    #Send
    send = Image.open("transfer.png")
    resizedsend = send.resize((150,150), Image.LANCZOS)
    newsend = ImageTk.PhotoImage(resizedsend)
    canvas.create_image(1370,570,image=newsend,anchor='nw',tags='TransferBTN')
    canvas.create_text(1320,750,anchor='nw',text="Transfer",fill='#F52549',font=("Inter",45),tags='TransferBTN')

    #CloseAccount
    close = Image.open("closeacc.png")
    resizedclose = close.resize((150,150), Image.LANCZOS)
    newclose = ImageTk.PhotoImage(resizedclose)
    canvas.create_image(370,1080,image=newclose,anchor='nw',tags='CloseBTN')
    canvas.create_text(310,1260,anchor='nw',text='CloseAcc.',fill='#F52549',font=("Inter",45),tags='CloseBTN')

    #UpdateAccount
    update = Image.open("updateacc.png")
    resizedupdate = update.resize((150,150), Image.LANCZOS)
    newupdate = ImageTk.PhotoImage(resizedupdate)
    canvas.create_image(870,1080,image=newupdate,anchor='nw',tags="UpdateBTN")
    canvas.create_text(790,1260,anchor='nw',text='UpdateAcc.',fill='#F52549',font=("Inter",45),tags="UpdateBTN")

    #Transation History
    history = Image.open("tranchist..png")
    resizedhistory = history.resize((150,150), Image.LANCZOS)
    newhistory = ImageTk.PhotoImage(resizedhistory)
    canvas.create_image(1370,1080,image=newhistory,anchor='nw',tags='TransactionBTN')
    canvas.create_text(1350,1260,anchor='nw',text='History',fill='#F52549',font=("Inter",45),tags="TransactionBTN")


    scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
    scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
    canvas.config(yscrollcommand=scrollbar.set)

def balance(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        print(data)
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        print(e)
        return
    
    rec = data[0][0]

    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec=='Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)

        canvas.create_rectangle((530,120),(1300,1030),fill="black")

        text = canvas.create_text(600,370,anchor='nw',text="Account No.",fill="white",font=("Inter",24))
        text1 = canvas.create_text(600,500,anchor='nw',text="PIN",fill="white",font=("Inter",24))
        text2 = canvas.create_text(600,630,anchor='nw',text="Balance",fill="white",font=("Inter",24))

        accno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your AccountNo.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        bal_entry = customtkinter.CTkEntry(canvas, width=500,height=50,font=("Helvetica",20),fg_color='black',corner_radius=0,text_color='white')

        pin_entry.configure(show='*')
        bal_entry.configure(state='disabled')

        accno_window = canvas.create_window(600, 420, anchor="nw", window=accno_entry)
        pin_window = canvas.create_window(600, 550, anchor="nw", window=pin_entry)
        bal_window = canvas.create_window(600, 680, anchor="nw", window=bal_entry)

        #-----------------------------------------------------------------------------------------------------
        #SQL FOR BALANCE
        def bal():
            bal_entry.delete(0,'end')
            bal_entry.configure(state='normal')
            entered_accno = accno_entry.get()
            pin = pin_entry.get()
            bal = '''Select Balance,pin from bank_details
            where AccNo = '{}' and pin={};'''.format(entered_accno,pin)
            cursor.execute(bal)
            data = cursor.fetchall()
            bal_entry.delete(0,'end')
            try:
                bal_entry.insert(0, str(data[0][0]))
            except:
                CTkMessagebox(title='Box',message="Account Not in existence",icon="cancel", option_1="Ok")
            bal_entry.configure(state='disabled')
        
        enter_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=bal)
        Enter_button = canvas.create_window(600,770,anchor='nw',window=enter_button)

        scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
        scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
        canvas.config(yscrollcommand=scrollbar.set)

def deposit(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        return
    
    rec = data[0][0]

    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec=='Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)
        canvas.create_rectangle((530,120),(1300,1030),fill="black")

        text = canvas.create_text(600,370,anchor='nw',text="Account No.",fill="white",font=("Inter",24))
        text1 = canvas.create_text(600,500,anchor='nw',text="UserName",fill="white",font=("Inter",24))
        text2 = canvas.create_text(600,630,anchor='nw',text="Amount",fill="white",font=("Inter",24))
        text3 = canvas.create_text(600,760,anchor='nw',text="PIN",fill="white",font=("Inter",24))

        accno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your AccountNo.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        name_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your name",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        amt_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter the Amount",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')

        pin_entry.configure(show='*')

        accno_window = canvas.create_window(600, 420, anchor="nw", window=accno_entry)
        name_window = canvas.create_window(600, 550, anchor="nw", window=name_entry)
        amt_window = canvas.create_window(600, 680, anchor="nw", window=amt_entry)
        pin_window = canvas.create_window(600, 810, anchor="nw", window=pin_entry)
        

        #-----------------------------------------------------------------------------------------------------
        #SQL FOR DEPOSIT
        def dep():
            accno=accno_entry.get()
            pin=pin_entry.get()
            amt=amt_entry.get()
            dep ='''Update bank_details set Balance = Balance+{} where AccNo = {} and pin='{}';'''.format(int(amt),accno,pin)
            dep1 = '''Insert into transactions values ({},'Deposit',{})'''.format(accno,int(amt))
            try:
                cursor.execute(dep)
                cursor.execute(dep1)
                mycon.commit()
            except Exception as e:
                CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                print(e)
            else:
                CTkMessagebox(title='Box',message="Successfully Deposited the Amount in your Account",icon="check", option_1="Ok")

        enter_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Enter",font=("Inter",20),command=dep,fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
        Enter_button = canvas.create_window(600,910,anchor='nw',window=enter_button)

        scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
        scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
        canvas.config(yscrollcommand=scrollbar.set)

def transfer(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        return
    
    rec = data[0][0]

    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec == 'Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)
        canvas.create_rectangle((530,120),(1300,1030),fill="black")

        text = canvas.create_text(600,370,anchor='nw',text="Account No. 1",fill="white",font=("Inter",24))
        text1 = canvas.create_text(600,500,anchor='nw',text="Account No. 2",fill="white",font=("Inter",24))
        text2 = canvas.create_text(600,630,anchor='nw',text="Amount",fill="white",font=("Inter",24))
        text3 = canvas.create_text(600,760,anchor='nw',text="PIN",fill="white",font=("Inter",24))

        accno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your AccountNo.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        accno1_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter the receivers Accno.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        amt_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter the Amount",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')

        pin_entry.configure(show='*')

        accno_window = canvas.create_window(600, 420, anchor="nw", window=accno_entry)
        accno1_window = canvas.create_window(600, 550, anchor="nw", window=accno1_entry)
        amt_window = canvas.create_window(600, 680, anchor="nw", window=amt_entry)
        pin_window = canvas.create_window(600, 810, anchor="nw", window=pin_entry)
        

        #-----------------------------------------------------------------------------------------------------
        #SQL FOR TRANSFER
        def send():
            accno=accno_entry.get()
            accno1 = accno1_entry.get()
            amt=amt_entry.get()
            pin=pin_entry.get()
            dep1 = '''select balance from bank_details where accno = '{}' and pin={};'''.format(accno,int(pin))
            cursor.execute(dep1)
            result = cursor.fetchone()
            try:
                if result[0] >= int(amt):
                    dep2 = '''
        update bank_details
        set balance = balance - {} where accno = '{}';'''.format(int(amt),accno)
                    dep3 = '''
        update bank_details
        set balance = balance + {} where accno = '{}';'''.format(int(amt),accno1)
                    dep4 = '''
        Insert into transactions 
        values ({},'Sent',{});'''.format(accno,int(amt))
                    dep5 = '''
        Insert into transactions 
        values ({},'Received',{});'''.format(accno1,int(amt))
                    cursor.execute(dep2)
                    cursor.execute(dep3)
                    cursor.execute(dep4)
                    cursor.execute(dep5)
                    mycon.commit()
                    CTkMessagebox(title='Box',message="Successfully Transfered the Amount",icon="check", option_1="Ok")
                else:
                    mycon.rollback()
                    CTkMessagebox(message="Transfer Failed: Not Enough Funds!",icon="cancel", option_1="Ok")
            except Exception as e:
                CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                print(e)

        enter_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Enter",font=("Inter",20),command=send,fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
        Enter_button = canvas.create_window(600,910,anchor='nw',window=enter_button)

        scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
        scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
        canvas.config(yscrollcommand=scrollbar.set)

def close(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        return
    
    rec = data[0][0]

    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec == 'Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)
        canvas.create_rectangle((530,120),(1300,1030),fill="black")

        text = canvas.create_text(600,370,anchor='nw',text="Account No.",fill="white",font=("Inter",24))
        text1 = canvas.create_text(600,500,anchor='nw',text="Username",fill="white",font=("Inter",24))
        text2 = canvas.create_text(600,630,anchor='nw',text="PIN",fill="white",font=("Inter",24))

        accno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your AccountNo.",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        un_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your UserName",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your PIN",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')

        pin_entry.configure(show='*')

        accno_window = canvas.create_window(600, 420, anchor="nw", window=accno_entry)
        accno1_window = canvas.create_window(600, 550, anchor="nw", window=un_entry)
        amt_window = canvas.create_window(600, 680, anchor="nw", window=pin_entry)

        #-----------------------------------------------------------------------------------------------------
        #SQL FOR CLOSEACCOUNT
        def close1():
            accno=accno_entry.get()
            un = un_entry.get()
            pin=pin_entry.get()
            try:
                sql1 = '''delete from bank_details where accno='{}'and name='{}' and pin={}'''.format(accno,un,int(pin))
                sql2 = '''delete from personel_details where accno='{}'and name='{}' '''.format(accno,un)
                msg1 = CTkMessagebox(message="Do You really want to delete your account?",icon="question", option_1="Yes",option_2='No')
                res = msg1.get()
                if res == "Yes":
                    cursor.execute(sql1)
                    cursor.execute(sql2)
                    CTkMessagebox(message="Successfully deleted account",icon="check", option_1="Ok")
                    mycon.commit()
                    try:
                        os.remove(f"{accno}_Details.txt")
                    except FileNotFoundError:
                        pass
                    pin_entry.delete(0,'end')
                    accno_entry.delete(0,'end')
                    un_entry.delete(0,'end')
                elif res == "No":
                    pass
            except Exception as e:
                CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                print(e)

        enter_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Enter",font=("Inter",20),command=close1,fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
        Enter_button = canvas.create_window(600,780,anchor='nw',window=enter_button)

        scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
        scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
        canvas.config(yscrollcommand=scrollbar.set)

def update(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        return
    
    rec = data[0][0]
    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec == 'Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)

        canvas.create_rectangle((530,120),(1300,1030),fill="black",tags = 'rect')

        name_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Name",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_name()])
        name_window = canvas.create_window(600,350,anchor='nw',window=name_button)

        dob_button = customtkinter.CTkButton(canvas, width=500,height=50,text="DOB",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_dob()])
        dob_window = canvas.create_window(600,450,anchor='nw',window=dob_button)

        email_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Email",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_email()])
        email_window = canvas.create_window(600,550,anchor='nw',window=email_button)

        phno_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Phno",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_phno()])
        phno_window = canvas.create_window(600,650,anchor='nw',window=phno_button)

        address_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Address",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_address()])
        address_window = canvas.create_window(600,750,anchor='nw',window=address_button)

        pin_button = customtkinter.CTkButton(canvas, width=500,height=50,text="Pin",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775",command=lambda:[update_pin()])
        pin_window = canvas.create_window(600,850,anchor='nw',window=pin_button)

        scrollbar = customtkinter.CTkScrollbar(root_tk,width=20,height=1500,button_color='#F52549',button_hover_color="#FA6775",command=canvas.yview)
        scrollbar_window = canvas.create_window(1900, 0, anchor="nw", window=scrollbar)
        canvas.config(yscrollcommand=scrollbar.set)

def update_name():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    name_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your new Name",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    name_window = canvas.create_window(600, 420, anchor="nw", window=name_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')

    def enter():
        name = name_entry.get()
        pin = pin_entry.get()
        try:
            sql0 = '''select accno from bank_details where pin={};'''.format(int(pin),)
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]
            print(accno)
            try:
                sql1 = f'''update bank_details set name = '{name}' where pin={int(pin)} and accno='{accno}';'''
                sql2 = f'''update personel_details set name = '{name}' where accno='{accno}';'''
                cursor.execute(sql1)
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your name",icon="check", option_1="Ok")

                name_entry.delete(0,'end')
                pin_entry.delete(0,'end')
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def update_dob():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    dob_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter new DOB(YYYY/MM/DD)",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    dob_window = canvas.create_window(600, 420, anchor="nw", window=dob_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')

    def enter():
        dob = dob_entry.get()
        pin = int(pin_entry.get())
        try:
            sql0 = f'''select accno from bank_details where pin={pin};'''
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]

            try:
                sql2 = f'''update personel_details set dob = '{dob}' where accno='{accno}';'''
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your DOB",icon="check", option_1="Ok")

                dob_entry.delete(0,'end')
                pin_entry.delete(0,'end')
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def update_email():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    email_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter new email",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    email_window = canvas.create_window(600, 420, anchor="nw", window=email_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')

    def enter():
        email = email_entry.get()
        pin = int(pin_entry.get())
        try:
            sql0 = f'''select accno from bank_details where pin={pin};'''
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]

            try:
                sql2 = f'''update personel_details set email = '{email}' where accno='{accno}';'''
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your Email",icon="check", option_1="Ok")

                email_entry.delete(0,'end')
                pin_entry.delete(0,'end')
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def update_phno():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    phno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter new phno",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    phno_window = canvas.create_window(600, 420, anchor="nw", window=phno_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')

    def enter():
        phno = int(phno_entry.get())
        pin = int(pin_entry.get())
        try:
            sql0 = f'''select accno from bank_details where pin={pin};'''
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]

            try:
                sql2 = f'''update personel_details set phone = '{phno}' where accno='{accno}';'''
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your phone no.",icon="check", option_1="Ok")

                phno_entry.delete(0,'end')
                pin_entry.delete(0,'end')
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def update_address():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    address_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter new address",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    address_window = canvas.create_window(600, 420, anchor="nw", window=address_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter your pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')

    def enter():
        address = address_entry.get()
        pin = int(pin_entry.get())
        try:
            sql0 = f'''select accno from bank_details where pin={pin};'''
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]

            try:
                sql2 = f'''update personel_details set address = '{address}' where accno='{accno}';'''
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your address",icon="check", option_1="Ok")

                address_entry.delete(0,'end')
                pin_entry.delete(0,'end')
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def update_pin():
    temp_page(1500)
    scroll=True
    scrolling(scroll)

    canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
    pin1_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter new pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin1_window = canvas.create_window(600, 420, anchor="nw", window=pin1_entry)
    pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter old pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
    pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

    pin_entry.configure(show='*')
    pin1_entry.configure(show='*')

    def enter():
        global pin10
        pin1 = int(pin1_entry.get())
        pin = int(pin_entry.get())
        try:
            sql0 = f'''select accno from bank_details where pin={pin} and loggedin='Yes';'''
            cursor.execute(sql0)
            data = cursor.fetchall()
            accno = data[0][0]

            try:
                sql2 = f'''update bank_details set pin = {pin1} where accno='{accno}';'''
                cursor.execute(sql2)
                mycon.commit()

                CTkMessagebox(message="Successfully Updated your pin",icon="check", option_1="Ok")

                pin1_entry.delete(0,'end')
                pin_entry.delete(0,'end')

                sql3 = f'''update bank_details set loggedin = 'Yes' where accno='{accno}' and pin={pin1};'''
                cursor.execute(sql3)
                mycon.commit()
            except Exception as e:
                    mycon.rollback()
                    CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                    print(e)
            pin10 = pin1
            print(pin10,'At update pin')
        except Exception as e:
            CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
            print(e)

    enter_button = customtkinter.CTkButton(canvas, command=enter,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
    enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

def transaction_history(event):
    try:
        sql1 = f'''select loggedin from bank_details where accno = '{accno10}' and pin = {pin10};'''
        cursor.execute(sql1)
        data = cursor.fetchall()
        if data == []:
            CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
            return
    except Exception as e:
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
        return
    
    rec = data[0][0]
    if rec=='No':
        CTkMessagebox(message="You are not logged in",icon="cancel", option_1="Ok")
    elif rec == 'Yes':
        temp_page(1500)
        scroll=True
        scrolling(scroll)

        canvas.create_rectangle((530,300),(1300,800),fill='black',tags='rect1')
        accno_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter Accno",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        accno_window = canvas.create_window(600, 420, anchor="nw", window=accno_entry)
        pin_entry = customtkinter.CTkEntry(canvas, width=500,height=50,placeholder_text="Enter pin",font=("Helvetica",20),fg_color='black',corner_radius=0,placeholder_text_color='grey',text_color='white')
        pin_window = canvas.create_window(600, 520, anchor="nw", window=pin_entry)

        pin_entry.configure(show='*')

        def newwindow():
            newWindow = customtkinter.CTkToplevel(root_tk)
            newWindow.title("TransactionHistory")

            def create_table():
                accno = accno_entry.get()
                pin = pin_entry.get()
                try:
                    sql1 = '''select * from bank_details where accno='{}' and pin='{}';'''.format(accno,pin)
                    cursor.execute(sql1)
                    data = cursor.fetchall()
                    if data !=[]:
                        try:
                            sql2 = f'''select * from transactions where accno='{accno}';'''
                            cursor.execute(sql2)
                            data1 = cursor.fetchall()
                            print(data1)
                            #table
                            if data1 == []:
                                CTkMessagebox(message="No data to display",icon="cancel", option_1="Ok")
                                return
                            else:
                                rows = len(data1)
                                cols = len(data1[0])

                                header_list = ['AccountNo.','Type','Amount']

                                for widget in table_frame.winfo_children():
                                    widget.destroy()

                                for col in range(cols):
                                    header = customtkinter.CTkLabel(table_frame, text=header_list[col],corner_radius=0,padx=0, pady=0)
                                    header.grid(row=0, column=col, sticky="nsew")

                                for row in range(rows):
                                    for col in range(cols):
                                        cell = customtkinter.CTkEntry(table_frame, width=200,justify='center',height=40,corner_radius=0)
                                        cell.grid(row=row+1, column=col, sticky="nsew")
                                        cell.insert(0,data1[row][col])

                                for col in range(cols):
                                    table_frame.grid_columnconfigure(col, weight=1)
                        except Exception as e:
                            mycon.rollback()
                            CTkMessagebox(message="Something went wrong!!!",icon="cancel", option_1="Ok")
                            print(e)
                except Exception as e:
                    CTkMessagebox(message="Your entries do not match/empty",icon="cancel", option_1="Ok")
                    print(e)
            table_frame = customtkinter.CTkFrame(newWindow)
            table_frame.grid(row=2, column=0, columnspan=3)
            create_table()
        
        accno_entry.delete(0,'end')
        pin_entry.delete(0,'end')

        enter_button = customtkinter.CTkButton(canvas, command=newwindow,width=500,height=50,text="Enter",font=("Inter",20),fg_color='#F52549',corner_radius=0,hover_color="#FA6775")
        enter_window = canvas.create_window(600,620,anchor='nw',window=enter_button)

'''
AUTOMATICALLY ADJUSTING BACKGROUND SIZE BASED ON WINDOW SIZE

def Bg(e):
    global bg, resized, new_bg, homebtn
    bg = Image.open("ANOTHER BG.png")
    resized = bg.resize((e.width,e.height), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized)
    canvas.create_image(0,0,image=new_bg,anchor='nw')
    canvas.create_text((500, 520),text="Made Easier",fill="#FA6775",font=("Inter",100))
    canvas.create_text((580, 400),text="Online Banking",fill="#F52549",font=("Inter",100))
    homebtn = canvas.create_text((600,60),text="home",fill="white",font=("",40),tags="HomeBTN")
'''
canvas.tag_bind("ContBTN","<ButtonPress-1>",contact_page)
canvas.tag_bind("HomeBTN", "<ButtonPress-1>", home_page)
canvas.tag_bind("LogBTN","<ButtonPress-1>",login_page)
canvas.tag_bind("SignBTN","<ButtonPress-1>",signup_page)
canvas.tag_bind("AbtBTN","<ButtonPress-1>",aboutus_page)
canvas.tag_bind("SerBTN","<ButtonPress-1>",services_page)
canvas.tag_bind("BalanceBTN","<ButtonPress-1>",balance)
canvas.tag_bind("DepositBTN","<ButtonPress-1>",deposit)
canvas.tag_bind("TransferBTN","<ButtonPress-1>",transfer)
canvas.tag_bind("CloseBTN","<ButtonPress-1>",close)
canvas.tag_bind("UpdateBTN","<ButtonPress-1>",update)
canvas.tag_bind("TransactionBTN","<ButtonPress-1>",transaction_history)

root_tk.mainloop()
mycon.close()

