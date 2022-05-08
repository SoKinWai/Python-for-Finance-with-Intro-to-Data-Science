#Student Name: Jianwei Su
#Date: 04/27/2022
#4.1.5

#Import the time libary here.
from time import time

#Convert your Timer class’ print statement to use f-Strings instead of concatenating strings.

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
                print(f'{self.name} : {self.Time/60:,.2f} {self.config}')

            elif self.config == 'hours':
                print('The timer is displaying in hours:')
                print(f'{self.name} : {self.Time / 3600:,.5f} {self.config}')


            else:
                print('The timer is displaying in seconds:')
                print(f'{self.name} : {self.Time:,.2f} {self.config}')

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