#Student name: Jianwei Su
#Date: 04/06/2022
#1.4.2

import random

#a
#Mortgage_amounts() function
#It returns 100 random numbers from 100 to 1000
def Mortgage_amounts():
    return [random.randint(100, 1000) for iter in range(100)]

def main():
    # Code goes here
    print('\n==========Exercise 1.4.2===========')

    # mortgage_amounts has 100 mortgage amounts,range from 100 to 1000
    # Print mortgage_amounts on screen
    mortgage_amounts = Mortgage_amounts()
    print("A function that returns an unsorted list of mortgage amounts,in thousands,range from 100 to 1000:", mortgage_amounts,
          '\n')

    # b
    # Filter amounts below 200 from mortgage_amounts and store them in miniMortgages
    # Print miniMortgages on screen
    miniMortgages = [i for i in mortgage_amounts if i < 200]
    print("Mini Mortgages(Amounts below 200):", miniMortgages, '\n')

    # Filter amounts between 200 and 467 and store them in standardMortgages
    # Print standardMortgages on screen
    standardMortgages = [a for a in mortgage_amounts if 200 <= a <= 467]
    print("Standard Mortgages(amounts between 200 and 467):", standardMortgages, '\n')

    # Filter amounts greater than 467 and store them in jumboMortgages
    # Print jumboMortgages on screen
    jumboMortgages = [b for b in mortgage_amounts if b > 467]
    print("Jumbo Mortgages(amounts greater than 467):", jumboMortgages, '\n')

    #Find the length of each list in part b of the previous exercise.
    miniMortgages_length=len(miniMortgages)
    print("The length of Mini Mortgages:", miniMortgages_length)

    standardMortgages_length = len(standardMortgages)
    print("The length of Standard Mortgages:", standardMortgages_length)

    jumboMortgages_length=len(jumboMortgages)
    print("The length of Jumbo Mortgages:", jumboMortgages_length)

    #Verify that the lengths of all three lists indeed add up to the length of the full list in part a.
    Length_a=len(mortgage_amounts)

    #Add all three lists' lengths together
    Sum_b=miniMortgages_length+standardMortgages_length+jumboMortgages_length

    print("Verify that the lengths of all three lists indeed add up to the length of the full list in part a:",Length_a==Sum_b)

    print('\n***Program Complete***')




if __name__ == '__main__':
    main()
