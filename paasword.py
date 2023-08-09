from tkinter import *
import string
import random

# # fun for log in
# def hendle_login():

#     email = email_input.get()
    


# fun for genartor

def genarator():
    small_case =string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digit = string.digits
    spacial = string.punctuation

    all = small_case + upper_case + digit + spacial
    
    password_fun = int(password_spin.get())


    if choice.get()==1:
        password_genarate.insert(0,random.sample(small_case,password_fun))

    if choice.get()==2 :
        password_genarate.insert(0,random.sample(small_case+upper_case,password_fun))

    if choice.get()==3 :
        password_genarate.insert(0,random.sample(small_case+upper_case+spacial,password_fun))       

    # password_ran = random.sample(all,password_fun)
    # password_genarate.insert(0,password_ran)


root = Tk()
root.title('Password Generator')
root.config(bg='black')
#root.geometry('280x380')

choice = IntVar()
# for password generator label 

password_label = Label(root,text='PASSWORD GENERATOR',fg='white',bg='black')
password_label.grid(pady=(20,10))
password_label.config(font=('Times new roman',14,'bold'))

# for email
email_label = Label(root,text="User Input ",fg='white',bg="black")
email_label.grid()
email_label.config(font=('fantasy',12,'bold'))

# #for email input box
# email_input =Entry(root,width=40)
# email_input.grid(pady=(1,10))

# for weak button
weak = Radiobutton(root,text='Weak',variable=choice,value=1)
weak.grid(pady=5)
weak.config(font=('vendana',13,'bold'))

# for mediam button
mediam = Radiobutton(root,text='Mediam',variable=choice,value=2)
mediam.grid(pady=5)
mediam.config(font=('vendana',13,'bold'))

# for strong button
strong = Radiobutton(root,text='Strong',variable=choice,value=3)
strong.grid(pady=5)
strong.config(font=('vendana',13,'bold'))

# for password length 
password_length = Label(root,text="Password length",fg='white',bg='black')
password_length.grid(pady=(5))
password_length.config(font=('vedana',13,'bold'))

# for spin box of password length
password_spin = Spinbox(root,from_=5,to=20,width=5)
password_spin.grid(pady=(5))
password_spin.config(font=('vendana',13,'bold'))

#  for genarate button 

genarate_button = Button(root,text="Genarate",fg="white",bg="black",command=genarator )
genarate_button.grid(pady=(5))
genarate_button.config(font=("vendana",13,"bold"))



#  for password  length input

password_genarate = Entry(root,width=40)
password_genarate.grid(pady=(1,10))


root.mainloop()