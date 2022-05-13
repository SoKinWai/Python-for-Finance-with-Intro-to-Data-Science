#Student Name: Jianwei Su
#Date: 05/11/2022
#5.2.3


#Import Asset class from asset
from asset.asset import Asset

import logging

# Loan class
# This class' object takes on the arguments notional, rate, start_date, end_date and asset
# Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
# Loan class
# This class' object takes on the arguments notional, rate, start_date, end_date
# Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
class Loan(object):

    # Initialize function with notional, rate, start_date, end_date and asset

    def __init__(self, notional, rate, start_date, end_date, asset):

        self.notional = notional

        self.rate = rate

        self.start_date = start_date

        self.end_date = end_date


        # Save an asset parameter down into an object-level attribute.
        # Make sure the asset parameter indeed contains an Asset object
        # If it’s not an Asset type, raise an error message
        if isinstance(asset, Asset):
            self.asset = asset
        else:
            logging.error('Something is wrong with the parameter.')
            raise TypeError('The input asset is not an Asset type.')

    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set the notional
    @notional.setter
    def notional(self, inotional):
        if inotional > 0:
            self._notional = inotional  # Set the instance variable notional from input
        else:
            logging.error('Something is wrong with the parameter.')
            raise ValueError("Error: Face value has to be greater than 0.")


    # Decorator to create a property function to get the argument rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set the rate
    @rate.setter
    def rate(self, irate):
        if type(irate) != dict and irate > 0:
            self._rate = irate  # Set the instance variable rate from input
        elif type(irate) == dict and min(irate.values()) > 0:
            self._rate = irate  # Set the instance variable rate from input
        else:
            logging.error('Something is wrong with the parameter.')
            raise ValueError("Error: Please make sure the inputs of rate are greater than 0.")

    # Decorator to create a property function to get the argument start_date
    @property
    def start_date(self):
        return self._start_date

    # Decorator to set the start_date
    @start_date.setter
    def start_date(self, istart_date):
        self._start_date = istart_date  # Set the instance variable start_date from input

    # Decorator to create a property function to get the argument end_date
    @property
    def end_date(self):
        return self._end_date

    # Decorator to set the end_date
    @end_date.setter
    def end_date(self, iend_date):
        self._end_date = iend_date  # Set the instance variable end_date from input


    # Decorator to create a property function to get the argument asset

    @property
    def asset(self):
        return self._asset

    # Decorator to set the asset
    @asset.setter
    def asset(self, iasset):
        self._asset = iasset  # Set the instance variable asset from input


    def term(self):
        date_delta=abs(self.end_date-self.start_date)

        total_months = round(abs(date_delta.total_seconds() / 2592000))

        if total_months > 0 and type(total_months) == int:
            return total_months
        elif type(total_months)!=int:
            logging.error('Something is wrong with the parameter.')
            raise TypeError("Error: Please make sure the term is an integer.")
        else:
            logging.error('Something is wrong with the parameter.')
            raise ValueError("Error: Please make sure the term is an integer and greater than 0")



    # Total payments over the entire loan
    # totalPayments() function.
    def totalPayments(self, period=None):

        logging.debug('Total payment is being calculated...')
        logging.debug('Sum up each month‘s payments to get the total payment')
        # Sum up each month's payments to get the total payment
        return sum([self.monthlyPayment(p) for p in range(1, self.term() + 1)])

    # Total interest over the entire loan
    # totalInterest() function. This will be total payments minus notional face values.
    def totalInterest(self, period=None):

        logging.debug('Total interest is being calculated...')
        logging.debug('Total interest= Total payments- Notional face value')
        # Total interest= Total payments- Notional face value
        return self.totalPayments() - self.notional

    # A version that uses the formulas provided in the slides.
    # interestDue() function. The interest amount due at a given period (interestDue).
    # This method is to calculate interest due at time period.
    def interestDue(self, period):
        # I will use this formula to calculate the interest due:
        # Interest Due= Monthly Rate * previous time period balance
        if period > 0 and period <= self.term():

            logging.debug('Interest due is being calculated...')
            logging.debug('Interest Due= Monthly Rate * previous time period balance')
            return (Loan.monthlyRate(self.getRate(period))) * self.balance(period - 1)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than 0.")

    # A version that uses the formulas provided in the slides.
    # principalDue() function. The principal amount due at a given period (principalDue).
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue(self, period):
        # I will use this formula to calculate the principal due:
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term():

            logging.debug('Principal due is being calculated...')
            logging.debug('Principal Due = monthlyPayment - interestDue')
            return self.monthlyPayment(period) - self.interestDue(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than 0.")

    def principalDue_re_ori(self, period):
        # I will use this formula to calculate the principal due:
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term():

            return self.monthlyPayment(period) - self.interestDue_re_ori(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0 or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than 0.")


    # A recursive version
    # principalDue_recur() function. The principal amount due at a given period (principalDue_recur).
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue_recur(self, period):
        logging.warning('This is a recursive function, so it will take a long time to run.')
        return self.principalDue_re_ori(period)



    def interestDue_re_ori(self, period):
        # I will use this formula to calculate the interest due:
        # Interest Due= Monthly Rate * previous time period balance
        if period > 0 and period <= self.term():

            return self.balance_re_ori(period - 1) * Loan.monthlyRate(self.getRate((period)))
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than or equal 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than 0.")


    # A recursive version
    # interestDue_recur() function. The interest amount due at a given period (interestDue_recur).
    # This method is to calculate interest due at time period.
    def interestDue_recur(self, period):
        logging.warning('This is a recursive function, so it will take a long time to run.')
        return self.interestDue_re_ori(period)


    def balance_re_ori(self, period):
        # I will use this formula to calculate the balance:
        # balance at current period= previous balance-current principal due
        if period >= 0 and period <= self.term():
            if period == 0:

                return self.notional
            else:

                return self.balance_re_ori(period - 1) - self.principalDue_re_ori(period)

        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    # A recursive version
    # balance_recur() function. The balance of the loan at a given period (balance_recur).
    # This method is to calculate remaining loan balance due at time period.
    def balance_recur(self, period):
        logging.warning('This is a recursive function, so it will take a long time to run.')
        return self.balance_re_ori(period)


    # Implement a class-level method called calcMonthlyPmt, in the Loan base class.
    # This should calculate a monthly payment based on three parameters: face, rate, and term.

    # This is the class method to calculate the monthly payment of the given loan
    # calcMonthlyPmt() function
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        # I will use this formula to calculate the balance:
        # pmt  = (r*P)/(1-1+r)**-N, pmt is monthly payment amount
        # r is monthly interest rate, P is principal which is face value and N is term
        # of loan(in months)

        logging.debug('Monthly payment in class method is being calculated...')

        return (face * (Loan.monthlyRate(rate))) / (1 - (1 + Loan.monthlyRate(rate)) ** (-term))

    # Create a class -level function, in the Loan base class, which calculates the balance (calcBalance).
    # Input parameters should be face, rate, term, period.

    # This is the class method to calculate outstanding balance of the given loan at given period
    # calcBalance() function.
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        # I will use this formula to calculate the balance:
        # balance = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r is monthly interest rate, P is principal which is face value and N is term
        # of loan(in months)
        # n is number of payments made, but we could think of it as the time period here.
        if period >= 0 and period <= term:
            logging.debug('Balance in class method is being calculated...')

            return face * ((1 + Loan.monthlyRate(rate)) ** period) - cls.calcMonthlyPmt(face, rate, term) * (
                        ((1 + Loan.monthlyRate(rate)) ** period) - 1) / (Loan.monthlyRate(rate))
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    # Modify the object-level methods for monthlyPayment to delegate to the class-level methods.

    # The monthly payment amount of the loan (monthlyPayment)
    # Define the function with a dummy ‘period’ parameter because
    # it’s possible some loan types will have a monthly payment dependent on the period.
    # monthlyPayment() function to calculate monthly payments
    def monthlyPayment(self, period=None):  # period is the dummy variable

        logging.debug('Monthly payment is being calculated...')
        logging.debug('Call the calcMonthlyPmt() to calculate monthly payment.')
        # Notional is equivalent to face
        return self.calcMonthlyPmt(self.notional, self.getRate(period), self.term())

    # Modify the object-level methods for balance to delegate to the class-level methods.

    # balance() function. The balance of the loan at a given period (balance).
    # This method is to calculate remaining loan balance due at time period.
    def balance(self, period):
        logging.debug('Call the calcBalance() to calculate balance.')

        # Notional is equivalent to face
        return self.calcBalance(self.notional, self.getRate(period), self.term(), period)

    # Create a static - level method in Loan called monthlyRate.This should return the monthly
    # interest rate for a passed-in annual rate.

    # monthlyRate() function
    # Monthly rate = Annual Rate / 12
    @staticmethod
    def monthlyRate(Annual_rate):


        return Annual_rate / 12

    # Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate).

    # Annual_rate() function
    # Annual rate=Monthly rate*12
    @staticmethod
    def Annual_rate(monthlyRate):

        return monthlyRate * 12

    # getRate() function
    def getRate(self, period=None):

        # should be overriden by derived class, this function makes Loan class abstract

        return self.rate

    # recoveryValue() function
    # Return to the current asset value for the given period times 0.6

    def recoveryValue(self, period):
        logging.debug('Recovery value is being calculated...')

        return self.asset.current_value(period) * 0.6


    # equity() function
    # Return to the asset value less the loan balance

    def equity(self, period):
        if period >= 0 and period <= self.term():
            logging.debug('Equity is being calculated...')
            logging.debug('Asset‘s current value minus balance')
            return self.asset.current_value(period) - self.balance(period)
        else:
            logging.error('Something is wrong with the parameter.')
            logging.info('Period should be greater than term or less than 0.')
            raise ValueError("Error: Period has to be within the term of the loan and greater than or equal to 0.")