import unittest#importing the unittest module
#importing the contact class

from contacts_app import Contact

class TestContact(unittest.TestCase):#TestContact is a subclass that inherits from unittest.TestCase
    def setUp(self):
        self.new_contact=Contact("John","Doe","0749319133","johndoe@gmail.com")#create contact object
    def test_init(self):
        #test_init test case to test if the object is initialized properly
        #self.assertEqual checks for an expected result
        self.assertEqual(self.new_contact.first_name,"John")
        self.assertEqual(self.new_contact.last_name,"Doe")
        self.assertEqual(self.new_contact.phone_number,"0749319133")
        self.assertEqual(self.new_contact.email,"johndoe@gmail.com")

if __name__ == "__main__":
    unittest.main()#provides a command line interface

#saving contacts

def test_save_contact(self):#case to test if the contact object is saved into the contact list
    self.new_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),1)#to check the length from the contact list to ensure there is an addition
if __name__ == "__main__":
    unittest.main()

#saving multiple contacts
def tearDown(self):
    Contact.contact_list=[]
    #tearDown is a method that does clean up after each test case has run

def test_save_multiple_contact(self):  #checks if one can save multiple contacts
    self.new_contact.save_contact()
    test_contact=Contact("Test", "user", "0712345678","test@user.com")
    test_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),2)
if __name__ == "__main__":
    unnitest.main()

#deleting contacts

def test_delete_contact(self):
    self.new_contact.save_contact()
    test_contact=Contact("Test","user","0712345678", "test@user.com")
    test_contact.save_contact()
    self.new_contact.delete_contact()
    self.assertEqual(len(Contact.contact_list),1)
if __name__ == "__main__":
    unnitest.main()

def delete_contact(self):#this deletes a saved contact from the contact_list
    Contact.contact_list.remove(self)

#finding a contact by phone number and display info

def test_find_contact_by_number(self):
    self.new_contact.save_contact()
    test_contact=Contact("Test","user","0712345678", "test@user.com")
    test_contact.save_contact()
    found_contact=Contact.find_by_number("0712345678")
    self.assertEqual(found_contact.email,test_contact.email)


    #DECORATORS
@classmethod#Informs the python interpreter that this is a method that belongs to the entire class
def find_by_number(cls,number):
        #takes in a number and returns a contact that matches that number
       

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact 

#to check if a contact object actually exists


def test_contact_exists(self):
    self.new_contact.save_contact()
    test_contact=Contact("Test", "user","071234678" ,"test@user.com")#new contact
    test_contact.save_contact()
    contact_exists=Contact.contact_exists("0712345678")
    self.assertTrue(contact_exists)

@classmethod
def contact_exists(cls, number):
    for contact in cls.contact_list:
        if contact.phone_number == number:
            return True
    return False




