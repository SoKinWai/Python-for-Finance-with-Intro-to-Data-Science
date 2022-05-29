#Student Name: Jianwei Su
#Date: 05/16/2022
#6.2.1

import logging
import random

#The player should be a class that defines the switch strategy and has functions to choose a door and whether or not to switch.
class Player(object):

    # Initialize function with player
    def __init__(self, strategy):

        self.strategy = strategy

    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument player
    @property
    def strategy(self):
        return self._strategy

    #True means to stay with the door and False means to switch the door
    @strategy.setter
    def strategy(self, istrategy):
        if istrategy ==True or istrategy==False:
            self._strategy = istrategy  # Set the instance variable strategy from input
        else:
            logging.error('Something is wrong with the parameter.')
            raise ValueError("Error: strategy has to be True or False.")




    def first_selection(self):

        return random.randint(1,3)


    def second_selection(self,host_selection):

        player_option={1,2,3}

        player_option-={host_selection,self.first_selection()}

        #strategy=True means stay and strategy=False means switch
        if self.strategy==True:
            second_choice = self.first_selection()

        else:
            second_choice =list(player_option)[0]


        return second_choice