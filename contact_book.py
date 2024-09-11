contact = {}

def display_contact():
    print('Name\t\tComponent Number')
    for key in contact:
        print('{}\t\t{}'.format(key,contact.get(key)))

while True:
    choice = int(input(' 1.Add Contact \n 2.Search Contact \n 3.View Contact \n 4.Update Contact \n 5.Delete Contact \n 6.Exit \n Enter which you need: '))
    if choice == 1:
        name = input('Enter the contact name: ')
        phone = input('Enter the mobile number: ')
        contact[name] = phone
    elif choice == 2:
        search_name = input('Enter the contact name: ')
        if search_name in contact:
            print(search_name,' -- ', contact[search_name])
        else:
            print('Name is not found in the list!')
    elif choice == 3:
        if not contact:
            print('Empty contact list!')
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input('Enter the contact to edit: ')
        if edit_contact in contact:
            phone = input('Enter mobile number: ')
            contact[edit_contact]=phone
            print('contact updated')
            display_contact()
        else:
            print('Name is not found in the list!')
    elif choice == 5:
        del_contact = input('Enter the contact to delete: ')
        if del_contact in contact:
            confirm = input('Want to delete this contact? (y/n): ')
            if confirm =='y' or confirm =='y':
                contact.pop(del_contact)
            display_contact()
        else:
            print('Name is not found in contact list')
    else:
        break

