#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.1

def main():
    # Code goes here
    print('\n==========Exercise 1.5.1===========')

    # The first set should be called ‘players’, and contain at least ten unique names.
    players = {'Ankur', 'Tim', 'Farbod', 'David', 'Adam', 'Rakesh', 'Jon', 'Fabino', 'Jim', 'Alex'}

    # The second set should be called ‘injured_players’, and contain a few names of players from the first set.
    injured_players = {'Fabino', 'Jim', 'Alex'}

    # Create a set which results in a set containing all active (non-injured) players.
    Set = players.symmetric_difference(injured_players)

    print('Non injured players list:', Set)


    #What’s the benefit?
    #sets cannot have multiple occurrences of the same element,
    # it makes sets highly useful to efficiently remove duplicate values from a list or tuple and to
    # perform common math operations like unions and intersections.

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()

