import pandas as pd

'''Checks the given product in the Inventory'''
class Inventory_Checkup:
   
    '''Inventory 1'''
    def __Inventory_1(option):
        
        df=pd.read_csv('./product_list.csv')

        df.index = df.index + 1
        
        if (option.isnumeric()):
            if(int(option) in df['Product_ID'].values):
                df1=(df.loc[df['Product_ID'] == int(option)])
                if("Beverly_plaza" in df1.values):
                    return df1
                else:
                    return "Product not found in this inventory"

            else:
                return "Product not found"
        else:
            df['Product_name']=df['Product_name'].map(lambda x: x.casefold())
            if (option.casefold() in df['Product_name'].values):
                df1=(df.loc[df['Product_name'] == option.casefold()])
                return df1
            else:
                return "Product not found"
        

    '''Inventory 2'''
    def __Inventory_2(option):
        
        df=pd.read_csv('./product_list.csv')
        df.index = df.index + 1
        
        if (option.isnumeric()):
            if(int(option) in df['Product_ID'].values):

                df1=(df.loc[df['Product_ID'] == int(option)])
                if("Park_avenue" in df1.values):
                    return df1
                else:
                    return "Product not found in this inventory"

            else:
                return "Product not found"
        else:
            df['Product_name']=df['Product_name'].map(lambda x: x.casefold())
            if (option.casefold() in df['Product_name'].values):
                df1=(df.loc[df['Product_name'] == option.casefold()])
                if("Park_avenue" in df1.values):
                    return df1
                else:
                    return "Product not found in this inventory"
            else:
                return "Product not found"

    def Product_search(self,option1,option2):
        
        if (option1 == '' or option2 == ''):
            return "Product Name/ID or Inventory ID is missing"

        elif(option1 == "1"):
            
            obj1=Inventory_Checkup
            r=obj1.__Inventory_1(option2)
            return r
            
        elif(option1 == "2"):
            obj1=Inventory_Checkup
            r1=obj1.__Inventory_2(option2)
            return r1

        else:
            return "Inventory ID doesn't exist"

        
    


    