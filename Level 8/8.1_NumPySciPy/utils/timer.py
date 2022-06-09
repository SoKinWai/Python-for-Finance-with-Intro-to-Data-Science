#Student Name: Jianwei Su
#Date: 04/22/2022
#3.4.2

#Import the time libary here.
from time import time

#Modify the Timer class to work as a context manager.
class Timer(object):



    def __init__(self, name):
        self.name = name

        #Set self.config to be 'seconds' initially.
        self.config = 'seconds'

    def __enter__(self):

        print('Timer is going to start.')
        # Start the timer by saving the current time
        self.timer_start = time()
        return self



    def __exit__(self, *args):
        if self.config == 'seconds' or self.config == 'minutes' or self.config == 'hours':
            print('Timer is going to stop.')

            # End the timer by saving the current time
            self.timer_end = time()
            # Use end time minus the start time to get the time taken
            self.Time = self.timer_end - self.timer_start

            if self.config == 'minutes':
                print('The timer is displaying in minutes:')
                print(self.name, ':', str(self.Time/60), self.config)

            elif self.config == 'hours':
                print('The timer is displaying in hours:')
                print(self.name, ':', str(self.Time/3600), self.config)

            else:
                print('The timer is displaying in seconds:')
                print(self.name, ':', str(self.Time), self.config)
        else:
            raise ValueError('Please make sure you entered either seconds, minutes, or hours you want to display.')


    # defaultName function to set default name
    @classmethod
    # Set at the class level the value of name as default if it is not speicified
    # Instead of storing dunit at the object level, store it at the class level
    def defaultName(cls, name):
    # Get value of the class variable from the instance object
        cls._dname = name

    # Decorators to define and the set value for the instance variable
    # Decorator to create a property function to define the argument name
    @property
    def name(self):
        return self._name

    # Decorator to set name
    @name.setter
    def name(self, iname):
        self._name = iname  # Set the instance variable name from input


    def configureTimerDisplay(self,units):

        self.config = units





