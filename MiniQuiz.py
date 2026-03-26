
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("MiniQuiz.kv")

class FirstScreen(Widget):
    answers = []
    correct_answers = ["Thor", "Hulk"]

    def chckbox_click1(self, instance, value, selected):
        if value == True:
            self.answers.append(selected)
            self.ids.display1.text = f"Your selection: {self.answers}"
        else:
            self.answers.remove(selected)
            self.ids.display1.text = f"Your selection: {self.answers}"
            


class SecondScreen(Widget):
    answers = []
    correct_answers = ["Superman", "Batman"]

    def chckbox_click2(self, instance, value, selected):
        if value == True:
            self.answers.append(selected)
            self.ids.display2.text = f"Your selection: {self.answers}"
        else:
            self.answers.remove(selected)
            self.ids.display2.text = f"Your selection: {self.answers}"
    