#Student Name: Jianwei Su
#Date: 04/27/2022
#4.1.5


from utils.timer import Timer
import time

def main():
    # Code goes here
    print('\n==========Exercise 4.1.5==========')
    print('Convert your Timer class’ print statement to use f-Strings instead of concatenating strings.\n')

    print('------Testing block 1-----')
    print('Testing the timer class without using "as"')
    with Timer('timerName'):
        # Set the time to be 10 seconds
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
        print(f'ValueError exception: {ex} \nPlease try again.')
    except Exception as ex:
        print(f'Unknown error besides a ValueError: {ex} \nPlease try again.')


    print('\n------Testing block 7-----')
    print('Testing the timer class with using Exception Handling')
    try:
        with Timer('timerName') as t5:
            t5.configureTimerDisplay(5)
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        print(f'ValueError exception: {ex} \nPlease try again.')
    except Exception as ex:
        print(f'Unknown error besides a ValueError: {ex} \nPlease try again.')


    print('\n------Testing block 8-----')
    print('Testing the timer class with using Exception Handling')
    try:
        with Timer(KUBHUI) as t5:
            t5.configureTimerDisplay('seconds')
            # Set the time to be 30 seconds
            time.sleep(30)
    except ValueError as ex:
        print(f'ValueError exception: {ex} \nPlease try again.')
    except NameError as ex:
        print(f'NameError exception: {ex} \nPlease try again.')
    except Exception as ex:
        print(f'Unknown error besides a ValueError: {ex} \nPlease try again.')


    print('\n***Program Complete***')

if __name__ == '__main__':
    main()