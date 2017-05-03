from Contact.AddressBook import AddressBook

from kivy.app import App, Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar
from kivy.properties import ObjectProperty, NumericProperty, StringProperty


class RootWidget(BoxLayout):
    screen_manager = ObjectProperty(None)


class AddressBookScreenManager(ScreenManager):
    pass


class AddressBookApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address_book = AddressBook();

    def build(self):
        return RootWidget()


class MenuBar(ActionBar):
    pass


class DataGrid(GridLayout):
    def add_row(self, data):
        for item in data:
            col_label = Label(text=str(item))
            self.add_widget(col_label)

        action_button = Button(text='Edit')
        self.add_widget(action_button)

    def reset(self):
        if(len(self.children) > self.cols):
            for child in self.children[:-self.cols]:
                self.remove_widget(child)

class WelcomeScreen(Screen):
    pass


class EntryScreen(Screen):
    pass


class ListEntryScreen(Screen):
    data_grid = ObjectProperty(None)

    def on_enter(self, *args):
        super().on_enter(*args)

        self.data_grid.reset()

        address_book = App.get_running_app().address_book;

        data = address_book.get_entries();
        for row in data:
            self.data_grid.add_row(row.get_data().values())


class SearchEntryScreen(Screen):
    pass


class EntryForm(BoxLayout):
    entry_id = NumericProperty(None)
    name = StringProperty('')
    telephone = StringProperty('')

    def save(self):
        properties = {
            'name': self.name,
            'telephone': self.telephone
        }
        address_book = App.get_running_app().address_book;
        address_book.add_entry(**properties);


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
