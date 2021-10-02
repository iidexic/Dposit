import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# replace with current version
kivy.require('2.0.0')

# Defining Class
class FirstKivyApp(App):

    # Function that returns root widget
    def build(self):

        # Label with text hello world
        # returned as root widget
        return Label(text = 'Hello World!')

    def closeApplication(self):

        self.stop()
        Window.close()