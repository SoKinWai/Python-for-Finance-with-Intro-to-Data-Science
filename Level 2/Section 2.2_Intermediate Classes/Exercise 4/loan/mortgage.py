#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.4

#Import Loan from loan_base
from loan.loan_base import Loan

#Derived classes
#Import FixedRateLoan, VariableRateLoan from loans
from loan.loans import FixedRateLoan, VariableRateLoan


#class MortgageMixin

class MortgageMixin(object):

    def __init__(self, notional, rate, term, asset):

        # Invoke the initialization function in the base class
        super(MortgageMixin, self).__init__(notional, rate, term, asset)



    # Implement a function called PMI that returns 0.0075% of the loan face value, but only if the LTV is < 80%.
    # Assume that the initial loan amount is for 100% of the asset value.

    # PMI() function
    # When LTV>=0.8, it returns to 0.0075% of the asset initial value
    # LTV= the loan amount /the asset is taken out initially value
    def PMI(self, period):
        # The balance of the loan at a given period (balance).
        # This method is to calculate remaining loan balance due at time period.
        if period >= 0 and period <= self.term and self.getRate(period) > 0 and self.notional > 0 and self.term > 0:
            balance = super(MortgageMixin, self).balance(period)

            # Loan-to-Value ratio
            LTV = balance / self.asset
            if LTV >= 0.8:
                return 0.000075 * self.notional
            else:
                # When LTV<0, it should return to 0
                return 0
        else:
            print("Error: Period have to be within the term of the loan and greater than or equal to 0 and the loan class inputs have to be greater than 0")


    # Override the base class monthlyPayment and principalDue functions to account for PMI

    # monthlyPayment() function.
    # Override the base class monthlyPayment function to account for PMI and use super to avoid duplicating the formula
    # It's the regular monthly payment plus PMI.
    def monthlyPayment(self, period):
        if period >= 0 and period <= self.term:
            return super(MortgageMixin, self).monthlyPayment(period) + self.PMI(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than or equal to 0.")


    # principalDue() function.The principal amount due at a given period (principalDue).
    # Override the base class principalDue function to account for PMI and use super to avoid duplicating the formula
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue(self, period):
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:
            return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than or equal to 0.")


    # A recursive version
    # principalDue_recur() function. The principal amount due at a given period (principalDue_recur).
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue_recur(self, period):
        # I will use this formula to calculate the principal due:
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:
            return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue_recur(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than or equal to 0.")



# Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate base class(es).

# Derived class from MortgageMixin and FixedRateLoan
# It gets everything from MortgageMixin and FixedRateLoan
class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

# Derived class from MortgageMixin and VariableRateLoan
# It gets everything from MortgageMixin and VariableRateLoan
class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass
