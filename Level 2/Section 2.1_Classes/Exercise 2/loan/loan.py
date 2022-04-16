#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.2

# Loan class
# This class' object takes on the arguments notional, rate, term
class Loan(object):

    # Initialize function with notional, rate and term
    def __init__(self,notional, rate, term):

            self.notional = notional

            self.term = term

            self.rate = rate




    #Add getter and setter property functions here
    # Decorators to get and the set values for the instance variables

    # Decorator to create a property function to get the argument rate
    @property
    def notional(self):
        return self._notional

    @notional.setter
    def notional(self, inotional):
        if inotional > 0:
            self._notional = inotional  # Set the instance variable notional from input
        else:
            self._notional='\nError: Please make sure the input of face value is greater than 0.'

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
            self._rate = '\nError:Please make sure the input of rate is greater than 0.'

    # Decorator to create a property function to get the argument term
    @property
    def term(self):
        return self._term

    # Decorator to set the term
    @term.setter
    def term(self, iterm):
        if iterm > 0 and type(iterm)==int:
            self._term = iterm  # Set the instance variable term from input
        else:
            self._term = '\nError:Please make sure the input of term is an integer and greater than 0.'




    #The monthly payment amount of the loan (monthlyPayment)
    #Define the function with a dummy ‘period’ parameter because
    # it’s possible some loan types will have a monthly payment dependent on the period.
    # monthlyPayment() function to calculate monthly payments
    def monthlyPayment(self, period=None): #period is the dummy variable
        # pmt  = (r * P * (1 + r)^N) / ((1 + r)^N - 1), pmt is monthly payment amount
        # r is monthly interest rate, P is principal which is notional value and N is term
        # of loan(in months)

        r=self.rate/12
        P=self.notional
        N=self.term

        return (r*P*(1+r)**N)/((1+r)**N-1)


    #Total payments over the entire loan
    #totalPayments() function.
    def totalPayments(self,period=None):

        #Sum up each month's payments to get the total payment
        return sum([self.monthlyPayment(p) for p in range(1,self.term+1)])



    #Total interest over the entire loan
    #totalInterest() function. This will be total payments minus notional face values.
    def totalInterest(self,period=None):

        return self.totalPayments()-self.notional

