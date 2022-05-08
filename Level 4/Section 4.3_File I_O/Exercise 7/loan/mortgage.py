#Student Name: Jianwei Su
#Date: 05/04/2022
#4.3.7

#Import Loan from loan_base
from loan.loan_base import Loan

#Derived classes
#Import FixedRateLoan, VariableRateLoan from loans
from loan.loans import FixedRateLoan, VariableRateLoan

#Import all classes from asset
from asset.asset import *


import logging


#class MortgageMixin

class MortgageMixin(object):

    def __init__(self, notional, rate, term, asset):

        if isinstance(asset, HouseBase):
            # Invoke the initialization function in the base class
            super(MortgageMixin, self).__init__(notional, rate, term, asset)
        else:
            logging.error('Something is wrong with the parameter.')
            raise TypeError('The input asset is not a HouseBase type.')




    # Implement a function called PMI that returns 0.0075% of the loan face value, but only if the LTV is < 80%.
    # Assume that the initial loan amount is for 100% of the asset value.

    # PMI() function
    # When LTV>=0.8, it returns to 0.0075% of the asset initial value
    # LTV= the loan amount /the asset is taken out initially value
    def PMI(self, period):
        # The balance of the loan at a given period (balance).
        # This method is to calculate remaining loan balance due at time period.
        if period >= 0 and period <= self.term:

            balance = super(MortgageMixin, self).balance(period)

            # Loan-to-Value ratio
            logging.debug('LTV equals balance divided by asset‘s initial value.')
            LTV = balance / self.asset.init_val
            if LTV >= 0.8:
                logging.debug('When LTV is greater or equal to 0.8, PMI equals to 0.000075 times face value.')
                return 0.000075 * self.notional
            else:
                # When LTV<0.8, it should return to 0
                logging.debug('When LTV is less than 0.8, PMI equals to 0.')
                return 0
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")


    # Override the base class monthlyPayment and principalDue functions to account for PMI

    # monthlyPayment() function.
    # Override the base class monthlyPayment function to account for PMI and use super to avoid duplicating the formula
    # It's the regular monthly payment plus PMI.
    def monthlyPayment(self, period):
        if period >= 0 and period <= self.term:
            logging.debug('Monthly payment is being calculated...')
            logging.debug('It equals to PMI plus the regular monthly payment.')
            return super(MortgageMixin, self).monthlyPayment(period) + self.PMI(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")


    # principalDue() function.The principal amount due at a given period (principalDue).
    # Override the base class principalDue function to account for PMI and use super to avoid duplicating the formula
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue(self, period):
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:
            logging.debug('Principal due payment is being calculated...')
            logging.debug('principalDue = monthlyPayment - interestDue')

            return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    def principalDue_re_ori(self, period):
        # I will use this formula to calculate the principal due:
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:

            return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue_re_ori(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    # A recursive version
    # principalDue_recur() function. The principal amount due at a given period (principalDue_recur).
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue_recur(self, period):
        logging.warning('This is a recursive function, so it will take a long time to run.')
        return self.principalDue_re_ori(period)



# Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate base class(es).

# Derived class from MortgageMixin and FixedRateLoan
# It gets everything from MortgageMixin and FixedRateLoan
class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

# Derived class from MortgageMixin and VariableRateLoan
# It gets everything from MortgageMixin and VariableRateLoan
class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass
