from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        btn = Button(text = 'This is Button!!! ')
        return btn


MyApp().run()

