#Student Name: Jianwei Su
#Date: 05/09/2022
#5.1.6

#Derived classes
#Import Loan from loan_base
from loan.loan_base import Loan

#Import all classes from asset
from asset.asset import *

import logging

#A fixed rate loan class which derives from Loan class
class FixedRateLoan(Loan):
      pass

#A variable rate loan class which derives from Loan class.
class VariableRateLoan(Loan):
    def __init__(self, notional, rateDict, term, asset):
        if isinstance(rateDict, dict):
            # Invoke the initialization function in the base class
            super(VariableRateLoan, self).__init__(notional, rateDict, term, asset)
        else:
            logging.error('Something is wrong with the parameter.')
            raise TypeError('Error: The input for rate is not a rate dictionary.')


    #getRate() function
    #We want to have a rate dictionary
    #The dict only contains start period for each rate
    #Override the base-class getRate() function
    def getRate(self, period):
        # add code to find the rate for a given period.
        # rateDict contains start period as key and rate as value,
        # for each rate.

        # Use rate to store the current rate
        # min(self.rate.keys()) means the smallest start period in the dict
        # Initialize it with initial rate
        logging.debug('Find the smallest start period in the dict.')
        logging.debug('min(self.rate.keys()) means the smallest start period in the dict')
        rate = self.rate[min(self.rate.keys())]

        # We want the start period to be sorted increasingly
        # self.rate.keys() are the start periods
        logging.debug('Sort the start period increasingly.')
        logging.debug('self.rate.keys() are the start periods')
        time_change = sorted(self.rate.keys())

        # If the input period is among those time periods in time_change, we will choose the closest smaller time period's rate as its rate
        # If the input period is less than the smallest time period in time_change, we will use the smallest time period's rate as its rate
        # If the input period is greater than the greatest time period in time_change, we will use the greatest time period's rate as its rate

        logging.debug('The rate will be chosen based on the sorted periods.')

        for time_period in time_change:

            if period >= time_period:
                rate = self.rate[time_period]

        logging.debug('It will just return the closest time period‘s rate.')
        # It will just return the closest time period's rate.
        return rate


#Create a fixed AutoLoan class.
#AutoLoan class is derived from FixedRateLoan class.
class AutoLoan(FixedRateLoan):

    def __init__(self, notional, rate, start_date, end_date, asset):

        # Make sure the asset parameter indeed contains a Car object
        # If it’s not a Car type, print an error message
        if isinstance(asset, CarMixin):
            # Overrides the base class
            # Invoke the initialization function in the base class
            super(AutoLoan, self).__init__(notional, rate, start_date, end_date, asset)
        else:
            logging.error('Something is wrong with the parameter.')
            raise TypeError('The input asset is not a CarMixin type.')