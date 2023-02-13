# with open('user_information.txt','r') as l:
#     data = l.read()
#     print(data)
#     data = data.replace('3570877','newpassword')



# with open('user_information.txt','w') as l:
#     l.write(data)


# class ButtonsSettings:
#     def __init__(self,cf,nf):
#         current_frame = cf
#         next_frame = nf

#     #Back button
#     def home_button_function(self):
#         current_frame.place_forget()
#     def set_home_button(self):
#         
#         home_button = Button(current_frame,text='B',command=home_button_function,font=('Arial',10),width=8)
#         home_button.place(x=300,y=300)
        


#Create back button 

# class settings:
#     def __init__(self,cf,nf):
#         next = nf()
#         current = cf
    
    
#     def home(self):
#         button = Button(current,text='Home',command=homef,width=8)
#         button.pack()
    
#     def homef(self):
#         button.pack_forget()
#         current.pack_forget()
#         next


# class test:
#     def __init__(self):
#         window = Tk()
#         window.geometry('300x300')
#         current()
        
#         mainloop()

#     def current(self):
        
#         cf = Frame(window)
#         set = settings(cf,next)
#         label = Label(cf,text='Hello').pack()
#         cf.pack()
#         set.home()
        
#     def next(self):
#         nextcf = Frame(window)
#         label2 = Label(nextcf,text='Next Frame').pack()
#         cf.pack()
#         print('Hello world')
# test()

# from tkinter import *

# class test:
#     def __init__(self):
#         window = Tk()
#         window.geometry('300x300')

#         entry = Entry(window,show='*').pack()

#         mainloop()

# test()

# with open('user_information.txt','r') as l:
#     data = l.read()
#     print(data)
#     data = data.replace('3570877','newpassword')



# with open('user_information.txt','w') as l:
#     l.write(data)

# user = lines[1].split('/')
        # print(user)
    

# def listToString(s):
 
#     # initialize an empty string
#     str1 = ""
 
#     # traverse in the string
#     for ele in s:
#         str1 += ele
 
#     # return string
#     return str1

#new_string replace string                                                                     

# with open('user_information.txt','r') as r:
#     nose = r.readlines()
#     new_string = str(nose[0])
#     print(new_string)

# with open('user_information.txt','r') as l:
#     lines = l.read()
#     print(lines)
#     lines = lines.replace(new_string,'hectora/3570877/100/Hector/w.hector.us@gmail.com/(832)407-7172\n')
#     print(lines)
# r.close()
# l.close()
# with open('user_information.txt','w') as w:
#     w.write(lines)
# w.close()

#Update balance

# def listToString(s):
#         str1 = ""
#         for ele in s:
#             if ele == s[-1]:
#                 str1 += ele
#             else:
#                 str1 += f'{ele}/'
 
#     # return string
#         return str1

# def update_information(user_index,old_value_index,new_value):

#     #Find string and change the value
#     with open('user_information.txt','r') as l:
#         lines = l.readlines()
#         old_string = lines[user_index]
#         new_string = lines[user_index].split('/')
#         print(new_string)
#         new_string[old_value_index] = new_value
#         print(new_string)

#         new_string = listToString(new_string)

#     l.close()

#     #Replace old value with the new one
#     with open('user_information.txt','r') as r:
#         information = r.read()
#         print(information)
#         information = information.replace(old_string,new_string)
#         print(information)

#     #Write information upadated in file
#     with open('user_information.txt','w') as w:
#         w.write(information)

# update_information(1,2,300)


character = 'A'
password = '*Gector*a'
lenght_flag = False
special_character_flag = False
uppercase_flag = False

for letter in password:
    if 41<= ord(letter) <= 47:
        special_character_flag = True
    elif 65<=ord(letter)<=89:
        uppercase_flag = True
    if special_character_flag and uppercase_flag:
        print('correct password')
        break