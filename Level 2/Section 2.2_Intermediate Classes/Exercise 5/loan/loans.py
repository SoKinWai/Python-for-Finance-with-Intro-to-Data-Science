#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.5

#Derived classes
#Import Loan from loan_base
from loan.loan_base import Loan

#A fixed rate loan class which derives from Loan class
class FixedRateLoan(Loan):
    # This is the FixedRateLoan class
    pass

#A variable rate loan class which derives from Loan class.
class VariableRateLoan(Loan):
    def __init__(self, notional, rateDict, term, asset):
        if isinstance(rateDict, dict):
            # Invoke the initialization function in the base class
            super(VariableRateLoan, self).__init__(notional, rateDict, term, asset)
        else:
            print('Error: The input for rate is not a rate dictionary.')


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
        rate = self.rate[min(self.rate.keys())]

        # We want the start period to be sorted increasingly
        # self.rate.keys() are the start periods
        time_change = sorted(self.rate.keys())

        # If the input period is among those time periods in time_change, we will choose the closest smaller time period's rate as its rate
        # If the input period is less than the smallest time period in time_change, we will use the smallest time period's rate as its rate
        # If the input period is greater than the greatest time period in time_change, we will use the greatest time period's rate as its rate

        for time_period in time_change:

            if period >= time_period:
                rate = self.rate[time_period]
        # It will just return the cloest time period's rate.
        return rate


#Create a fixed AutoLoan class.
#AutoLoan class is derived from FixedRateLoan class.
class AutoLoan(FixedRateLoan):

    def __init__(self, notional, rate, term, asset):

        #Overrides the base class
        # Invoke the initialization function in the base class
        super(AutoLoan, self).__init__(notional, rate, term, asset)
