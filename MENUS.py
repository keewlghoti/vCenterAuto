"""
Author: Mike Bell
Date: 19JAN2019
Description: This is a module that will allow you to dynamically create menus from two equal sized dictionaries.
Instructions:
Expected Behavior
    This module will have 2 dictionaries passed to it, test various conditions to build a menu from those dictionaries,
    build the menu, test user input, and then execute upon proper user input. Exceptions will be thrown if any of the
    conditions are not suited for menu creation or interaction. This module will not return a value.
How to call:
    MENUS.Menu([dictionary1], [dictionary2])
Methods:
    None
Attributes:
    None
Exceptions that will be raised:
    ValueError - for a non int value
    CorrectTheLists - if lists are not an equal size
    ValueTooHigh - if the user enters a interger higher than the largest index
What to pass:
    dictionary1
        This dictionary is what the menu items are. Needs to be in format:
        dicname = {1: value, 2: value, ... n: value}
    dictionary 2
        This dictionary is what the menu items do. These need to be neutered, external method calls.
        neutered methods DO NOT include the '()' at the end
        dicname = {1: MOD.Class.method, 2: MOD.Class.method, ... n: MOD.Class.method}
Lets do this, fucking pass in lists, get a built menu out.
"""

# Building test menus - testing purposes only
menu1 = {1: 'Choice 1',
         2: 'Choice 2',
         3: 'Choice 3'}

menu2 = {1: 'Choice 1',
         2: 'Choice 2',
         3: 'Choice 3',
         4: 'Choice 4'
         }

# Building test result - testing purposes only
result1 = {1: 'Choice -1',
           2: 'Choice -2',
           3: 'Choice -3'
           }
result2 = {1: 'Choice -1',
           2: 'Choice -2',
           3: 'Choice -3',
           4: 'Choice -4'
           }

# test class with test methods - testing purposes only
class Testmethod:
    def test1(self):
        print(result2.get(1))

    def test2(self):
        print(result2.get(2))

    def test3(self):
        print(result2.get(3))

    def test4(self):
        print(result2.get(4))


#create a list of the methods. I DO NOT USE method() as that will make it execute. These get called in class Menu.
# - testing purposes only
result3 = {1: Testmethod.test1, 2: Testmethod.test2, 3: Testmethod.test3, 4: Testmethod.test4}

"""
All code above is for testing.
All code below is production
"""

class Menu:
    #get the class dictonaries started early
    menu = {}
    result = {}

    #make my own exceptions
    class CorrectTheLists(Exception):
        #raised when lists don't match
        pass
    class ValueTooHigh(Exception):
        #raised when a value that is too high is entered
        pass

    # create the menu object - all code is executed upon creation
    def __init__(self, mlistin, rlistin):
        #passing args for creation
        self.menu = mlistin
        self.result = rlistin

        #test args for equal status
            #testing values
        self.x = int(len(self.menu))
        self.y = int(len(self.result))

        #check to see if lists match
        if self.x != self.y:
            raise Menu.CorrectTheLists
        else:

        #building the menu
            print('*********************')
            print('MENU CREATION')
            print('*********************')

            # print each menu item
            self.options = self.menu.keys()
            self.test = sorted(self.options)
            for self.entry in self.test:
                print(self.entry, self.menu[self.entry])

            #get user input and test it
            self.selection = None
            self.z = 0
            while self.selection == None: #runs until a proper input was passed.
                try: #this try block looks for an interger input
                    print('Please Select:')
                    self.selection = int(input()) #USERINPUT
                    self.z = int(self.selection)
                    if self.z > self.y: #this if statement looks for the interger to be in the right range
                        print('Please enter a correct value')
                        raise Menu.ValueTooHigh
                    else:
                        # this code runs the neutered methods- we literally add the '(self)' to method(self) here.
                        self.result.get(self.z)(self)

                except ValueError:
                    print('integer')
                    self.selection = None

"""
Above is operational code
If this was a real module, we would not include the following code. But this is standalone and needs to be tested.
"""