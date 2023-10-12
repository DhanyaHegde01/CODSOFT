from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import string

class PasswordGeneratorApp(App):
    def build(self):
        self.title = 'Password Generator'

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.password_label = Label(text='', font_size=24)
        length_label = Label(text='Password Length:')
        self.length_input = TextInput(multiline=False, input_filter='int', input_type='number')

        generate_button = Button(text='Generate Password')
        generate_button.bind(on_press=self.generate_password)

        layout.add_widget(length_label)
        layout.add_widget(self.length_input)
        layout.add_widget(generate_button)
        layout.add_widget(self.password_label)

        return layout

    def generate_password(self, instance):
        length = int(self.length_input.text)
        password = self.generate_random_password(length)
        self.password_label.text = password

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

if __name__ == '__main__':
    PasswordGeneratorApp().run()
