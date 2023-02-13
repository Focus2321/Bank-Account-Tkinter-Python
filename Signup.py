from tkinter import *

class CreateAccount:
    def __init__(self):
        
        #First window
        window1 = Tk()
        window1.geometry('300x300')
        window1.title('Create Account')


        #Variables
        
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.dateOfBirth = StringVar()
        self.phoneNumber = IntVar(value='')

        labelWc = Label(window1,text='Create Account',font='Arial')

        #User information labels
        frame1 = Frame(window1)

        labelFn = Label(frame1,text='First Name')
        labelLn = Label(frame1,text='Last Name')
        labelDb = Label(frame1,text='Date of Birth')
        labelPn = Label(frame1,text='Phone Number')

        #User information entries

        entryFn = Entry(frame1,textvariable=self.firstName)
        entryLn = Entry(frame1,textvariable=self.lastName)
        entryDb = Entry(frame1,textvariable=self.dateOfBirth)
        entryPn = Entry(frame1,textvariable=self.phoneNumber)

        submitBt = Button(window1,text='Submit',height=2,width=10,command=window1.destroy)


        #Positions

          #Labels
        labelWc.pack(pady=20)
        frame1.pack()
        labelFn.grid(row=0,column=0,padx=5,pady=10)
        labelLn.grid(row=1,column=0,padx=5,pady=10)
        labelDb.grid(row=2,column=0,padx=5,pady=10)
        labelPn.grid(row=3,column=0,padx=5,pady=10)
        

          #Entries
        entryFn.grid(row=0,column=1,padx=5,pady=5)
        entryLn.grid(row=1,column=1,padx=5,pady=5)
        entryDb.grid(row=2,column=1,padx=5,pady=5)
        entryPn.grid(row=3,column=1,padx=5,pady=5)

          #Submit Button
        submitBt.pack(pady=10)
        
        window1.mainloop()


    #Functions
    def check(self):
        print(self.firstName.get())
    
    

    #Submit Button Function
        



CreateAccount()

