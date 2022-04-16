#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.1

# Import necessary packages
# Import the Timer class from utils
from utils.timer import Timer
import time

def main():
    # f. Test your class thoroughly.

    print('------Exercise 2.1.1------')
    print('Testing the timer class\n')

    # Initialize t1 with Timer class and set the unit to be minutes
    print('------Testing block 1-----')
    print('Testing the timer class with unit to be minutes')
    print('Set time to sleep in 30 seconds and display in minutes:')
    t1 = Timer('minutes')
    # Print the timer unit
    print('t1 timer‘s unit will be:',t1.unit)
    # Set the timer to start
    t1.start()
    # Set time to sleep in 30 seconds
    time.sleep(30)
    # Set the timer to end
    t1.end()  # This should stop the timer and print the time taken

    # Initialize t2 with Timer class and set the unit to be hours
    print('\n------Testing block 2-----')
    print('Testing the timer class with unit to be hours')
    print('Set time to sleep in 30 seconds and display in hours:')
    t2 = Timer('hours')
    # Print the timer unit
    print('t2 timer‘s unit will be:', t2.unit)
    # Set the timer to start
    t2.start()
    # Set time to sleep in 30 seconds
    time.sleep(30)
    # Set the timer to end
    t2.end()  # This should stop the timer and print the time taken

    # Initialize t3 with Timer class and set the unit to be hours
    print('\n------Testing block 3-----')
    print('Testing the timer class with unit to be seconds')
    print('Set time to sleep in 30 seconds and display in seconds:')
    t3 = Timer('seconds')
    # Print the timer unit
    print('t3 timer‘s unit will be:', t3.unit)
    # Set the timer to start
    t3.start()
    # Set time to sleep in 30 seconds
    time.sleep(30)
    # Set the timer to end
    t3.end()  # This should stop the timer and print the time taken

    # Initialize t4 with Timer class and set the unit to be empty
    print('\n------Testing block 4-----')
    print('Testing the timer class with empty unit')
    print('Set time to sleep in 10 seconds and display in seconds:')
    t4 = Timer()
    # Print the timer unit
    # It will print seconds because it is set to be 'seconds' in timer class if the timer is empty
    print('t4 timer‘s unit will be:', t4.unit)
    # Set the timer to start
    t4.start()
    # Set time to sleep in 10 seconds
    time.sleep(10)
    # Set the timer to end
    t4.end()  # This should stop the timer and print the time taken

    # Testing the setter function from timer class
    print('\n------Testing block 5-----')
    print('Testing the setter function from timer class')
    print('Set time to sleep in 10 seconds and display in seconds:')
    #Set timer t1's unit to be 'seconds'
    t1.unit='seconds'
    # Print the timer unit
    # It will change to 'seconds'
    print('After set t1.unit=‘seconds’, t1 timer‘s unit will be:', t1.unit)
    # Set the timer to start
    t1.start()
    # Set time to sleep in 10 seconds
    time.sleep(10)
    # Set the timer to end
    t1.end()  # This should stop the timer and print the time taken

    # Testing the setter function from timer class
    print('\n------Testing block 6-----')
    print('Testing the setter function from timer class')
    print('Set time to sleep in 10 seconds and display in minutes:')
    # Set timer t2's unit to be 'minutes'
    t2.unit = 'minutes'
    # Print the timer unit
    # It will change to 'minutes'
    print('After set t2.unit=‘seconds’, t2 timer‘s unit will be:', t2.unit)
    # Set the timer to start
    t2.start()
    # Set time to sleep in 10 seconds
    time.sleep(10)
    # Set the timer to end
    t2.end()  # This should stop the timer and print the time taken

    # Testing the setter function from timer class
    print('\n------Testing block 7-----')
    print('Testing the setter function from timer class')
    print('Set time to sleep in 10 seconds and display in hours:')
    # Set timer t3's unit to be 'hours'
    t3.unit = 'hours'
    # Print the timer unit
    # It will change to 'hours'
    print('After set t3.unit=‘hours’, t3 timer‘s unit will be:', t3.unit)
    # Set the timer to start
    t3.start()
    # Set time to sleep in 10 seconds
    time.sleep(10)
    # Set the timer to end
    t3.end()  # This should stop the timer and print the time taken

    # Testing the retrieveLastResult() function from timer class
    print('\n------Testing block 8-----')
    print('Testing the retrieveLastResult() function from timer class')
    #I will try t1, t2 and t3 in retrieveLastResult() and see what retrieveLastResult() function will display on screen
    print('retrieveLastResult() function for t1:')
    t1.retrieveLastResult()
    print('retrieveLastResult() function for t2:')
    t2.retrieveLastResult()
    print('retrieveLastResult() function for t3:')
    t3.retrieveLastResult()

    # Testing the wrong input for the timer
    print('\n------Testing block 9-----')
    print('Testing the wrong input for the timer')
    print('Set time to sleep in 5 seconds:')
    t_wrong=Timer('kk')
    # Print the timer unit
    print('t_wrong timer‘s unit will be:', t_wrong.unit)
    # Set the timer to start
    t_wrong.start()
    # Set time to sleep in 5 seconds
    time.sleep(5)
    # Set the timer to end
    t_wrong.end()  # This should give an error
    #Try to retrieve the time taken from t_wrong
    t_wrong.retrieveLastResult() # This should give an error

    # Testing the start() function if the Timer is already started
    print('\n------Testing block 10-----')
    print('Testing the start() function if the Timer is already started')
    t_start=Timer('seconds')
    print('Set time to sleep in 5 seconds and display in seconds:')
    # Print the timer unit
    print('t1 timer‘s unit will be:', t_start.unit)
    # Set the timer to start
    t_start.start()
    #Set the timer to start again and see what will happen.
    #t_start.start() # This should give an error
    # Set time to sleep in 5 seconds
    time.sleep(5)
    # Set the timer to end
    t_start.end()  # This should stop the timer and print the time taken

    # Testing the end() function if the Timer is already ended
    print('\n------Testing block 11-----')
    print('Testing the end() function if the Timer is already ended')
    # Set the timer to end again
    t_start.end()  # This should give an error





    print('\n***Program Complete***')



#######################
if __name__ == '__main__':
    main()