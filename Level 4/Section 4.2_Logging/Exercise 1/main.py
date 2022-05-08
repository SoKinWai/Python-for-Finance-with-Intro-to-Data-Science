#Student Name: Jianwei Su
#Date: 04/28/2022
#4.2.1


from utils.timer import Timer
import time

import logging


def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 4.2.1==========')
    logging.info('Modify your Timer class to use a logging statement (info level) instead of a print statement.\n')



    logging.info('------Testing block 1-----')
    logging.info('Testing the timer class without using "as"')
    with Timer('timerName'):
        # Set the time to be 10 seconds
        time.sleep(10)


    logging.info('\n------Testing block 2-----')
    logging.info('Testing the timer class with using "as"')
    with Timer('timerName') as t0:
        # Set the time to be 10 seconds
        time.sleep(10)


    logging.info('\n------Testing block 3-----')
    logging.info('Testing the timer class with using "as" and showing it in minutes')
    with Timer('timerName') as t1:
        t1.configureTimerDisplay('minutes')
        # Set the time to be 30 seconds
        time.sleep(30)


    logging.info('\n------Testing block 4-----')
    logging.info('Testing the timer class with using "as" and showing it in hours')
    with Timer('timerName') as t2:
        t2.configureTimerDisplay('hours')
        # Set the time to be 30 seconds
        time.sleep(30)


    logging.info('\n------Testing block 5-----')
    logging.info('Testing the timer class with using "as" and showing it in seconds')
    with Timer('timerName') as t3:
        t3.configureTimerDisplay('seconds')
        # Set the time to be 30 seconds
        time.sleep(30)


    logging.info('\n------Testing block 6-----')
    logging.info('Testing the timer class with using Exception Handling')
    try:
        with Timer('timerName') as t4:
            t4.configureTimerDisplay('dfxfdx')
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        logging.info(f'ValueError exception: {ex} \nPlease try again.')
    except Exception as ex:
        logging.info(f'Unknown error besides a ValueError: {ex} \nPlease try again.')


    logging.info('\n------Testing block 7-----')
    logging.info('Testing the timer class with using Exception Handling')
    try:
        with Timer('timerName') as t5:
            t5.configureTimerDisplay(5)
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        logging.info(f'ValueError exception: {ex} \nPlease try again.')
    except Exception as ex:
        logging.info(f'Unknown error besides a ValueError: {ex} \nPlease try again.')



    logging.info('\n------Testing block 8-----')
    logging.info('Testing the timer class with using Exception Handling')
    try:
        with Timer(KUBHUI) as t5:
            t5.configureTimerDisplay('seconds')
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        logging.info(f'ValueError exception: {ex} \nPlease try again.')
    except NameError as ex:
        logging.info(f'NameError exception: {ex} \nPlease try again.')
    except Exception as ex:
        logging.info(f'Unknown error besides a Value Error and Name Error: {ex} \nPlease try again.')












    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()