from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.names = ""
        main_layout = BoxLayout(orientation="vertical")
        self.addNames = TextInput()
        main_layout.add_widget(self.addNames)
        addButton = Button(text='add')
        addButton.bind(on_press=self.addingNames)
        main_layout.add_widget(addButton)
        self.namesBox = TextInput(multiline=True, readonly=True, font_size=55)
        main_layout.add_widget(self.namesBox)
        return main_layout

    def addingNames(self, instance):
        self.names = self.names + '\n' + self.addNames.text
        self.namesBox.text = self.names

if __name__ == "__main__":
    app = MainApp()
    app.run()