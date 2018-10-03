"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Tom'

M_KM = 1.60934

class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Square Number"
        self.root = Builder.load_file('KM_conversion_kiv.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        km = self.get_m_value()
        miles = km * M_KM
        self.root.ids.output_label.text = str(miles)

    def handle_increment(self, value):
        miles = self.get_m_value() + value
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()
    def get_m_value(self):
        miles = float(self.root.ids.input_miles.text)
        return miles



SquareNumberApp().run()
