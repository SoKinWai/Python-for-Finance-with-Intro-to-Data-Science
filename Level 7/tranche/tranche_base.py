#Student Name: Jianwei Su
#Date: 05/18/2022
#7.1.1

import logging
import math

import numpy_financial as npf
import numpy as np
import operator
import math


#Create an abstract base class called Tranche
class Tranche(object):

    # It should be initialized with notional and rate.
    # Additionally, it should have a subordination flag.
    # This flag can either be letters of the alphabet or numbers.
    def __init__(self, notional, rate, subordination_flag):


        self.notional = notional
        self.rate = rate
        self.subordination_flag = subordination_flag


        self.interest_payments={0:0}
        self.principal_payments = {0:0}

    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument notional
    @property
    def notional(self):
        return self._notional


    @notional.setter
    def notional(self, inotional):
        if inotional > 0:
            self._notional = inotional  # Set the instance variable notional from input
        else:
            logging.error('Error: Face value has to be greater than 0.')


    # Decorator to create a property function to get the argument rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set the rate
    @rate.setter
    def rate(self, irate):
        if irate > 0:
            self._rate = irate  # Set the instance variable rate from input
        else:
            logging.error('Error: Please make sure the inputs of rate are greater than 0.')


    # Decorator to create a property function to define the attribute subordinationFlag
    @property
    def subordinationFlag(self):
        return self._subordinationFlag

    # Decorator to set subordinationFlag value
    @subordinationFlag.setter
    def subordinationFlag(self, isubordinationFlag):
        if type(isubordinationFlag)==int or type(isubordinationFlag)==float or type(isubordinationFlag)==str:
            self._subordinationFlag = isubordinationFlag  # Set instance variable subordinationFlag from input
        else:
            logging.error('Please enter a number or alphabet letter for subordination.')

    @property
    def principal_payments(self):
        return self._principal_payments


    @principal_payments.setter
    def principal_payments(self,iprincipal_payments):
        self._principal_payments=iprincipal_payments

    @property
    def interest_payments(self):
        return self._interest_payments

    @interest_payments.setter
    def interest_payments(self,iinterest_payments):
        self._interest_payments=iinterest_payments




    # monthlyRate() function
    # Monthly rate = Annual Rate / 12
    @staticmethod
    def monthlyRate(Annual_rate):
        return Annual_rate / 12


    # Implement three new methods in the Tranche base class: IRR, AL, and DIRR


    def IRR(self):

        list_a=list(self.principal_payments.values())
        list_b=list(self.interest_payments.values())


        cashflow_list = list(map(operator.add, list_a,list_b ))

        cashflow_list.insert(0,-self.notional)

        # Multiply the result by 12 to annualize

        result= npf.irr(cashflow_list)*12

        return result

    #Simply subtract the IRR from tranche’s rate
    def DIRR(self):

        return round(self.rate-self.IRR(),6)

    def AL(self):

        #Sum of the pricipal payments
        Total= sum(self.principal_payments.values())

        #Use enumerate() for the principal_payments values to do the calculation
        list_a=[a*b for (a,b) in enumerate(self.principal_payments.values())]

        #If the loan was not paid down (balance != 0), then AL is infinite – in this case, return None
        al= sum(list_a)/self.notional
        if math.isinf(al)==True:
            return None
        else:
            return al




    #Use the table from Appendix A to translate a DIRR value to a letter rating
    @staticmethod
    def convert_rating(dirr_input):
        dirr = dirr_input / 100


        ABS_Rating = {'Aaa': 0.06,
                   'Aa1': 0.67,
                   'Aa2': 1.3,
                   'Aa3': 2.7,
                   'A1': 5.2,
                   'A2': 8.9,
                   'A3': 13,
                   'Baa1': 19,
                   'Baa2': 27,
                   'Baa3': 46,
                   'Ba1': 72,
                   'Ba2': 106,
                   'Ba3': 143,
                   'B1': 183,
                   'B2': 231,
                   'B3': 311,
                   'Caa': 2500,
                   'Ca': 10000}


        try:

            # Find the smallest value at which value >= dirr
            closest_value=min([x for x in ABS_Rating.values() if x>=dirr])


            ratings = {a: b for b, a in ABS_Rating.items()}


            return ratings[closest_value]

        except Exception:
            return 'Ca'


    # Get DIRR in letter form
    def DIRR_Letter(self):

        dirr_Letter = self.convert_rating(self.DIRR())

        return dirr_Letter






