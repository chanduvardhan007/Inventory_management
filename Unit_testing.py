import unittest
from Invoice import customer,product_details,Invoice
import pandas as pd
from Inventory_checkup import Inventory_Checkup
from pandas.util.testing import assert_frame_equal

class Test1(unittest.TestCase):
    def test1_create(self):

        '''Testing by passing correct parameters'''
        obj1=customer("chandu vardhan","kanadam","chandukanadam@gmail.com","9985532075","4720 7G bvld")
        obj2=product_details("samsung_TV","2")
        obj=Invoice()
        actual=obj.create(obj1.first_name,obj1.last_name,obj1.email,obj1.contact,obj1.address,obj2.product_name,obj2.quantity,"5")
        self.assertEqual(actual,"Invoice Generated successfully")

    def test2_create(self):

        ''' Testing invalid Numericals'''
        obj1=customer("chandu vardhan","kanadam","chandukanadam@gmail.com","+9985532075","4720 7G bvld")
        obj2=product_details("samsung_TV","2")
        obj=Invoice()
        actual=obj.create(obj1.first_name,obj1.last_name,obj1.email,obj1.contact,obj1.address,obj2.product_name,obj2.quantity,"a")
        self.assertEqual(actual,"Please give the valid data")

    def test3_create(self):

        ''' Passing invalid Email address'''
        obj1=customer("chandu vardhan","kanadam","chandukanadam@.com","9985532075","4720 7G bvld")
        obj2=product_details("samsung_TV","2")
        obj=Invoice()
        actual=obj.create(obj1.first_name,obj1.last_name,obj1.email,obj1.contact,obj1.address,obj2.product_name,obj2.quantity,"5")

        self.assertEqual(actual,"Please give the valid data")

    def test4_create(self):

        '''passing invalid Names'''
        obj1=customer("chandu1vardhan","kanadam","chandukanadam@gmail.com","9985532075","4720 7G bvld")
        obj2=product_details("samsung_TV","2")
        obj=Invoice()
        actual=obj.create(obj1.first_name,obj1.last_name,obj1.email,obj1.contact,obj1.address,obj2.product_name,obj2.quantity,"5")
    
        self.assertEqual(actual,"Please give the valid data")
    
    
    def test1_Inventory_lookup(self):

        '''Passing Inventory ID and product name to get product details'''

        test_case1=Inventory_Checkup().Product_search("1","samsung_TV") #passing Inventory ID and Product_name
        
        dataframe1=pd.DataFrame({'Product_ID': 1, 'Product_name': 'samsung_tv', 'Product_model': '4k_QLED', 'Quantity':10, 'Inventory': 'Beverly_plaza', 'Price': 500},index=[1])
        
        assert_frame_equal(test_case1,dataframe1)
    
    def test2_Inventory_lookup(self):

        '''passing Inventory ID and product name to check in wrong inventory'''

        test_case2=Inventory_Checkup().Product_search("2","samsung_TV")
        
        self.assertEqual(test_case2,"Product not found in this inventory")
    
    def test3_Inventory_lookup(self):

        '''Passing Inventory ID and product ID to get product details'''

        test_case3=Inventory_Checkup().Product_search("2","22")  #passing Inventory id and product ID
        
        dataframe2=pd.DataFrame({'Product_ID': 22, 'Product_name': 'googlesmart_TV', 'Product_model': '4k_model_1', 'Quantity':10, 'Inventory': 'Park_avenue', 'Price': 720},index=[22])
        # expected='''Product_ID Product_name Product_model  Quantity      Inventory
        #          1           1   samsung_tv       4k_QLED        10  Beverly_plaza'''
        assert_frame_equal(test_case3,dataframe2)

    def test4_Inventory_lookup(self):

        '''Passing invalid Inventory ID and product ID to retrive the product details'''

        test_case4=Inventory_Checkup().Product_search("!","22")
        self.assertEqual(test_case4,"Inventory ID doesn't exist")
    
    def test5_Inventory_lookup(self):

        '''Passing Inventory ID and wrong product ID'''

        test_case5=Inventory_Checkup().Product_search("2","23")
        self.assertEqual(test_case5,"Product not found")

    def test6_Inventory_lookup(self):

        '''Passing inventory ID and case sensitive product name to get product details'''

        test_case6=Inventory_Checkup().Product_search("2","Apple_Stereo")
        dataframe3=pd.DataFrame({'Product_ID': 21, 'Product_name': 'apple_stereo', 'Product_model': '4k_model_13', 'Quantity':12, 'Inventory': 'Park_avenue', 'Price': 540},index=[21])
        # expected='''Product_ID Product_name Product_model  Quantity      Inventory
        #          1           1   samsung_tv       4k_QLED        10  Beverly_plaza'''
        assert_frame_equal(test_case6,dataframe3)
    
    def test7_Inventory_lookup(self):

        '''Passing Inventory ID and empty product Name/ID'''

        test_case5=Inventory_Checkup().Product_search("2","")
        self.assertEqual(test_case5,"Product Name/ID or Inventory ID is missing")

        

if __name__ == '__main__':
    unittest.main()

