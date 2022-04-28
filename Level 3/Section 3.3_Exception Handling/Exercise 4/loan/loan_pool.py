#Student Name: Jianwei Su
#Date: 04/20/2022
#3.3.4


#Import Loan from loan_base
from loan.loan_base import Loan

#Import reduce function from functools
from functools import reduce


#Create a LoanPool class
class LoanPool(object):
    # loans are the loans taken out for initially valued at
    # loans should be a loan list here
    def __init__(self, loans):
        self.loans = loans



    #Modify your LoanPool class to be an iterable.
    #Define an __iter__ method within the class
    #This method should be a generator, that returns one Loan at a time.
    def  __iter__(self,loans=None):
        for loan in self.loans:
            yield loan

    # Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument loans
    @property
    def loans(self):
        return self._loans

    # Decorator to set loans
    @loans.setter
    def loans(self, iloans):
        self._loans = iloans  # Set instance variable loans from input


    # Get the total loan principal
    # Total_principal() function
    def Total_principal(self):
        # Sum up all the loans' principals
        return sum(loan.notional for loan in self.loans)

    # Get the total loan balance for a given period
    # Total_balance() function
    def Total_balance(self, period):
        # Sum up all the loans' balances
        return sum(loan.balance(period) for loan in self.loans)


    # Get the aggregate principal due in a given period
    # Total_principalDue() function
    def Total_principalDue(self, period):
        # Sum up all the loans' principal due payments
        return sum(loan.principalDue(period) for loan in self.loans)

    # Get the aggregate interest due in a given period
    # Total_interestDue() function
    def Total_interestDue(self, period):
        # Sum up all the loans' interest due payments
        return sum(loan.interestDue(period) for loan in self.loans)

    # Get the aggregate monthly payments in a given period
    # Total_monthlyPayment() function
    def Total_monthlyPayment(self, period):
        # Sum up all the loans' monthly payments
        return sum(loan.monthlyPayment(period) for loan in self.loans)

    # Returns the number of ‘active’ loans.
    # Active loans are loans that have a balance greater than zero.
    # active_loans() function
    def active_loans(self, period):
        # Calculate how many active loans
        return len([loan for loan in self.loans if loan.balance(period) > 0])

    # Create a function that calculates the Weighted Average Rate of the loan pool.
    # WAR() function.
    def WAR_original(self):
        # Sum up each face value*rate from each loan
        weighted_rate = sum([loan.notional * loan.getRate() for loan in self.loans if loan.getRate() > 0 and loan.notional > 0 and loan.term > 0])
        # Here returns the Weighted Average Rate of the loan pool.
        return weighted_rate / self.Total_principal()

    # Create a function that calculates the Weighted Average Maturity (term) of the loan pool.
    # WAM_original() function
    def WAM_original(self):
        # Sum up each face value*term from each loan
        weighted_maturity = sum([loan.notional * loan.term for loan in self.loans if loan.getRate() > 0 and loan.notional > 0 and loan.term > 0])
        # Here returns the Weighted Average Maturity (term) of the loan pool
        return weighted_maturity / self.Total_principal()

    # Create a function that calculates the Weighted Average Rate of the loan pool via using reduce function
    # WAR() function
    def WAR(self):
        # Create a list to store loan amounts and rates.
        vals = [(loan.getRate(), loan.notional) for loan in self.loans]

        return reduce(lambda total, loan: total + loan[0] * loan[1] / float(self.Total_principal()), vals, 0)

    # Create a function that calculates the Weighted Average Maturity (term) of the loan pool via using reduce function
    # WAM() function
    def WAM(self):
        # Create a list to store loan amounts and terms.
        vals = [(loan.notional, loan.term) for loan in self.loans]

        return reduce(lambda total, loan: total + loan[0] * loan[1] / float(self.Total_principal()), vals, 0)