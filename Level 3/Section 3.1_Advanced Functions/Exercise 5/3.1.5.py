#Student Name: Jianwei Su
#Date: 04/18/2022
#3.1.5

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
        #method 1:
        return list(map(lambda list:breakFn(list[0],list[1]), zip(list_a,list_b)))


    #It will show an error message when these two lists have different lengths.
    else:
        return 'Error:These two lists do not have the same length.'

def main():
    # Code goes here
    print('\n==========Exercise 3.1.5==========\n')

    # Create a breakAbsolute stored lambda which takes two values and an epsilon parameter.
    # This lambda should ‘return’ True if the two values are not within epsilon of each other.
    # That means when the absolute value of two values' difference is greater than epsilon, it should return True.
    # Otherwise, it should return False.
    # Method 1:
    breakAbsolute = lambda value_a, value_b, epsilon: abs(value_a - value_b) > abs(epsilon)

    # Method 2
    # breakAbsolute = lambda value_a, value_b, epsilon: True if abs(value_a - value_b) > epsilon else False

    # Create a breakRelative stored lambda which takes two values and a percent parameter.
    # This lambda should ‘return’ True if the percent difference between the two values exceeds percent
    # value_b can not be zero.
    breakRelative = lambda value_a, value_b, percent: value_b != 0 and (value_a / value_b - 1) * 100 > percent

    # Create a breakAbsRelative function which takes two values and a percent parameter.
    # This should return True if the percent difference between the absolute values of the two values exceeds percent
    breakAbsRelative = lambda value_a, value_b, percent: value_b != 0 and abs((abs(value_a) / abs(value_b)) - 1 * 100) > percent

    # Initialize large numbers' lists
    # I choose 100 random numbers from -1000 to 1000 of lists
    list_a = [random.randint(-1000, 1000) for iter in range(100)]
    list_b = [random.randint(-1000, 1000) for iter in range(100)]




    print('\n------Testing block 1-----')
    print('Test the reconcileListsBreakAbsolute function:')
    # Ask the user to input a number of epsilon for reconcileListsBreakAbsolute function
    epsilon = float(input('Please enter the number of epsilon for reconcileListsBreakAbsolute function:'))

    # Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute function).
    reconcileListsBreakAbsolute = partial(reconcileLists, breakFn=partial(breakAbsolute, epsilon=epsilon))
    print('The result of reconcileListsBreakAbsolute is:',reconcileListsBreakAbsolute(list_a,list_b))

    print('\n------Testing block 2-----')
    print('Test the reconcileListsBreakRelative function:')
    # Ask the user to input a positive number of percent_a for reconcileListsBreakRelative function
    percent_a = float(input('Please enter a positive number of epsilon for reconcileListsBreakRelative function:'))

    # Create a partial called reconcileListsBreakRelative (which uses the breakRelative function).
    reconcileListsBreakRelative = partial(reconcileLists, breakFn=partial(breakRelative, percent=percent_a))
    print('The result of reconcileListsBreakRelative is:', reconcileListsBreakRelative(list_a, list_b))

    print('\n------Testing block 3-----')
    print('Test the reconcileListsbreakAbsRelative function:')
    # Ask the user to input a positive number of percent_b for reconcileListsbreakAbsRelative function
    percent_b = float(input('Please enter a positive number of epsilon for reconcileListsBreakRelative function:'))

    # Create a partial called reconcileListsbreakAbsRelative (which uses the breakAbsRelative function).
    reconcileListsbreakAbsRelative = partial(reconcileLists, breakFn=partial(breakAbsRelative, percent=percent_b))
    print('The result of reconcileListsbreakAbsRelative is:', reconcileListsbreakAbsRelative(list_a, list_b))









    print('\n***Program Complete***')


if __name__ == '__main__':
    main()