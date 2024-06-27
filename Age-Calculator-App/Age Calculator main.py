""" Age Calculator """
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from sys import exit
from datetime import datetime

KV = """
MDScreen:
    FloatLayout:
        orientation: 'vertical'
        
        # --- App Name --- #
        MDTopAppBar:
            title:'Age Calculator'
            height:'50dp'
            type:'top'
            top: 1
            pos_hint: {'y':.93}
            left_action_items: [["menu", app.menubar]]
            right_action_items: [["close",exit]]
       
        MDLabel:
            id: output_label
            text: "Enjoy Age Calculator!"
            halign: 'center'
            theme_text_color: 'Secondary'
            font_style: 'H4'
            pos_hint: {'y':.3}
            
        MDTextField:
            id: dob_input
            icon_left: "account"
            hint_text: 'Enter your DOB'
            size_hint_x: None
            width: 400
            font_size: 40
            halign: "center"
            helper_text: "In this format(dd/mm/yyyy) e.g. 15/04/2012"
            helper_text_mode: "on_focus"
            mode: "rectangle"
            line_color_normal: [0,0,0,.8]
            line_color_focus: [0,0,1,1]
            pos_hint: {'center_x':0.5,'center_y':0.6}

        MDRectangleFlatButton:
            text: 'Calculate my age'
            width: "200dp"
            pos_hint: {'center_x': .5, 'center_y': .3}
            on_release: app.calculate()
"""

class AgeCalculator(MDApp):
        
    def build(self):
        self.root = Builder.load_string(KV)
        return 
    
    def calculate(self):
        dob_string = self.root.ids.dob_input.text
        if dob_string == "":
            self.show_message("Please enter DOB first!")
            return
        # getting age difference
        months, years = self.get_age_difference(dob_string)
        # updating the information
        self.root.ids.output_label.text = f"You are {years} years &\n{months} months old."
        # clear the DOB input field
        self.root.ids.dob_input.text = ""
    
    def get_age_difference(self, dob_string: str):
        # user's date
        dob_elements = dob_string.strip().split('/')
        dob_month, dob_year = int(dob_elements[1]), int(dob_elements[2])
        # Today date
        today = datetime.today().date()
        # difference
        years: int = today.year - dob_year
        months: int = today.month - dob_month
        if months < 0:
            months += 12
            years -= 1   
        return (months,years)
    
    def show_message(self, text: str):
        self.dialog = MDDialog(
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.close_dialog,
                )
            ],
        )
        self.dialog.open()
        
    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)
    
    def menubar(self, *args):
        self.show_message("Menu button is not currently working.")


if __name__ == "__main__":
    AgeCalculator().run() # calling main class
