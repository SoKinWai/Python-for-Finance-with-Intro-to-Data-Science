#Student Name: Jianwei Su
#Date: 05/13/2022
#6.1.3


from utils.timer import timer
from Monty_Hall.game import Game
from Monty_Hall.player import Player
import logging
import random
from utils.timer import timer


#The average of this list should be the approximate probability of winning with your
#chosen strategy (stay or switch). Time this function (it may take some time)
#strategy=True means to stay and strategy=False means to switch

@timer
def monte_pro(game,N):

    list_a = [game.playGame() for i in range(N)]

    pro=list_a.count(True)/len(list_a)
    return logging.info(f'The winning probability is {pro}')




def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)


    #Note down your hypothesis
    #I think choosing to stay or choosing to switch should have the same probability.


    logging.info('\n==========Exercise 6.1.3=========')
    logging.info('\n------Testing block 1-----')
    logging.info('Play the game one time from main to verify that it works')


    player_a=Player(True)
    player_b=Player(False)

    game_a=Game(player_a)
    game_b=Game(player_b)

    #Choose True means stay and choose False means switch
    #The result False means lose and True means win.

    logging.info(f'Choosing to switch to another door:{game_b.playGame()}')

    #Play again
    logging.info(f'Playing again and this time choosing to stay with the previous door:{game_a.playGame()}')

    logging.info('\n')
    logging.info('------Testing block 2-----')
    logging.info('Play the game in a loop of 10,000,000 times')

    logging.info('\n')
    logging.info(f'The time taken and the winning probability for choosing to stay with the chosen door will be:')
    monte_pro(game_a,10000000)

    logging.info('\n')

    logging.info(f'The time taken and the winning probability for choosing to switch to the new door will be:')
    monte_pro(game_b,10000000)


    #Was your hypothesis correct?
    #No, my hypothesis was wrong. People should choose to switch the door because switching the door would have much better chance to win.

    logging.info('\n***Program Complete***')



if __name__ == '__main__':
    main()
