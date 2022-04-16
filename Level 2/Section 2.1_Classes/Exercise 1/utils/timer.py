#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.1


#Import the time libary here.
from time import time


#a. Create a class called Timer.
class Timer(object):

    # To check if the timer has started
    # Initial value is False: timer has not started
    _timerStarted = False


    # Initialize function with unit
    # Also included in this function to set the argument to be 'seconds' if it doesn't exists
    def __init__(self, unit=None):
        self._unit=str(unit) if unit is not None \
            else str(Timer._dunit) if hasattr(Timer, '_dunit') else 'seconds'

    # DefaultTimer function to set default time
    @classmethod
    # Set at the class level the value of unit as default if it is not speicified
    # Instead of storing dunit at the object level, store it at the class level
    def defaultTimer(cls, unit):
    # Get value of the class variable from the instance object
        cls._dunit = unit

    # Decorators to define and the set value for the instance variable
    # Decorator to create a property function to define the argument unit
    @property
    def unit(self):
        return self._unit

    # Decorator to set unit
    @unit.setter
    def unit(self, iunit):
        self._unit = iunit # Set the instance variable unit from input


    #b. Add a start method and end method.
    #c. Note that start should give an error if the Timer is already started and end should give an error if the Timer is not currently running.

    #start() function to start the timer
    #It will give an error if the timer has already started
    def start(self):
        #False means timer has not started
        if self._timerStarted==False:
            print('Timer is going to start.')
            # Start the timer by saving the current time
            self.timer_start = time()
            # Set the _timerStarted flag to True
            # True means timer is running
            self._timerStarted = True
        else:
            #It gives an error if the timer is already started
            print('Error: The timer has already started.')

    # end() function to end the timer
    # It will give an error if the timer has already ended
    def end(self):
        #True means timer has not started
        if self._timerStarted== True:
            print('Timer is going to stop.')

            # End the timer by saving the current time
            self.timer_end = time()
            # Use end time minus the start time to get the time taken
            self.Time = self.timer_end - self.timer_start

            # e. Add the ability to configure the Timer to display either seconds, minutes, or hours.
            # Set the timer to display configuration
            self.time_config =self.unit
            # Use the calculations to get the time displays in either seconds, minutes, or hours.
            if self.time_config == 'minutes':
                print('The timer is displaying in minutes:')
                print('This process took ' + str(self.Time / 60) + ' minutes.')
            elif self.time_config == 'hours':
                print('The timer is displaying in hours:')
                print('This process took ' + str(self.Time / 3600) + ' hours.')
            elif self.time_config =='seconds':
                print('The timer is displaying in seconds:')
                print('This process took ' + str(self.Time) + ' seconds.')
            else:
                print('Error: please make sure you entered either seconds, minutes, or hours you want to display .')

            # Set the _timerStarted flag to False
            # False means timer has ended
            self._timerStarted = False
        else:
            # It gives an error if the timer is already ended
            print('Error:the timer has not started.')

    #    d. Add a method to retrieve the last timer result.
    # retrieveLastResult() function
    # It will retrieve the last timer result and print it on screen either in seconds, minutes, or hours.
    def retrieveLastResult(self):
        self.last_result = self.Time

        # e. Add the ability to configure the Timer to display either seconds, minutes, or hours.
        # Set the timer to display configuration
        self.time_config = self.unit
        # Use the calculations to get the time displays in either seconds, minutes, or hours.
        if self.time_config == 'minutes':
            print('The timer is displaying in minutes:')
            print('The last timer took ' + str(self.last_result / 60) + ' minutes.')
        elif self.time_config == 'hours':
            print('The timer is displaying in hours:')
            print('The last timer took ' + str(self.last_result/ 3600) + ' hours.')
        elif self.time_config == 'seconds':
            print('The timer is displaying in seconds:')
            print('The last timer took ' + str(self.last_result) + ' seconds.')
        else:
            print('retrieveLastResult() error: please make sure you entered either seconds, minutes, or hours you want to display .')