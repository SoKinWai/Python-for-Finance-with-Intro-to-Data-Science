#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.3

import random

#Mortgage_amounts() function
#It returns 10 random numbers from 0 to 1000
def Mortgage_amounts():
    return [random.randint(0, 1000) for iter in range(10)]

def main():
    # Code goes here
    print('\n==========Exercise 1.5.3===========')

    # Use {} to make sure each number is unique, then use [] to convert to a list
    # mortgage_amounts has 10 mortgage amounts,range from 0 to 10
    # Print mortgage_amounts on screen
    mortgage_amounts=list(set(Mortgage_amounts()))
    print("A list of unique mortgage amounts:",mortgage_amounts)

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()



