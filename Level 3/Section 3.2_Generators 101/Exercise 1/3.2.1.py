#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.1

import random

def main():
    # Code goes here
    print('\n==========Exercise 3.2.1==========\n')


    #Create a list of 1000 numbers.
    list_a = [random.random() for iter in range(1000)]

    #Check the length of the list_a
    print('The length of list_a is: ',len(list_a))

    #Convert the list to an iterable and iterate through it
    a=iter(list_a)

    #c is to check the nth of each number
    c=1

    print('\nIterate through each number of iterable:')
    #It will cause an error if range is more than 1000
    for i in range(1000):
        print(c,':',next(a))
        c=c+1



    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
