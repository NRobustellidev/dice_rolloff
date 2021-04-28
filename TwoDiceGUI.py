"""
Program: TwoDiceGUI.py
Author: Nicholas
Date: 4/28/2021

GUI based application that has the player and the computer roll a die to compete for the highest roll.
"""

from breezypythongui import EasyFrame
import random

class TwoDice(EasyFrame):
    """ Sets up the two dice game. """
    
    def __init__(self):
        """ Sets up the window and widgets. """
        EasyFrame.__init__(self, title = "Two Dice Roll Off", resizable = False, background = "cyan")
        self.addLabel(text = "Two Dice Roll Off", row = 0, column = 0, columnspan = 4, sticky = "NSEW", background = "cyan").config(font = ("Courier", 20))
        self.addLabel(text = "The players die: ", row = 1, column = 0, background = "cyan")
        self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1)
        self.addLabel(text = "The computers die: ", row = 2, column = 0, background = "cyan")
        self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1)
        
        self.button = self.addButton(text = "Roll!", row = 3, column = 0, columnspan = 4, command = self.roll)
        
        self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 4, sticky = "NSEW")
    
    def roll(self):
        # Variables and constants
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        self.playerRoll.setNumber(num1)
        self.computerRoll.setNumber(num2)
        
        # Calculation phase
        if num1 > num2:
            result = "Your numbers higher! You win!"
        elif num1 < num2:
            result = "The computers number is higher! The computer wins!"
        else:
            result = "The numbers match! It's a tie!"
        
        # Output phase
        self.resultArea["text"] = result

# Definition of the main() function for program entry
def main():
    """ Instantiates and pops up the window. """
    TwoDice().mainloop()

# Global call to the main() function
main()