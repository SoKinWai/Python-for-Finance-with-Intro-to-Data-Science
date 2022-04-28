#Student Name: Jianwei Su
#Date: 04/22/2022
#3.4.2


from utils.timer import Timer
import time

def main():
    # Code goes here
    print('\n==========Exercise 3.4.2==========')
    print('Modify the Timer class to work as a context manager.\n')

    print('------Testing block 1-----')
    print('Testing the timer class without using "as"')
    with Timer('timerName'):
        #Set the time to be 10 seconds
        time.sleep(10)

    print('\n------Testing block 2-----')
    print('Testing the timer class with using "as"')
    with Timer('timerName') as t0:
        # Set the time to be 10 seconds
        time.sleep(10)

    print('\n------Testing block 3-----')
    print('Testing the timer class with using "as" and showing it in minutes')
    with Timer('timerName') as t1:
        t1.configureTimerDisplay('minutes')
        # Set the time to be 30 seconds
        time.sleep(30)

    print('\n------Testing block 4-----')
    print('Testing the timer class with using "as" and showing it in hours')
    with Timer('timerName') as t2:
        t2.configureTimerDisplay('hours')
        # Set the time to be 30 seconds
        time.sleep(30)

    print('\n------Testing block 5-----')
    print('Testing the timer class with using "as" and showing it in seconds')
    with Timer('timerName') as t3:
        t3.configureTimerDisplay('seconds')
        # Set the time to be 30 seconds
        time.sleep(30)

    print('\n------Testing block 6-----')
    print('Testing the timer class with using Exception Handling')
    try:
        with Timer('timerName') as t4:
            t4.configureTimerDisplay('dfxfdx')
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
    except Exception as ex:
        print('Unknown error besides a ValueError:', ex, '\nPlease try again.')

    print('\n------Testing block 7-----')
    print('Testing the timer class with using Exception Handling')
    try:
        with Timer('timerName') as t5:
            t5.configureTimerDisplay(5)
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
    except Exception as ex:
        print('Unknown error besides a ValueError:', ex, '\nPlease try again.')



    print('\n------Testing block 8-----')
    print('Testing the timer class with using Exception Handling')
    try:
        with Timer(KUBHUI) as t5:
            t5.configureTimerDisplay('seconds')
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')
    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')
    except Exception as ex:
        print('Unknown error besides a ValueError:', ex, '\nPlease try again.')

    # How does this compare to the previous approach of using the regular Timer class?
    # This method requires less codes, so it will look much cleaner than the previous method.
    # It is an easier way for me to understand because it does not need a lot of codes.
    # Also, because I used exception handing method, it will run faster than previous method.

















    print('\n***Program Complete***')

if __name__ == '__main__':
    main()