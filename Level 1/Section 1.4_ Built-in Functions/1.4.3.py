#Student name: Jianwei Su
#Date: 04/06/2022
#1.4.3

import random

#a
#Mortgage_amounts() function
#It returns 100 random numbers from 100 to 1000
def Mortgage_amounts():
    return [random.randint(100, 1000) for iter in range(100)]



def main():
    # Code goes here
    print('\n==========Exercise 1.4.3===========')

    # mortgage_amounts has 100 mortgage amounts,range from 100 to 1000
    # Print mortgage_amounts on screen
    mortgage_amounts = Mortgage_amounts()
    print("A function that returns an unsorted list of mortgage amounts,range from 100 to 1000(in thousands):", mortgage_amounts,
          '\n')


    #Sum the full list of mortgages, to obtain the total amount owed to your firm.
    sum_mortgages=sum(mortgage_amounts)
    print("Sum the full list of mortgages, to obtain the total amount owed to your firm(in thousands):",sum_mortgages)

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()
