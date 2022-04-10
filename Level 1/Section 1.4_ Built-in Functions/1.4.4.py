#Student name: Jianwei Su
#Date: 04/06/2022
#1.4.4

import random

#a
#Mortgage_amounts() function
#It returns 100 random numbers from 100 to 1000
def Mortgage_amounts():
    return [random.randint(100, 1000) for iter in range(100)]



def main():
    # Code goes here
    print('\n==========Exercise 1.4.4===========')

    # mortgage_amounts has 100 mortgage amounts,range from 100 to 1000
    # Print the minimum and maximum of mortgage_amounts on screen
    mortgage_amounts = Mortgage_amounts()
    print("The minimum and maximum for Mortgage Amounts(in thousands):",min(mortgage_amounts),",",max(mortgage_amounts))


    # Filter amounts below 200 from mortgage_amounts and store them in miniMortgages
    # Print the minimum and maximum of miniMortgages on screen
    miniMortgages= [i for i in mortgage_amounts if i<200]
    print("The minimum and maximum for Mini Mortgages(in thousands):",min(miniMortgages),",",max(miniMortgages))

    # Filter amounts between 200 and 467 and store them in standardMortgages
    # Print the minimum and maximum of standardMortgages on screen
    standardMortgages=[a for a in mortgage_amounts if 200<=a<=467]
    print("The minimum and maximum for Standard Mortgages(in thousands):",min(standardMortgages),",",max(standardMortgages))

    # Filter amounts greater than 467 and store them in jumboMortgages
    # Print the minimum and maximum of jumboMortgages on screen
    jumboMortgages=[b for b in mortgage_amounts if b>467]
    print("The minimum and maximum for Jumbo Mortgages(in thousands):",min(jumboMortgages),",",max(jumboMortgages))

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
