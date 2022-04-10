#Student name: Jianwei Su
#Date: 04/06/2022
#1.4.1


import random

#a
#Mortgage_amounts() function
#It returns 100 random numbers from 100 to 1000
def Mortgage_amounts():
    return [random.randint(100, 1000) for iter in range(100)]



def main():
    # Code goes here
    print('\n==========Exercise 1.4.1===========')

    #mortgage_amounts has 100 mortgage amounts,range from 100 to 1000
    #Print mortgage_amounts on screen
    mortgage_amounts=Mortgage_amounts()
    print("A function that returns an unsorted list of mortgage amounts,in thousands, range from 100 to 1000:",mortgage_amounts,'\n')

    #b
    #Filter amounts below 200 from mortgage_amounts and store them in miniMortgages
    #Print miniMortgages on screen
    miniMortgages= [i for i in mortgage_amounts if i<200]

    #Test for empty list
    #miniMortgages=[]

    print("Mini Mortgages(Amounts below 200):",miniMortgages,'\n')

    #Filter amounts between 200 and 467 and store them in standardMortgages
    #Print standardMortgages on screen
    standardMortgages=[a for a in mortgage_amounts if 200<=a<=467]
    print("Standard Mortgages(amounts between 200 and 467):",standardMortgages,'\n')

    #Filter amounts greater than 467 and store them in jumboMortgages
    # Print jumboMortgages on screen
    jumboMortgages=[b for b in mortgage_amounts if b>467]
    print("Jumbo Mortgages(amounts greater than 467):",jumboMortgages,'\n')

    #c
    #Use the all function with an if statement to verify that the resulting list miniMortgages
    # indeed contain only numbers within the specified ranges

    #Test for empty list
    # if (all(i<200 for i in miniMortgages)):

    if (all(i<200 for i in miniMortgages)) and miniMortgages!=[]:
     print("True for Mini Mortgages by using all function\n")
    else: print("False for Mini Mortgages by using all function\n")

    # Use the all function with an if statement to verify that the resulting list standardMortgages
    # indeed contain only numbers within the specified ranges
    if (all(200<=a<=467 for a in standardMortgages)) and standardMortgages!=[]:
     print("True for Standard Mortgages  by using all function\n")
    else: print("False for Standard Mortgages  by using all function\n")

    # Use the all function with an if statement to verify that the resulting list jumboMortgages
    # indeed contain only numbers within the specified ranges
    if (all(b>467 for b in jumboMortgages)) and jumboMortgages!=[]:
     print("True for Jumbo Mortgages by using all function\n")
    else: print("False for Jumbo Mortgages by using all function\n")


    #d
    # Use the any function with an if statement to verify that the resulting list miniMortgages
    # indeed contain only numbers within the specified ranges
    if any(i>=200 for i in miniMortgages):
     print("False for Mini Mortgages by using any function\n")
    else:print("True for Mini Mortgages by using any function\n")

    # Use the any function with an if statement to verify that the resulting list standardMortgages
    # indeed contain only numbers within the specified ranges
    if any(a<200 or a>467 for a in standardMortgages):
     print("False for Standard Mortgages by using any function\n")
    else:print("True for Standard Mortgages by using any function\n")

    # Use the any function with an if statement to verify that the resulting list jumboMortgages
    # indeed contain only numbers within the specified ranges

    #Test for the any condition
    #jumboMortgages.append(200)

    if any(b<=467 for b in jumboMortgages):
     print("False for Jumbo Mortgages by using any funcion\n")
    else:print("True for Jumbo Mortgages by using any funcion\n")

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()


