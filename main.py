from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.theming import ThemeManager

# Define the app layout
class MyAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyAppLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Add a label
        self.label = Label(text="Hello, Kivy!")
        self.add_widget(self.label)
        
        # Add a button
        self.button = Button(text="Click Me!")
        self.button.bind(on_press=self.on_button_click)
        self.add_widget(self.button)
    
    # Button click event
    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"

# Define the app class
class MyApp(App):
    def build(self):
        return MyAppLayout()

# Run the app
if __name__ == '__main__':
    MyApp().run()