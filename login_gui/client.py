import socket
import threading 
import customtkinter as ctk

from tkinter import messagebox
import tkinter as tk
import time 
def home_page():
    i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    i.connect(('localhost',4444))
    def check():
        user = username.get()
        passw = password.get()
        passw1 = confirm.get()
        if passw != passw1:
            messagebox.showerror("Error","The password you entered is not identical")
        else :
            i.sendall('signin'.encode('utf-8'))
            i.sendall(user.encode('utf-8'))
            time.sleep(0.5)
            i.sendall(passw.encode('utf-8'))
            reponse = i.recv(1024).decode('utf-8')
            if reponse == 'refuse':
                messagebox.showerror('Cubix','Choose another Username')
            else :
                messagebox.showinfo('Cubix','you have successfully created an account :)')
                window_destroyer()
    def verificator():
        global usernamex
        i.sendall('login'.encode('utf-8'))
        usernamex = userx.get()
        passwordx = passwx.get()
        i.sendall(usernamex.encode('utf-8'))
        time.sleep(0.5)
        i.sendall(passwordx.encode('utf-8'))
        reponse = i.recv(1024).decode('utf-8')
        if reponse == 'refuse':
            messagebox.showerror('Cubix','Incorrect Username or Password :(')
        else :
           messagebox.showinfo('Cubix','you have successfully logged in to your account')
           
    def window_destroyer():
        try :
            window_login.destroy()
        except:
            pass
        try :
            window_signin.destroy()
        except:
            pass
        login_page()

    def login_page():
        global window 
        try :  
            ctk.set_appearance_mode('dark')
            ctk.set_default_color_theme('dark-blue')
            window = ctk.CTk()
            window.title('Cubix - Login_Page')
            window.geometry('600x600')
            Button1 = ctk.CTkButton(window,text='LOGIN',command=login)
            Button1.pack(padx=10,pady=100)
            Button2 = ctk.CTkButton(window,text='Sign in',command=sign_in)
            Button2.place(x=225,y=180)
            window.resizable(False , False)
            window.mainloop()
        except:
            messagebox.showerror("Cubix", "Network Error 404")
    def login():
        global window_login
        global userx
        global passwx
        window.destroy()
        ctk.set_appearance_mode('cyan')
        ctk.set_default_color_theme('dark-blue')
        window_login = ctk.CTk()
        window_login.geometry('600x600')
        window_login.iconbitmap('Images/rubik.ico')
        window_login.title('Cubix - Login')
        userx = ctk.CTkEntry(window_login,placeholder_text='Username :')
        userx.place(x=100,y=70)
        passwx = ctk.CTkEntry(window_login,placeholder_text='Password :',show='*')
        passwx.place(x=100,y=140)
        submite = ctk.CTkButton(window_login ,text='Submite',command=verificator)
        submite.place(x=300,y=280)
        exit = ctk.CTkButton(window_login,text='Exit',command=window_destroyer)
        exit.place(x=70 ,y=280)
        window_login.resizable(False , False)
        window_login.mainloop()
    def sign_in():
        global username 
        global password 
        global confirm 
        global window_signin
        window.destroy()
        ctk.set_appearance_mode('cyan')
        ctk.set_default_color_theme('dark-blue')
        window_signin = ctk.CTk()
        window_signin.title('Cubix -Sign in')
        window_signin.geometry('600x600')
        window_signin.iconbitmap('Images/rubik.ico')
        username = ctk.CTkEntry(window_signin ,placeholder_text='Username :')
        username.place(x=100,y=70)
        password = ctk.CTkEntry(window_signin , placeholder_text='Password :',show='*')
        password.place(x=100,y=140)
        confirm = ctk.CTkEntry(window_signin , placeholder_text='Confirm Password :',show='*')
        confirm.place(x=100,y=210)
        submite = ctk.CTkButton(window_signin ,text='Submite',command=check)
        submite.place(x=300,y=280)
        exit = ctk.CTkButton(window_signin,text='Exit',command=window_destroyer)
        exit.place(x=70 ,y=280)
        window_signin.resizable(False, False)
        window_signin.mainloop()
    login_page()



home_page()