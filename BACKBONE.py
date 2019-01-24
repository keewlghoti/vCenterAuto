"""
Author: Mike Bell
Date:
Description:
Instructions:
Expected Behavior-
How to call-
Methods-
Attributes-
Exceptions that will be raised-
What to pass-
"""
from vCenterAuto import MENUS
import vCenterAuto.MENUS

class RuntimeMenus:

    mainmenuoptions = {1: 'Start vCenter automation suite',
                       2: 'Manage your account',
                       3: 'Exit'}

    def mainmenuoption1(self): #change the print statement to a method
        print('Not yet implemented')

    def mainmenuoption2(self):  #change the print statement to a method
        print('Not yet implemented')

    def mainmenuoption3(self):  #change the print statement to a method
        print('Goodbye')
        exit()

    mainmenuactions = {1: mainmenuoption1, 2: mainmenuoption2, 3: mainmenuoption3} method(args)

class Runtime:
    def __init__(self):
        print('Start of Runtime()')
        print('Welcome to vCenter Automation Suite.')
        while True:
            try:
                MENUS.Menu(RuntimeMenus.mainmenuoptions, RuntimeMenus.mainmenuactions)
            except MENUS.Menu.ValueTooHigh:
                print('Please enter a valid choice')
            except MENUS.Menu.CorrectTheLists:
                print('Please pass in correct size lists.')


        print('End of Runtime()')





class Ignition:
    @staticmethod
    def start():
        while True:
            Runtime()


if __name__ == '__main__':
    Ignition.start()