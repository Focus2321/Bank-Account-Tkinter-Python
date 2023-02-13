class user_account_class:
    def __init__(self,user_index,user_info):
        self.user_index = user_index
        self.user_username = user_info[0]
        self.user_password = user_info[1]
        self.user_balance = user_info[2]
        self.user_name = user_info[3]
        self.user_email = user_info[4]
        self.user_phone_number = user_info[5]
    
    #Conver array to string
    def listToString(self,s):
        str1 = ""
        for ele in s:
            if ele == s[-1]:
                str1 += ele
            else:
                str1 += f'{ele}/'
 
    # return string
        return str1

    def update_information(self,user_index,old_value_index,new_value):

        #Find string and change the value
        with open('user_information.txt','r') as l:
            lines = l.readlines()
            self.old_string = lines[user_index]
            self.new_string = lines[user_index].split('/')
            self.new_string[old_value_index] = new_value

            self.new_string = self.listToString(self.new_string)

        l.close()

    #Replace old value with the new one
        with open('user_information.txt','r') as r:
            information = r.read()
            information = information.replace(self.old_string,self.new_string)

    #Write information upadated in file
        with open('user_information.txt','w') as w:
            w.write(information)


    def set_deposit_balance(self,amount):
        self.new_deposit_balance = float(amount) + float(self.user_balance)
        self.user_balance = self.new_deposit_balance
        self.update_information(self.user_index,2,self.user_balance)
    
    def set_withdraw_balance(self,amount):
        self.new_withdraw_balance = float(self.user_balance) - float(amount)
        self.user_balance = self.new_withdraw_balance
        self.update_information(self.user_index,2,self.user_balance)

    def balance_currency_format(self):
        self.balance_currency = self.user_balance
        if self.user_balance == 0:
            return '$0.00'
        else:
        # Both combined along with the currency symbol(in this case $)
            currency_string = "${:,.2f}".format(float(self.balance_currency))
            return currency_string