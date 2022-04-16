#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.4

# Loan class
# This class' object takes on the arguments notional, rate, term
class Loan(object):

    # Initialize function with notional, rate and term

    def __init__(self, notional, rate, term):
        self.notional = notional

        self.term = term

        self.rate = rate

    # DefaultLoan function to set default loan
    @classmethod
    # Set at the class level the values of notional, rate and term as default if they are not specified
    # Instead of storing dnotional, drate and dterm at the object level, store them at the class level
    def defaultLoan(cls, notional, rate, term):
        # Get values of each class variable from the instance objects
        cls._dnotional = notional
        cls._drate= rate
        cls._dterm=term

    #Add getter and setter property functions here
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
            self._notional = '\nError: Please make sure the input of face value is greater than 0.'

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
        if iterm > 0 and type(iterm) == int:
            self._term = iterm  # Set the instance variable term from input
        else:
            self._term = '\nError:Please make sure the input of term is an integer and greater than 0.'


    #The monthly payment amount of the loan (monthlyPayment)
    #Define the function with a dummy ‘period’ parameter because
    # it’s possible some loan types will have a monthly payment dependent on the period.
    # monthlyPayment() function to calculate monthly payments
    #def monthlyPayment(self, period=None): #period is the dummy variable
        # pmt  = (r * P * (1 + r)^N) / ((1 + r)^N - 1), pmt is monthly payment amount
        # r is monthly interest rate, P is principal which is notional value and N is term
        # of loan(in months)
     #   r=self.rate
     #  P=self.notional
     #   N=self.term

     #   return (r*P*(1+r)**N)/((1+r)**N-1)

    #Total payments over the entire loan
    #totalPayments() function.
    def totalPayments(self):

        # Sum up each month's payments to get the total payment
        return sum([self.monthlyPayment(p) for p in range(1, self.term + 1)])


    #Total interest over the entire loan
    #totalInterest() function. This will be total payments minus notional face values.
    def totalInterest(self):

        #Total interest= Total payments- Notional face value
        return self.totalPayments()-self.notional


    # A version that uses the formulas provided in the slides
    #balance() function. The balance of the loan at a given period (balance).
    #This method is to calculate remaining loan balance due at time period.
    #def balance(self,period):
        #I will use this formula to calculate the balance:
        #balance = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r is monthly interest rate, P is principal which is notional value and N is term
        # of loan(in months)
        # n is number of payments made, but we could think of it as the time period here.
     #   return self.notional*((1+self.rate)**period)-self.monthlyPayment()*(((1+self.rate)**period)-1)/self.rate


    # A version that uses the formulas provided in the slides.
    #interestDue() function. The interest amount due at a given period (interestDue).
    #This method is to calculate interest due at time period.
    def interestDue(self,period):
        # I will use this formula to calculate the interest due:
        # Interest Due= Monthly Rate * previous time period balance
        if period > 0 and period <= self.term:
            return (self.rate/12)* self.balance(period-1)
        else:
            print("Error: Period has to be within the term of the loan and greater than 0.")

    # A version that uses the formulas provided in the slides.
    #principalDue() function. The principal amount due at a given period (principalDue).
    #Principal due is the monthly payment less the interest due.
    #This method is to calculate principal due at time period.
    def principalDue(self,period):
        # I will use this formula to calculate the principal due:
        #principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:
            return self.monthlyPayment()-self.interestDue(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than 0.")

    #A recursive version
    # principalDue_recur() function. The principal amount due at a given period (principalDue_recur).
    # Principal due is the monthly payment less the interest due.
    # This method is to calculate principal due at time period.
    def principalDue_recur(self,period):
        # I will use this formula to calculate the principal due:
        # principalDue = monthlyPayment - interestDue
        if period > 0 and period <= self.term:
            return self.monthlyPayment()-self.interestDue_recur(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than 0.")

    # A recursive version
    # interestDue_recur() function. The interest amount due at a given period (interestDue_recur).
    # This method is to calculate interest due at time period.
    def interestDue_recur(self,period):
        # I will use this formula to calculate the interest due:
        # Interest Due= Monthly Rate * previous time period balance
        if period > 0 and period <= self.term:
            return self.balance_recur(period - 1) * self.rate / 12
        else:
            print("Error: Period has to be within the term of the loan and greater than 0.")

    #A recursive version
    # balance_recur() function. The balance of the loan at a given period (balance_recur).
    # This method is to calculate remaining loan balance due at time period.
    def balance_recur(self, period):
        # I will use this formula to calculate the balance:
        # balance at current period= previous balance-current principal due
        if period >= 0 and period <= self.term :
            if period == 0:
                return self.notional
            else:
                return self.balance_recur(period - 1) - self.principalDue_recur(period)
        else:
            print("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    #Implement a class-level method called calcMonthlyPmt, in the Loan base class.
    # This should calculate a monthly payment based on three parameters: face, rate, and term.

    #This is the class method to calculate the monthly payment of the given loan
    #calcMonthlyPmt() function
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        # I will use this formula to calculate the balance:
        # pmt  = (r*P)/(1-1+r)**-N, pmt is monthly payment amount
        # r is monthly interest rate, P is principal which is face value and N is term
        # of loan(in months)

        return (face * (rate/12)) / (1 - (1 + rate/12) ** (-term))


    #Create a class -level function, in the Loan base class, which calculates the balance (calcBalance).
    # Input parameters should be face, rate, term, period.

    #This is the class method to calculate outstanding balance of the given loan at given period
    #calcBalance() function.
    @classmethod
    def calcBalance(cls,face, rate, term, period):
        # I will use this formula to calculate the balance:
        # balance = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r is monthly interest rate, P is principal which is face value and N is term
        # of loan(in months)
        # n is number of payments made, but we could think of it as the time period here.
        if period >= 0 and period <= term:
            return face*((1+rate/12)**period)-cls.calcMonthlyPmt(face, rate, term)*(((1+rate/12)**period)-1)/(rate/12)
        else:
            print("Error: Period has to be within the term of the loan and greater than or equal to 0.")

    # Modify the object-level methods for monthlyPayment to delegate to the class-level methods.

        # The monthly payment amount of the loan (monthlyPayment)
        # Define the function with a dummy ‘period’ parameter because
        # it’s possible some loan types will have a monthly payment dependent on the period.
        # monthlyPayment() function to calculate monthly payments
    def monthlyPayment(self, period=None):  # period is the dummy variable
        # Notional is equivalent to face
        return self.calcMonthlyPmt(self.notional,self.rate,self.term)



    #Modify the object-level methods for balance to delegate to the class-level methods.

        # balance() function. The balance of the loan at a given period (balance).
        # This method is to calculate remaining loan balance due at time period.
    def balance(self, period):
        # Notional is equivalent to face
        return self.calcBalance(self.notional,self.rate,self.term,period)
