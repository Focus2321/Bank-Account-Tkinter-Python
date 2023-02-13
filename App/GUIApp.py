from tkinter import * 
from user_account import *
from tkinter import messagebox

 
class MainGui:

    def __init__(self): 

        #Index user 
        self.username_index = 0
        self.passowrd_index = 1
        self.deposit_index = 2
        self.name_index = 3
        self.email_index = 4
        self.phone_number_index = 5

        self.window = Tk()
        self.window.config(bg='#393E46')
        self.window.resizable(False,False)
        self.login_interface()

        
                                   #Interfaces 

    def account_settings_interface(self):

        #Settings frame
        self.user_settings_frame = Frame(self.window,bg='#393E46')

        #Home button
        self.home_button = Button(self.window,text='Home',command=self.home_button_function,font=('Arial',10))
        self.home_button.place(x=10,y=10)

        #Title
        self.user_info_title = Label(self.user_settings_frame,text='User Information',bg='#393E46',fg='#F2E7D5',font=('Arial',20)).grid(row=1,column=1,pady=20,padx=215)
        #User info
        label_user_name = Label(self.user_settings_frame,text=f'\n{self.user_information_class.user_name}',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=2,column=1,pady=7,padx=215)
        label_user_email = Label(self.user_settings_frame,text=f'\n{self.user_information_class.user_email}',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=3,column=1,pady=7,padx=215)
        label_user_phone_number = Label(self.user_settings_frame,text=f'\n{self.user_information_class.user_phone_number}',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=4,column=1,pady=7,padx=215)

        self.user_settings_frame.grid(row=0,column=0)
        
    def user_account_interface(self,user_index,user_info):
        self.user_information_class = user_account_class(user_index,user_info)
        self.window.geometry('600x600')
        self.user_account_frame = Frame(self.window,bg='#393E46')

        #Title
        label_user_account = Label(self.user_account_frame,text=f'{self.user_information_class.user_name.capitalize()} Checking Account',bg='#393E46',fg='#F2E7D5',font=('Arial',20)).grid(row=0,column=0,columnspan=2,sticky='nesw',pady=5)

        #Current balance

        self.label_current_balance = Label(self.user_account_frame,text=f'\n{self.user_information_class.balance_currency_format()}\n',bg='#393E46',fg='#F2E7D5',font=('Arial',17))
        self.label_current_balance.grid(row=1,column=0,columnspan=2,pady=7)

        #Deposit button
        self.deposit_button = Button(self.user_account_frame,text='Deposit',command=self.deposit_button_function,font=('Arial',10),width=8)
        self.deposit_button.grid(row=2,column=0,sticky=W,pady=10,padx=5)

        #Withdraw button
        self.withdraw_button = Button(self.user_account_frame,text='Withdraw',command=self.withdraw_button_function,font=('Arial',10),width=8)
        self.withdraw_button.grid(row=2,column=1,sticky=E,pady=10,padx=5)
        
        #User account
        self.account_settings_button = Button(self.window, text='Account',command=self.account_settings_function,font=('Arial',10),width=8)
        self.account_settings_button.place(x=520,y=10)

        #Logout button
        self.logout_button = Button(self.window,text='Logout',command=self.logout_button_function,font=('Arial',10),width=5)
        self.logout_button.place(x=10,y=10)#grid(row=0,column=0,sticky=N,columnspan=2,pady=10,padx=5)
        

        self.user_account_frame.grid(row=0,column=0,padx=140,pady=30)#,pady=55

        #User Account
    def transaction_interface(self,type):

        #Check if Deposit or Withdraw
        if type == 'd':
            self.transaction_type = 'Deposit'
        elif type == 'w':
            self.transaction_type = 'Withdraw'

        self.user_transaction_frame = Frame(self.window,bg='#393E46')
        
        #Title
        label_transaction = Label(self.user_transaction_frame,text='Transaction',bg='#393E46',fg='#F2E7D5',font=('Arial',17)).grid(row=0,column=0,columnspan=2,pady=5)

        #Entry transaction
        self.transaction_amount_var = StringVar()
       
        self.transaction_amount_label = Label(self.user_transaction_frame,text = f'{self.transaction_type} amount',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=1,column=0,padx=5,pady=20)
        self.transaction_amount_entry = Entry(self.user_transaction_frame,textvariable=self.transaction_amount_var).grid(row=1,column=1,pady=20)

        #Post button
        transaction_post_button = Button(self.user_transaction_frame,text='Post',command=self.post_button_function,font=('Arial',10),width=8).grid(row=2,column=0,columnspan=2,pady=20)

        self.user_transaction_frame.grid(row=1,column=0,padx=150)
        #Login 
    def login_interface(self):
        try:
            self.back_button.place_forget()
        except:
            None
        self.window.geometry('300x302')
        self.login_frame = Frame(self.window,bg='#393E46')

        #Title
        title = Label(self.login_frame,text='Bank Account',bg='#393E46',fg='#F2E7D5',font=('Arial',20)).grid(row=0,column=0,columnspan=2,pady=5)

        #Login

        label_username = Label(self.login_frame,text='Username:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=1,column=0,pady=5)
        self.username = StringVar()
        entry_username = Entry(self.login_frame,textvariable=self.username).grid(row=1,column=1,pady=5,padx=5)
        label_password = Label(self.login_frame,text='Password:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=2,column=0,pady=5)
        self.password = StringVar()
        entry_password = Entry(self.login_frame,textvariable=self.password,show='*').grid(row=2,column=1,pady=5,padx=5)

        #Login and sign up button

        login_button= Button(self.login_frame,text='Login',command=self.login_button_function,font=('Arial',10),width=5).grid(row=3,column=1,sticky=E,pady=10,padx=5)
        signup_button = Button(self.login_frame,text='Sign up',command=self.signup_interface,font=('Arial',10)).grid(row=3,column=0,sticky=W,pady=10,padx=5)


        self.login_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

        self.window.mainloop()

                #Sign up

    def signup_interface(self):

        #In case logout button starts to duplicate, turn this on mmv
        # try:
        #     self.logout_button.place_forget()
        # except:
        #     None
        self.login_frame.place_forget()
        self.window.geometry('300x350')
        self.signup_frame = Frame(self.window,bg='#393E46')
        
        #Back button
        self.back_button = Button(self.window,text='Back',command=self.back_button_function,font=('Arial',10))
        self.back_button.place(x=10,y=10)

        #Title
        create_account = Label(self.signup_frame,text='Create Account',bg='#393E46',fg='#F2E7D5',font=('Arial',20)).grid(row=0,column=0,pady=10,columnspan=2)

        #User information
        label_name = Label(self.signup_frame,text='Name:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=1,column=0,pady=7)
        self.name = StringVar()
        entry_name = Entry(self.signup_frame,textvariable=self.name).grid(row=1,column=1,pady=7,padx=5)

        label_email = Label(self.signup_frame,text='Email:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=2,column=0,pady=7)
        self.email = StringVar()
        entry_email = Entry(self.signup_frame,textvariable=self.email).grid(row=2,column=1,pady=7,padx=5)

        label_phone_number = Label(self.signup_frame,text='Phone Number:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=3,column=0,pady=7)
        self.phone_number = StringVar()
        entry_phone_number = Entry(self.signup_frame,textvariable=self.phone_number).grid(row=3,column=1,pady=7,padx=5)

        label_new_username = Label(self.signup_frame,text='Username:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=4,column=0,pady=7)
        self.new_username = StringVar()
        entry_new_username = Entry(self.signup_frame,textvariable=self.new_username).grid(row=4,column=1,pady=7,padx=5)

        label_new_password = Label(self.signup_frame,text='Password:',bg='#393E46',fg='#F2E7D5',font=('Arial',11)).grid(row=5,column=0,pady=7)
        self.new_password = StringVar()
        entry_new_password = Entry(self.signup_frame,show="*",textvariable=self.new_password).grid(row=5,column=1,pady=7,padx=5)



        #Submit Button

        submit_button = Button(self.signup_frame,text='Submit',command=self.submit_button_function,font=('Arial',10)).grid(row=6,column=1,sticky=E,pady=10,padx=5)
        self.signup_frame.place(relx=0.5,rely=0.1,anchor=N)

    

                                        #Methods

    #Back button

    #Buttons

        #Account
    def account_settings_function(self):
        self.user_account_frame.grid_forget()
        self.account_settings_button.place_forget()
        try:
            self.user_transaction_frame.grid_forget()
        except:
            None
        self.account_settings_interface()

    #Home button function
    def home_button_function(self):
        self.logout_button.place_forget()
        self.home_button.place_forget()
        self.user_settings_frame.grid_forget()
        self.user_account_interface(self.index,self.user_info)

    #Back button function
    def back_button_function(self):
        self.back_button.place_forget()
        self.signup_frame.place_forget()
        self.login_interface()

        #Logout https://www.tutorialspoint.com/how-to-see-if-a-widget-exists-in-tkinter#:~:text=To%20make%20a%20particular%20Tkinter,widget%20we%20want%20to%20check. For duplicate widgets
    def logout_button_function(self):
        self.logout_button.place_forget()
        self.account_settings_button.place_forget()
        try:
            self.back_button.place_forget()
            self.user_transaction_frame.grid_forget()
        except:
            None
        self.user_account_frame.grid_forget()
        self.login_interface()

        #Login
    def login_button_function(self):
        self.login_flag = False
        self.user_data = []
        self.login_information = []
        with open('user_information.txt','r') as l:
            for self.index,lines in enumerate(l.readlines()):
                self.user_data = lines.split('/')
                if self.user_data[0] == self.username.get() and self.user_data[1] == self.password.get():
                    print('You have are in')
                    self.user_info = self.user_data
                    self.login_frame.place_forget()
                    self.user_account_interface(self.index,self.user_info)
                    self.login_flag = True
                    break
            if not self.login_flag:
                self.login_error_window = messagebox.showerror(title = 'Error',message='Wrong password or username')

                
        
    def check_password(self,password):
        self.lenght_flag = False
        self.special_character_flag = False
        self.uppercase_flag = False

        #Check for 8 characters long
        if len(password)>=8:
            self.lenght_flag = True

        #Check for special character and uppercase letter
        for letter in password:
            if 33<= ord(letter) <= 47 or 58<= ord(letter) <= 64:
                print('Special character')
                self.special_character_flag = True
            elif 65<=ord(letter)<=89:
                self.uppercase_flag = True
            if self.special_character_flag and self.uppercase_flag:
                break

        if not self.lenght_flag:
            self.password_len_error = messagebox.showerror(title='Password',message='Password must be 8 characters long')
        elif not self.uppercase_flag:
            self.password_uppercase_error = messagebox.showerror(title='Password',message='Password must contain at least one upppercase letter')
        elif not self.special_character_flag:
            self.password_special_character_error = messagebox.showerror(title='Password',message='Password must contain at least one special character')       
        else:
            return True
        # if self.lenght_flag and self.special_character_flag and self.uppercase_flag: 
        #     return True

        #Submit sign up information
    def submit_button_function(self):
        
        self.user_balance = 0 #When account is created, the balance of the account will allways stard with 0 until the first deposit is made

        print(f'Welcome {self.name.get()} with email {self.email.get()} and phone number ({self.phone_number.get()[:3]}){self.phone_number.get()[3:6]}-{self.phone_number.get()[6:10]}')      

        #Send user information to txt file
        with open ('user_information.txt','a+') as u:
            if not self.check_password(self.new_password.get()):
                None
            else:   
                u.write(f'{self.new_username.get()}/{self.new_password.get()}/{self.user_balance}/{self.name.get()}/{self.email.get()}/({self.phone_number.get()[:3]}){self.phone_number.get()[3:6]}-{self.phone_number.get()[6:10]}\n')
                u.close()
                self.signup_frame.place_forget()
                self.login_interface()

    #Deposit button
    def deposit_button_function(self):
        self.deposit_button.grid_forget()
        self.withdraw_button.grid_forget()
        self.transaction_interface('d') #Will show transaction interface and because is a deposit the code is 'd'
    
    #Withdraw button
    def withdraw_button_function(self):
        self.deposit_button.grid_forget()
        self.withdraw_button.grid_forget()
        self.transaction_interface('w') #Will show transaction interface and because is a withdraw the code is 'w'
    
    #Post button
    def post_button_function(self):

        if self.transaction_type == 'Deposit':
            self.user_information_class.set_deposit_balance(self.transaction_amount_var.get())
            print('money has been deposited',self.user_information_class.user_balance)
        elif self.transaction_type == 'Withdraw':
            self.user_information_class.set_withdraw_balance(self.transaction_amount_var.get())

        self.user_transaction_frame.grid_forget()
        self.deposit_button.grid(row=2,column=0,sticky=W,pady=10,padx=5)
        self.withdraw_button.grid(row=2,column=1,sticky=E,pady=10,padx=5)

        

        self.label_current_balance.grid_forget()
        self.label_current_balance = Label(self.user_account_frame,text=f'\n{self.user_information_class.balance_currency_format()}\n',bg='#393E46',fg='#F2E7D5',font=('Arial',17))
        self.label_current_balance.grid(row=1,column=0,columnspan=2,pady=7)
        # self.new_balance = self.transaction_amount_var+self.user_information_class.user_balance


        # self.transaction_amount_var
        # self.user_information_class.user_balance
    
    
        


        

        

MainGui()


