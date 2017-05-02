from Contact.AddressBook import AddressBook

from kivy.app import App, Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar
from kivy.properties import ObjectProperty

class RootWidget(BoxLayout):
    screen_manager = ObjectProperty(None)

class AddressBookScreenManager(ScreenManager):
    pass

class AddressBookApp(App):

    def build(self):
        return RootWidget()

class MenuBar(ActionBar):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def new_entry(self):
        self.screen_manager.current = 'new_entry'

    def list_entries(self):
        self.screen_manager.current = 'list_entry'

    def search_entries(self):
        self.screen_manager.current = 'search_entry'


class WelcomeScreen(Screen):
    pass

class NewEntryScreen(Screen):
    pass

class ListEntryScreen(Screen):
    pass

class SearchEntryScreen(Screen):
    pass

if __name__ == '__main__':
    AddressBookApp().run()

    # def menu_prompt():
    #     print("Select an option:")
    #     print('(A)dd new entry')
    #     print('(L)ist entries')
    #     print('(S)earch entries')
    #     print('(Q)uit')
    #     option = input()[:1].lower()
    #     return option
    #
    #
    # address_book = AddressBook()
    #
    #
    # def display_entries(entries):
    #     index = 1
    #     for entry in entries:
    #         print('-- Entry {} --'.format(str(index)))
    #         print('Id:' + str(entry.get_id()))
    #         print('Name:' + entry.get_name())
    #         print('Telephone:' + entry.get_telephone())
    #         index += 1
    #
    #     print('-- End of entries --')
    #
    #
    # while (True):
    #     option = menu_prompt()
    #     if option == 'a':
    #         print('--Add New Entry--')
    #         address_book.add_entry()
    #     if option == 'l':
    #         entries = address_book.get_entries()
    #         display_entries(entries)
    #     if option == 's':
    #         term = input('Search:')
    #         entries = address_book.search(term)
    #         display_entries(entries)
    #     if option == 'q':
    #         print('Bye!')
    #         quit(0)
