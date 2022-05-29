#Student Name: Jianwei Su
#Date: 05/16/2022
#6.2.1


import random


class Game(object):

    # Initialize function with player
    def __init__(self, player):

        self.player = player


    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument player
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, iplayer):
         self._player = iplayer # Set the instance variable player from input



    #playGame function
    def playGame(self):

        #Randomly places the prize behind one of three doors
        prize_door=random.randint(1,3)

        #Asks its player object to choose a door
        first_choice=self.player.first_selection()


        host_option={1,2,3}

        #Figure out which door to ‘open’ (it should be one of the two non-selected doors,
        #but it must not have the prize behind it).
        host_option-={prize_door,first_choice}
        host_selection=random.choice(list(host_option))

        #Query the player object whether or not to switch to the remaining door
        #The player object should either always switch or always not switch
        second_choice=self.player.second_selection(host_selection)

        #Check if the final chosen door is a winner or loser and return the Boolean result
        if second_choice==prize_door:
            return True

        else:
            return False