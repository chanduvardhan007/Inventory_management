import pandas as pd
import re
import random as rand
import datetime

class  customer:
    '''initializing private variables'''
    def __init__(self,first_name,last_name,email,contact,address):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__email=email
        self.__contact=contact
        self.__address=address
    '''Get first_name'''
    @property
    def first_name(self):
        return self.__first_name
    '''Get last_name'''
    @property
    def last_name(self):
        return self.__last_name
    '''Get email'''
    @property
    def email(self):
        return self.__email
    '''Get contact'''
    @property
    def contact(self):
        return self.__contact
    '''Get address'''
    @property
    def address(self):
        return self.__address
    '''Set first_name'''
    @first_name.setter
    def first_name(self, val):
        self.__first_name=val
    '''Set last_name'''
    @last_name.setter
    def last_name(self,val):
        self.__last_name=val
    '''Set email'''
    @email.setter
    def email(self,val):
        self.__email=val
    '''Set contact'''
    @contact.setter
    def contact(self,val):
        self.__address=val
    '''Set address'''
    @address.setter
    def address(self,val):
        self.__address=val
    

    
        
class product_details:
    '''initializing private variables'''
    def __init__(self,product_name,quantity):
        self.__product_name=product_name
        self.__quantity=quantity
    '''Get product name'''
    @property
    def product_name(self):
        return self.__product_name
    '''Get quantity'''
    @property
    def quantity(self):
        return self.__quantity
    '''Set product name'''
    @product_name.setter
    def product_name(self,val):
        self.__product_name=val
    '''Set quantity'''
    @quantity.setter
    def last_name(self,val):
        self.__quantity=val


class Invoice():
            
    '''validating contact,quantity and tax'''
    def contact_quantity_valid(contact,quantity,tax):
        if contact.isnumeric() and quantity.isnumeric() and tax.isnumeric():
            return True
        else:
            return False
    '''validating email'''
    def email_valid(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if(re.search(regex,email)):   
            return True
        else:
            return False 
    '''Validating first name and last name'''
    def firstandlastname_valid(first_name,last_name):
        print(first_name,last_name)
        if ''.join(first_name.split()).isalpha() and ''.join(last_name.split()).isalpha():
            return True
        else:
            return False
    
    ''' Validating product name'''
    def product_name_valid(product_name):
        if "".join(product_name.split('_')).isalpha():
            return True
        else:
            return False

        
    ''' Creating Invoice'''   

    def create(self,first_name,last_name,email,contact,address,product_name,quantity,tax):
        
        return_contact_quantity=Invoice.contact_quantity_valid(contact,quantity,tax)
        return_email=Invoice.email_valid(email)
        return_name=Invoice.firstandlastname_valid(first_name,last_name)
        return_product_name=Invoice.product_name_valid(product_name)

        if return_contact_quantity and return_email and return_name and return_product_name:
            
            df=pd.read_csv('./product_list.csv')
            s=list(df.loc[df.Product_name==product_name].iloc[0])
            price=s[5]
            cost = int(quantity)*int(price)
            tax_percent_dollar=int((cost * int(tax))/100)
            total_cost=cost + tax_percent_dollar
            date=datetime.datetime.now()

            

            print("************Invoice************")
            print("*******************************")
            
            print("Invoice ID:",rand.randint(1,100))
            print("Invoice Generation Date:",date.strftime("%x"))
            print("Customer ID:",rand.randint(1000,5000))
            print("Customer Name:",first_name)
            print("Customer Name:",last_name)
            print("Customer email:",email)
            print("Customer contact:",contact)
            print("Customer address:",address)
            print("Product ID:",s[0])
            print("Product Name:",s[1])
            print("Product model:",s[2])
            print("Product Quantity:",quantity)
            print("Cost before tax: ${}".format(cost))
            print("Indivdual_tax: {}%".format(tax))
            print("Total_Cost : ${}".format(total_cost))

            print("*******************************")
            

            return "Invoice Generated successfully"
        else:
            return "Please give the valid data"
            
        
    

        
       

# if __name__=="__main__":
#     print("Enter the customer first name:")
#     first_name="chandu vardhan"
#     print("Enter the customer last name:")
#     last_name="kanadam"
#     print("Enter the customer email:")
#     email="chandukanadam@gmail.com"
#     print("Enter the customer contact:")
#     contact="9985532075"
#     print("Enter the customer Address:")
#     address="4720 7G bvld"
#     print("Enter the product name:")
#     product_name="samsung_TV"
#     quantity="2"
#     individual_tax="5"

#     obj1=customer(first_name,last_name,email,contact,address)
#     obj2=product_details(product_name,quantity)
#     obj=Invoice()
#     print(obj.create(obj1.first_name,obj1.last_name,obj1.email,obj1.contact,obj1.address,obj2.product_name,obj2.quantity,individual_tax))
    


   

    


        