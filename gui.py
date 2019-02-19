#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from file import File


class MyApp(App):

    App.title = "Little Chat"

    global ti
    global bt
    global text
    global layout_1
    global layout_2

    def onInit():
        text=File().get_text()
        return text

    ti = TextInput(text="")
    bt = Button(text=">>")
    text = TextInput(text=onInit())
    layout_1 = GridLayout(cols=1)
    layout_2= GridLayout(cols=2)

    def onClick(self):
        text.text = text.text + '\nme: ' + ti.text
        ti.text = ""
        File().write(text.text)

    def build(self):

        text.size_hint = None, None
        text.height = 300
        text.width = 300
        text.x = 50
        text.y = 130
        text.readonly= True 

        ti.size_hint = None, None
        ti.height = 100
        ti.width = 250
        ti.x = 50
        ti.y = 25

        bt.size_hint= None, None
        bt.height = 100
        bt.width = 50
        bt.x = 350
        bt.y = 75
        bt.on_press = self.onClick

        layout_1.add_widget(text)
        layout_1.add_widget(layout_2)
        layout_2.add_widget(ti)
        layout_2.add_widget(bt)

        return layout_1

Window.size = 300, 400
MyApp().run()
