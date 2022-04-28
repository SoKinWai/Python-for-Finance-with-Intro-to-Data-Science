#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.2


import random

def main():
    # Code goes here
    print('\n==========Exercise 3.2.2==========\n')

    # Create a list of 1000 numbers.
    list_a = [random.random() for iter in range(1000)]

    #Convert the list to a reversed list
    list_b=list(reversed(list_a))

    #Check if the list is reversed
    print('Check the list if it is reversed:',list_a[0]==list_b[-1])

    # Check the length of the list_a
    print('The length of list_b is: ', len(list_b))

    # Convert the list to an iterable and iterate through it
    a = iter(list_b)

    # c is to check the nth of each number
    c = 1

    print('\nIterate through each number of iterable:')
    # It will cause an error if range is more than 1000
    for i in range(1000):
        print(c, ':', next(a))
        c = c + 1







    print('\n***Program Complete***')


if __name__ == '__main__':
    main()