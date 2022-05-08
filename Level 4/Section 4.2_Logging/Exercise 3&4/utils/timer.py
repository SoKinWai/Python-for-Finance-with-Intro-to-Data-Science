#Student Name: Jianwei Su
#Date: 04/29/2022
#4.2.3 & 4.2.4

#Import the time libary here.
from time import time

import logging


#Add a class-level warnThreshold variable, which defaults to 1 minute
#When printing the time taken, use a warn-level log statement instead of info-level if the
#time taken exceeds the warn threshold

class Timer(object):


    def __init__(self, name):
        self.name = name

        #Set self.config to be 'seconds' initially.
        self.config = 'seconds'

        #Set self.warnThreshold to be 60 seconds which is 1 minute
        self.warnThreshold=60

    divDict = {'hours': 3600, 'minutes': 60, 'seconds':1}

    def __enter__(self):

        logging.info('Timer is going to start.')
        # Start the timer by saving the current time
        self.timer_start = time()
        return self



    def __exit__(self, *args):
        if self.config == 'seconds' or self.config == 'minutes' or self.config == 'hours':
            logging.info('Timer is going to stop.')

            # End the timer by saving the current time
            self.timer_end = time()
            # Use end time minus the start time to get the time taken
            self.Time = self.timer_end - self.timer_start


            #When printing the time taken, use a warn-level log statement instead of info-level if the
            #time taken exceeds the warn threshold
            log_fuc = logging.warning if self.Time> self.warnThreshold else logging.info

            log_fuc(f'{self.name}: {self.Time/self.divDict[self.config]} {self.config}')


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