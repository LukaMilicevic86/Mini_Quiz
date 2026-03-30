
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("MiniQuiz.kv")

#Create a class for the first screen that contains the function for its checkboxes:

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

#Function for keeping the score and transitioning into the second window:

    def next1(self):
        for element in self.answers:
            if element in self.correct_answers:
                MainApp.points += 1
        MainApp.ScrnMngr.current = "second screen"

#Create a class for the second screen that contains the function for its checkboxes:

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

#Function for keeping the score and transitioning into the final window:

    def next2(self):
        for element in self.answers:
            if element in self.correct_answers:
                MainApp.points += 1
        MainApp.results.ids.results.text = "Your points: " + str(MainApp.points) + "/4"        
        MainApp.ScrnMngr.current = "results"


#Create the class for the third window wuth the function to reset the score, uncheck all the ckeckboxes and return to the first screen

class Results(Widget):
    def restart(self):
        MainApp.points = 0

        for screen in MainApp.root.screens:
            for child in screen.children:

                for k, v in child.ids.items():
                    v.active = False

        MainApp.ScrnMngr.current = "first screen"


#Create the main app class which returns a screen manager, setting it as a root, and adds instances of the classes above into it as widgets

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