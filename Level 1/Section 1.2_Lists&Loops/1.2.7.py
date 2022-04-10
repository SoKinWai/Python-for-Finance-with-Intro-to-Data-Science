#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.7


def main():
    # Code goes here
    print('\n==========Exercise 1.2.7===========')

    # The first list should be called ‘players’, and contain at least ten unique names.
    players=['Ankur','Tim', 'Farbod', 'David', 'Adam', 'Rakesh', 'Jon', 'Fabino','Jim', 'Alex']

    #The second list should be called ‘injured_players’, and contain a few names of players from the first list.
    injured_players=['Fabino', 'Jim', 'Alex']

    #Create a list comprehension which results in a list containing all active (non-injured) players.
    # This is a list comprehension results all players in list playes but not in list injured_players.
    List=[i for i in players if i not in injured_players]

    #Here prints put the non injured players from list players.
    print('Non injured players list:',List)

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()