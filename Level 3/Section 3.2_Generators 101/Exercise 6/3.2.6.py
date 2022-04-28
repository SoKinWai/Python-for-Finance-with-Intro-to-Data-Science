#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.6

from itertools import chain

def main():
    # Code goes here
    print('\n==========Exercise 3.2.6==========')

    #Create three generator expressions.
    A=[i for i in range(10)]
    B=[x**2 for x in range(3)]
    C=[a**3 for a in range((5))]



    #Use itertools.chain to attach them together.
    Together=chain(A,B,C)

    print('\n------Testing block 1-----')
    print('Display three generator expressions:')
    print('Generator A:',A)
    print('Generator B:',B)
    print('Generator C:',C)

    print('\n------Testing block 2-----')
    print('Display the list after chain A,B and C together:')
    #Print out the result as a list.
    print('The list after chain A,B and C:',list(Together))



    print('\n***Program Complete***')

if __name__ == '__main__':
    main()