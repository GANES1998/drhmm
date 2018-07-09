#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:26:07 2018

@author: ganeson
"""

from tkinter import *
import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
 
def Signup(): 
    global pwordE 
    global nameE
    global roots
 
    roots = Tk() 
    roots.title('Signup') 
    intruction = Label(roots, text='Please Enter new Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        r = Tk() 
        r.title(':D')
        r.geometry('150x50') 
        rlbl = Label(r, text='\n[+] Logged In') 
        rlbl.pack() 
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()