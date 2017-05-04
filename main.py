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
        for item in data.values():
            col_label = Label(text=str(item))
            self.add_widget(col_label)

        id = data['id']
        action_button = Button(text='Edit', id='entry_' + str(id))
        action_button.bind(on_release=self.edit_entry);

        self.add_widget(action_button)

    def edit_entry(self, button):
        id = int(button.id.replace('entry_', ''))
        screen_manager = App.get_running_app().root.ids.address_book_screen_manager
        screen = screen_manager.ids.entry_screen

        screen.entry_id = id
        screen_manager.current = 'edit_entry'
        pass

    def reset(self):
        if (len(self.children) > self.cols):
            for child in self.children[:-self.cols]:
                self.remove_widget(child)


class WelcomeScreen(Screen):
    pass


class EntryScreen(Screen):

    entry_id = NumericProperty()

    def on_enter(self, *args):
        super().on_enter(*args)
        if(self.entry_id):
            self.ids.entry_form.load(self.entry_id)


class ListEntryScreen(Screen):
    data_grid = ObjectProperty(None)

    def on_enter(self, *args):
        super().on_enter(*args)

        self.data_grid.reset()

        address_book = App.get_running_app().address_book;

        data = address_book.get_entries();
        for row in data:
            self.data_grid.add_row(row.get_data())


class SearchEntryScreen(Screen):
    data_grid = ObjectProperty(None)

    def on_enter(self, *args):
        super().on_enter(*args)

        self.data_grid.reset()

    def search(self, term):
        if len(term) >= 3:
            self.data_grid.reset()
            address_book = App.get_running_app().address_book;

            data = address_book.search(term);
            for row in data:
                self.data_grid.add_row(row.get_data())
        else:
            self.data_grid.reset()

class EntryForm(BoxLayout):
    entry_id = NumericProperty(1)
    name = StringProperty('')
    telephone = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address_book = App.get_running_app().address_book;

    def load(self, id):
        entry = self.address_book.get_entry(id)
        self.entry_id = entry.get_id()
        self.name = entry.get_name()
        self.telephone = entry.get_telephone()

    def save(self):
        if(self.entry_id):
            entry = self.address_book.get_entry(self.entry_id)

        properties = {
            'name': self.name,
            'telephone': self.telephone
        }
        if(self.entry_id):
            entry.set_data(**properties)
            self.address_book.save_entry(entry);
        else:
            self.address_book.add_entry(**properties);
        screen_manager = App.get_running_app().root.ids.address_book_screen_manager



if __name__ == '__main__':
    AddressBookApp().run()