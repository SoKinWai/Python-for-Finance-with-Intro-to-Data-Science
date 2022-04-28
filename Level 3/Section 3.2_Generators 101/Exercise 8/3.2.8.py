#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.8

from itertools import *

def main():
    # Code goes here
    print('\n==========Exercise 3.2.8==========')

    #Create three generator expressions with different lengths
    A=[i for i in range(5)]
    B=[x**2 for x in range(5)]
    C=[a**3 for a in range((5))]

    print('\n------Testing block 1-----')
    print('Display three generator expressions:')
    print('Generator A:', A)
    print('Generator B:', B)
    print('Generator C:', C)


    #Get all the combinations of the values and convert it to a list


    Values_com_a=list(product(A,B,C))


    print('\n------Testing block 2-----')
    print('Get all the combinations of the values:')

    # Print out the result as a list
    print(Values_com_a)

    print('\n------Testing block 3-----')
    print('Alternative way about combinations:')
    Values_chain = list(chain(A, B, C))
    print('The list of the chain of A,B and C:',Values_chain)
    Values_com_b = list(combinations(Values_chain,3))
    print('Alternative combinations:',Values_com_b)

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()