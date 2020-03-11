class Contact:# a class that generates new instances of contacts
    contact_list=[] #empty contact list

    def save_contact(self):
        Contact.contact_list.append(self)#saves contact objects into contact_list
    def __init__(self, first_name, last_name,phone_number, email):
        #__init__allows us to pass in properties for the new object
        #self is a variable that represents the instance of the object itself
        self.first_name= first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email




#open the terminal- python3
#>>> from contacts_app import Contacts
#>>> new_contact=Contact("first_name", "last_name","phone_number","email")
#>>> new_contact.first_name- this will display the contacts first name
