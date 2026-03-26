
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
    
    def next1(self):
        for element in self.answers:
            if element in self.correct_answers:
                MainApp.points += 1
        MainApp.ScrnMngr.current = "second screen"


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

    def next2(self):
        for element in self.answers:
            if element in self.correct_answers:
                MainApp.points += 1
        MainApp.results.ids.results.text = "Your points: " + str(MainApp.points) + "/4"        
        MainApp.ScrnMngr.current = "results"


class Results(Widget):
    def restart(self):
        MainApp.points = 0

        for screen in MainApp.root.screens:
            for child in screen.children:

                for k, v in child.ids.items():
                    v.active = False

        MainApp.ScrnMngr.current = "first screen"


class MainApp(App):
    points = 0
    def build(self):
        self.ScrnMngr = ScreenManager()

        self.FirstScreen = FirstScreen()
        fscreen = Screen(name = "first screen")
        fscreen.add_widget(self.FirstScreen)
        self.ScrnMngr.add_widget(fscreen)

        self.SecondScreen = SecondScreen()
        sscreen = Screen(name = "second screen")
        sscreen.add_widget(self.SecondScreen)
        self.ScrnMngr.add_widget(sscreen)

        self.results = Results()
        rscreen = Screen(name = "results")
        rscreen.add_widget(self.results)
        self.ScrnMngr.add_widget(rscreen)

        return self.ScrnMngr

MainApp= MainApp()        
MainApp.run()