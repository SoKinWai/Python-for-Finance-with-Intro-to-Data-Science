#Student Name: Jianwei Su
#Date: 05/10/2022
#5.2.1


import logging
import time
from utils.timer import Timer
from utils.timer import timer


@timer  # decorating the function with the timer function
def intenseFunction(input):
    time.sleep(input)
    return 'Done'




def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.2.1==========')

    logging.info('\n------Testing block 1-----')
    logging.info('Testing the timer decorator function')

    #Set the time to be 30 seconds
    logging.info(f'{intenseFunction(30)}')


    logging.info('\n')

    logging.info('------Testing block 2-----')
    logging.info('Testing the timer class')
    with Timer('timerName'):
        # Set the time to be 30 seconds
        time.sleep(30)



    #How does this compare to the previous approach to using the context manager?
    # When is this more useful and when are context managers more useful

    # Decorators provide ‘syntactic sugar’ for wrapping a function or class inside another.
    # A context manager is a class that cleans up after itself.
    # The with statement enters the context. After the statement, the context exits and all is cleaned up.

    # Decorators are more useful to efficiently nest functions together.
    # Context Managers are more useful to clean up without explicitly telling the computer to do so.



    logging.info('\n***Program Complete***')


if __name__ == '__main__':
    main()