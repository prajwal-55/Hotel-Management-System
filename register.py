import random
from tkinter import*     #pip install pillow 
import mysql.connector 
from time import strftime
from datetime import datetime
from PIL import  Image,ImageTk 
from tkinter import ttk,messagebox



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #===================== Variable ==================
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #===================== bg image ==================

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\shockwave\Desktop\HotelManagementSystem\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #======================left image==================
        
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\shockwave\Desktop\HotelManagementSystem\hotel images\thought-good-morning-messages-LoveSove.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)
        
        #=====================main frame=================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        # =============== label and entry =================

        #row1
        #First name
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        #Last Name
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.text_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.text_lname.place(x=370,y=130,width=250)
        
        #row2
        #contact
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.text_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.text_contact.place(x=50,y=200,width=250)

        #Email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.text_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.text_email.place(x=370,y=200,width=250)
        
        #row3
        #security
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row4
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.text_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.text_pswd.place(x=50,y=340,width=250)
        
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.text_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.text_confirm_pswd.place(x=370,y=340,width=250)
        
        # =================== checkbutton ================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #==================== Button ===================
                
        img=Image.open(r"C:\Users\shockwave\Desktop\HotelManagementSystem\hotel images\register-now-button1.jpg")
        img=img.resize((200,55),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)
        
       
        img1=Image.open(r"C:\Users\shockwave\Desktop\HotelManagementSystem\hotel images\loginpng.png")
        img1=img1.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)
        

    # ================= Function Detail ===================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms are condition")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Mnbvcxz@123',database='management')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            rows=my_cursor.fetchone()
            
            if rows != None:
                messagebox.showerror("Error","User already exist,Please try another email")
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get(),
            
                ))
            conn.commit() 
            conn.close()
            messagebox.showinfo("Success","Register Successfully")




if __name__=="__main__":
    root=Tk() 
    obj=Register(root)
    root.mainloop()