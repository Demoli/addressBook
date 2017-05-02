from Contact.AddressBook import AddressBook

print('--Welcome to SuperContactBook 0.1 Alpha--')


def menu_prompt():
    print("Select an option:")
    print('(A)dd new entry')
    print('(L)ist entries')
    print('(S)earch entries')
    print('(Q)uit')
    option = input()[:1].lower()
    return option


address_book = AddressBook()


def display_entries(entries):
    index = 1
    for entry in entries:
        print('-- Entry {} --'.format(str(index)))
        print('Id:' + str(entry.get_id()))
        print('Name:' + entry.get_name())
        print('Telephone:' + entry.get_telephone())
        index += 1

    print('-- End of entries --')


while (True):
    option = menu_prompt()
    if option == 'a':
        print('--Add New Entry--')
        address_book.add_entry()
    if option == 'l':
        entries = address_book.get_entries()
        display_entries(entries)
    if option == 's':
        term = input('Search:')
        entries = address_book.search(term)
        display_entries(entries)
    if option == 'q':
        print('Bye!')
        quit(0)