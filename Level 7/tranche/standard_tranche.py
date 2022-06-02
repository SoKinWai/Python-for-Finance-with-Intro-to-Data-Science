#Student Name: Jianwei Su
#Date: 05/20/2022
#7.1.2

from tranche.tranche_base import Tranche
import logging


#Derive a class called StandardTranche
class StandardTranche(Tranche):

    def __init__(self,notional, rate,subordination_flag):
        # Invoke the initialization function in the base class
        super(StandardTranche, self).__init__(notional, rate, subordination_flag)

        self.period=0

        self.interest_shortfall={0:0}

        self.interest_Due={0:0}

        self.principalShortFall = {0: 0}

        self.interest_paid = False

        self.principal_paid = False



    @property
    def period(self):
        return self._period

    @period.setter
    def period(self,iperiod):
        self._period=iperiod



    @property
    def interest_shortfall(self):
        return self._interest_shortfall

    @interest_shortfall.setter
    def interest_shortfall(self,iinterest_shortfall):
        self._interest_shortfall=iinterest_shortfall


    @property
    def interest_Due(self):
        return self._interest_Due

    @interest_Due.setter
    def interest_Due(self,iinterest_Due):
        self._interest_Due=iinterest_Due

    @property
    def principalShortFall(self):
        return self._principalShortFall

    @principalShortFall.setter
    def principalShortFall(self,iprincipalShortFall):
        self._principalShortFall=iprincipalShortFall

    # Decorator to create a property function to define the attribute interest_paid
    @property
    def interest_paid(self):
        return self._interest_paid

    # Decorator to set interest_paid value
    @interest_paid.setter
    def interest_paid(self, iinterest_paid):
        self._interest_paid = iinterest_paid # Set instance variable interest_paid from input

    # Decorator to create a property function to define the attribute principal_paid
    @property
    def principal_paid(self):
        return self._principal_paid

    # Decorator to set principal_paid value
    @principal_paid.setter
    def principal_paid(self, iprincipal_paid):
        self._principal_paid = iprincipal_paid  # Set instance variable principal_paid from input



    def increaseTimePeriod(self):
        #This should increase the current time period of
        # the object by 1 (starts from 0).
        self.interest_paid = False
        self.principal_paid = False
        self.period+=1

        return self.period






    #This should return the amount of notional still owed to the tranche for the current time period (after any payments made)
    #You can calculate this based on the original notional, the sum of all the principal payments already made, and any
    #interest shortfalls.
    def notionalBalance(self,t):

        total_principal_made=sum(list(self.principal_payments.values()))
        total_interest_shortfall=sum(list(self.interest_shortfall.values())[:t])
        return max(0,self.notional-total_principal_made+total_interest_shortfall)


    #This should return the amount of interest due for the current time period.
    #This can be calculated using the notional balance of the previous time period and the rate.
    def interestDue(self,t):
        if t==0:
            return 0
        else:
            return self.monthlyRate(self.rate) * self.notionalBalance(t - 1)+self.interest_shortfall[t-1]





    #This should record a principal payment for the current object time period.
    def makePrincipalPayment(self, payment,t):

        #This should only be allowed to be called once for a given time period (raise an error otherwise)
        if self.principal_paid==True:
            logging.error(f'Principal payment has already been made for {t}')


        elif self.notionalBalance(t)==0:
            self.principal_payments[t]=0
            return 0



        else:
            self.principal_payments[t]=payment
            self.principal_paid=True


    #This should record an interest payment for the current object time period.
    def makeInterestPayment(self,payment,t):

        #This should only be allowed to be called once for a given time period (raise an error otherwise).
        if self.interest_paid==True:
            logging.error(f'Interest payment has already been made for {t}')


        elif self.interestDue(t)==0:
            self.interest_payments[t] = 0
            self.interest_shortfall[t]=0

        else:
            self.interest_payments[t] = payment

            # If the interest amount is less than the current interest due,
            # the missing amount needs to be recorded
            # separately as an interest shortfall
            self.interest_shortfall[t] = max(self.interestDue(t)-payment,0)
            interest_paid=True










    #This should reset the tranche to its original state (time 0).
    def reset(self):

        self.period=0
        self.interest_payment={0:0}
        self.principal_payments = {0:0}
        self.interest_shortfall = {0: 0}
        self.interest_Due = {0: 0}
        self.principalShortFall = {0: 0}

        self.interest_paid = False
        self.principal_paid = False
