#Student Name: Jianwei Su
#Date: 05/11/2022
#5.2.2


import logging
import time
from utils.timer import Timer
from utils.timer import timer
from utils.memoize import memoize


@memoize
@timer
def Fibonacci_recursive_a(N):
    # Set up res to be a list here to store the first two integers from the Fibonacci list
    res = [0, 1]

    #Integers input from the user have to greater than 0
    if N <= 0:
        print("Please enter a positive integer")

    # Set up the first integer to be 0 in Fibonacci sequence list when the input from the user is 1
    elif N == 1:
        return([0])

    else:
    #range(2,N) means all integers from 2 to N-1
    #res.append(res[i - 1] + res[i - 2]) means to append the previous two numbers' addition to the res list as the Fibonacci list
     for i in range(2, N):
        res.append(res[i - 1] + res[i - 2])
     return (res)


@timer
def Fibonacci_recursive_b(N):
    # Set up res to be a list here to store the first two integers from the Fibonacci list
    res = [0, 1]

    #Integers input from the user have to greater than 0
    if N <= 0:
        print("Please enter a positive integer")

    # Set up the first integer to be 0 in Fibonacci sequence list when the input from the user is 1
    elif N == 1:
        return([0])

    else:
    #range(2,N) means all integers from 2 to N-1
    #res.append(res[i - 1] + res[i - 2]) means to append the previous two numbers' addition to the res list as the Fibonacci list
     for i in range(2, N):
        res.append(res[i - 1] + res[i - 2])
     return (res)



@memoize
@timer
def intenseFunction_a(input):
    time.sleep(input)
    return 'Done'

@timer
def intenseFunction_b(input):
    time.sleep(input)
    return 'Done'

def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.2.2=========')

    logging.info('\n------Testing block 1-----')
    logging.info('Testing the Fibonacci function in memoized way and normal way‘s time taken:')

    #Set the number to be 300000
    logging.info('Memoized way:')
    logging.info(f'{Fibonacci_recursive_a(300000)}')

    logging.info('\n')
    logging.info('Normal way:')
    logging.info(f'{Fibonacci_recursive_b(300000)}')

    #Memoized way took 2.0214686393737793 seconds and normal way took 4.415985584259033 seconds. That means memoized way is much faster for large number.

    logging.info('\n')
    logging.info('\n------Testing block 2-----')
    logging.info('Testing the intenseFunction function in memoized way and normal way‘s time taken:')

    logging.info('Memoized way:')
    logging.info(f'{intenseFunction_a(30)}')

    logging.info('\n')
    logging.info('Normal way:')
    logging.info(f'{intenseFunction_b(30)}')

    #The time will be the same because there is no way to memoize it.



    logging.info('\n***Program Complete***')



if __name__ == '__main__':
    main()