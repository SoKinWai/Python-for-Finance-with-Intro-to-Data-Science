#Student Name: Jianwei Su
#Date: 04/18/2022
#3.1.4

#I will need to use functools.partial for the below function
from functools import partial

import random

#Modified reconcileLists() function
#It will take a third parameter breakFn
#breakFn should represent a passed-in function or lambda
#The reconcileLists function will utilize the passed-in breakFn function to build the True/False list
def reconcileLists(list_a,list_b,breakFn):
    #It will return to a list of True or False values when these two lists have the same length
    if len(list_a)==len(list_b):

        return list(map(lambda list:breakFn(list[0],list[1]), zip(list_a,list_b)))


    #It will show an error message when these two lists have different lengths.
    else:
        return 'Error:These two lists do not have the same length.'




def main():
    # Code goes here
    print('\n==========Exercise 3.1.4==========\n')

    #Create a breakAbsolute stored lambda which takes two values and an epsilon parameter.
    #This lambda should ‘return’ True if the two values are not within epsilon of each other.
    #That means when the absolute value of two values' difference is greater than epsilon, it should return True.
    #Otherwise, it should return False.

    breakAbsolute= lambda value_a, value_b, epsilon: abs(value_a-value_b)>abs(epsilon)



    print('\n------Testing block 1-----')
    print('Test the breakAbsolute() function via using different numbers:')
    print('value_a=1,value_b=2 and epsilon=3:',breakAbsolute(1,2,3))
    print('value_a=3,value_b=2 and epsilon=3:', breakAbsolute(3, 2, 3))
    print('value_a=6,value_b=2 and epsilon=3:', breakAbsolute(6, 2, 3))
    print('value_a=-5,value_b=2 and epsilon=3:', breakAbsolute(-5, 2, 3))
    print('value_a=-5,value_b=0 and epsilon=l-3:', breakAbsolute(-5, 2, -3))

    #Create a breakRelative stored lambda which takes two values and a percent parameter.
    #This lambda should ‘return’ True if the percent difference between the two values exceeds percent
    #value_b can not be zero.
    breakRelative= lambda value_a, value_b,percent: value_b!=0 and (value_a/value_b-1)*100>percent

    print('\n------Testing block 2-----')
    print('Test the breakRelative() function via using different numbers:')
    print('value_a=3,value_b=1 and percent=50:',breakRelative(3,1,50))
    print('value_a=1,value_b=1 and percent=30:', breakRelative(1, 1, 30))
    print('value_a=4,value_b=-4 and percent=20:', breakRelative(4, -4, 20))
    print('value_a=4,value_b=0 and percent=60:', breakRelative(4, 0, 60))

    #Create a breakAbsRelative function which takes two values and a percent parameter.
    #This should return True if the percent difference between the absolute values of the two values exceeds percent
    breakAbsRelative=lambda value_a, value_b,percent: value_b!=0 and abs((abs(value_a)/abs(value_b)-1))*100>percent

    print('\n------Testing block 3-----')
    print('Test the breakAbsRelative() function via using different numbers:')
    print('value_a=3,value_b=1 and percent=50:', breakAbsRelative(3, 1, 50))
    print('value_a=1,value_b=1 and percent=30:', breakAbsRelative(1, 1, 30))
    print('value_a=-8,value_b=-4 and percent=20:', breakAbsRelative(-8, -4, 20))
    print('value_a=4,value_b=0 and percent=60:', breakAbsRelative(4, 0, 60))


    #Initialize large numbers' lists
    #I choose 100 random numbers from -1000 to 1000 of lists
    list_a=[random.randint(-1000, 1000) for iter in range(100)]
    list_b=[random.randint(-1000, 1000) for iter in range(100)]




    print('\n------Testing block 4-----')
    print('Test the reconcileLists() function via using breakAbsolute() function:')
    print('Set epsilon=100:',reconcileLists(list_a, list_b, partial(breakAbsolute, epsilon=100)))
    print('Set epsilon=-100:', reconcileLists(list_a, list_b, partial(breakAbsolute, epsilon=-100)))
    print('Set epsilon=1000:', reconcileLists(list_a, list_b, partial(breakAbsolute, epsilon=1000)))
    print('Set epsilon=10:', reconcileLists(list_a, list_b, partial(breakAbsolute, epsilon=10)))
    print('Set epsilon=-101:', reconcileLists(list_a, list_b, partial(breakAbsolute, epsilon=-101)))



    print('\n------Testing block 5-----')
    print('Test the reconcileLists() function via using breakRelative() function:')
    print('Set percent=50:', reconcileLists(list_a, list_b, partial(breakRelative, percent=50)))
    print('Set percent=30:', reconcileLists(list_a, list_b, partial(breakRelative, percent=30)))
    print('Set percent=20:', reconcileLists(list_a, list_b, partial(breakRelative, percent=20)))
    print('Set percent=60:', reconcileLists(list_a, list_b, partial(breakRelative, percent=60)))
    print('Set percent=100:', reconcileLists(list_a, list_b, partial(breakRelative, percent=100)))

    print('\n------Testing block 6-----')
    print('Test the reconcileLists() function via using breakAbsRelative() function:')
    print('Set percent=50:', reconcileLists(list_a, list_b, partial(breakAbsRelative, percent=50)))
    print('Set percent=30:', reconcileLists(list_a, list_b, partial(breakAbsRelative, percent=30)))
    print('Set percent=20:', reconcileLists(list_a, list_b, partial(breakAbsRelative, percent=20)))
    print('Set percent=60:', reconcileLists(list_a, list_b, partial(breakAbsRelative, percent=60)))
    print('Set percent=100:', reconcileLists(list_a, list_b, partial(breakAbsRelative, percent=100)))

    print('\n------Testing block 7-----')
    print('Test the reconcileLists() function via using breakAbsolute(), breakRelative() and breakAbsRelative() functions without "epsilon=" and "percent":')
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 9, 7, 11, 10]

    # Here -6 is a list which is [-6,-6,-6,-6,-6] as the first parameter of reconcileLists() function
    # l1 is the second parameter of reconcileLists() function
    # l2 is the list of epsilon
    a = reconcileLists(l1, l2, partial(breakAbsolute, -6))

    # Here 1 is a list which is [1,1,1,1,1] as the first parameter of reconcileLists() function
    # l1 is the second parameter of reconcileLists() function
    # l2 is the list of percent
    b = reconcileLists(l1,l2,partial(breakRelative,1))

    # Here 2 is a list which is [2,2,2,2,2] as the first parameter of reconcileLists() function
    # l1 is the second parameter of reconcileLists() function
    # l2 is the list of percent
    c = reconcileLists(l1,l2, partial(breakAbsRelative,2))

    print('partial(breakAbsolute, -6):',a)
    print('partial(breakRelative,1):',b)
    print('partial(breakAbsRelative,2):',c)


    print('\n***Program Complete***')


if __name__ == '__main__':
    main()