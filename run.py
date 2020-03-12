#!/usr/bin/env python3
from contacts_app import Contact

def create_contact(fname, lname, phone,email):
    new_contact=Contact(fname, lname, phone, email)
    return new_contact
def save_contacts(contact):
    contact.save_contact()
def del_contact(contact):
    contact.delete_contact()
def find_contact(number):
    return Contact.find_by_number(number)
def check_existing_contacts(number):
    return Contact.contact_exist(number)
def display_contacts():
    return Contact.display_contacts()


def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name=input()
    #print("Hello {user_name}.What would you like to do?")
    print("Hello " + user_name + ".What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: cc - create a new contact, dc- display contacts, fc- find a contact, ex - exit the contact list")
        short_code=input().lower()
        if short_code == 'cc':
            print("New Contact")
            print("-" *10)
            print("First name.....")
            f_name=input()
            print("Last name....")
            l_name=input()
            print("Phone number....")
            p_number=input()
            print("Email address....")
            e_address=input()
            save_contacts(create_contact(f_name,l_name,p_number,e_address))
            print('\n')
            print("New Contact"+f_name+" "+l_name+ "created")
            print('\n')
        elif short_code =='dc':
             if display_contacts():
                    print("Here is a list of all your contacts")
                    print('\n')
                    for contact in display_contacts():
                        print("{contact.first_name},{contact.last_name}....{contact.phone_number}")
                        print('\n')
             else:
                 print('\n')
                 print("You dont seem to have any contacts saved yet")
                 print('\n')
        elif short_code =='fc':
             print("Enter the number you want to search for")
             search_number=input()
             if check_existing_contacts(search_number):
                 search_contact= find_contact(search_number)
                 print("{search_contact.first_name} {search_contact.last_name}")
                 print('-'*20)
                 print("Phone number.....{search_contact.phone_number}")
                 print("Email address....{search_contact.email}")
             else:
                print("That contact does not exist")
        elif short_code == "ex":
             print("Exit")
             break
        else:
            print("Please use short code")

if __name__ == "__main__":
    main()