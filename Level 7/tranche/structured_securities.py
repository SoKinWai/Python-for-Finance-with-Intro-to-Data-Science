#Student Name: Jianwei Su
#Date: 05/20/2022
#7.1.3

import logging
from tranche.standard_tranche import StandardTranche



#Create a class called StructuredSecurities. This will be a composition of Tranche objects
class StructuredSecurities(object):

    #It should be initialized with a total Notional amount
    def __init__(self, total_notional,mode):

        self.total_notional = total_notional

        #object’s internal list of tranches
        self.tranches=[]

        #Add a method that flags ‘Sequential’ or ‘Pro Rata’ modes on the object
        self.mode=mode

        self.period = 0

        self.reserved_amount = 0



        self.loanpool = None

        # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument total_notional
    @property
    def total_notional(self):
        return self._total_notional

    # Decorator to set total_notional
    @total_notional.setter
    def total_notional(self, itotal_notional):
        self._total_notional = itotal_notional  # Set instance variable total_notional from input


    @property
    def tranches(self):
        return self._tranches

    @tranches.setter
    def tranches(self,itranches):
        self._tranches=itranches

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, imode):
        if imode=='Sequential' or imode=='Pro Rata':
            self._mode = imode
        else:
            logging.error('Error: Mode has to be ‘Sequential’ or ‘Pro Rata’.')

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, iperiod):
        self._period = iperiod

    @property
    def loanpool(self):
        return self._loanpool

    @loanpool.setter
    def loanpool(self, iloanpool):
        self._loanpool = iloanpool



    @property
    def reserved_amount(self):
        return self._reserved_amount

    @reserved_amount.setter
    def reserved_amount(self,ireserved_amount):
        self._reserved_amount=ireserved_amount




    def addTranche(self, notional_percent, rate, subordination_flag):

        tranche_class=StandardTranche(notional_percent*self.total_notional, rate, subordination_flag)

        # Add the tranche to the StructuredSecurity object’s internal list of tranches
        self.tranches.append(tranche_class)

        #Use subordination_level to sort tranches list
        self.tranches.sort(key=lambda x:x.subordination_flag)



    #Add a method that increases the current time period for each tranche.
    def increaseTranchesTimePeriod(self):
        self.period += 1

        for tranche in self.tranches:
            tranche.increaseTimePeriod()


    #Create a method called makePayments. This should have a cash_amount parameter.
    def makePayments(self, cash_amount):

        cash_amount=cash_amount+self.reserved_amount

        #It should cycle through all interest payments first, paying each tranche from the available cash_amount.
        for tranche in self.tranches:
            #record interest due for that time period
            interestDue=tranche.interestDue(self.period)
            tranche.interest_Due[self.period]=interestDue
            interestPaid=min(interestDue,cash_amount)

            #make the payment, subtract the paid amount from the availableFunds
            tranche.makeInterestPayment(interestPaid,self.period)
            cash_amount=cash_amount-interestPaid


        #Assuming there is cash left over after all the interest paymentss, begin cycling through
        #the tranches to make principal payments.

        #Principal due to the tranches are based on the total principal received from the Loans in a given period
        principal_received=self.loanpool.Total_principalDue(self.period)

        #Cycle through each tranche (in order of subordination), making the maximum principal payment
        if self.mode=='Sequential':
            for tranche in self.tranches:

                #Ask each tranche for its balance and pay min(principal received + prior principal shortfalls, available cash, balance).
                principal_received=principal_received+tranche.principalShortFall[self.period-1]

                principal_due=min(principal_received,cash_amount,tranche.notionalBalance(self.period)) if not cash_amount==0 else 0

                principal_paid=min(cash_amount,principal_due)

                tranche.makePrincipalPayment(principal_paid, self.period)

                tranche.principalShortFall[self.period]=principal_due-principal_paid

                principal_received =principal_received-principal_paid

                cash_amount=cash_amount-principal_paid


        elif self.mode == 'Pro Rata':

            total_principal_paid=0

            for tranche in self.tranches:

                principal_due=min(principal_received*tranche.notional/self.total_notional+tranche.principalShortFall[self.period-1],cash_amount, tranche.notionalBalance(self.period)) if not cash_amount==0 else 0

                principal_paid = min(cash_amount, principal_due)

                tranche.makePrincipalPayment(principal_paid, self.period)

                tranche.principalShortFall[self.period] = principal_due - principal_paid

                principal_received = principal_received - principal_paid

                total_principal_paid=total_principal_paid+principal_paid

            cash_amount=cash_amount-total_principal_paid

        #Once all interest and principal payments have been made, it’s possible that there is
        #leftover cash. This extra cash goes into a reserve account.

        self.reserved_amount=cash_amount




    def getWaterfall(self,period):

        waterfall=[[period]]
        for tranche in self.tranches:
            waterfall.append([tranche.interest_Due[period],tranche.interest_payments[period],tranche.interest_shortfall[period],tranche.principal_payments[period],tranche.notionalBalance(period)])



        waterfall.append([self.reserved_amount])

        return waterfall




    def reset(self):
        self.period = 0

        self.reserved_amount = 0



        [tranche.reset() for tranche in self.tranches]