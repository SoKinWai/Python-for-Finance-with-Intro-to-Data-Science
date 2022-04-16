#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.4

# Importing necessary packages

from loan.loan import Loan

def main():
    # Test Loan class thoroughly.

    print('------Exercise 2.1.4------')
    print('Testing the Loan class\n')


    # Initialize loan_1 with Loan class
    loan_1=Loan(200000,0.05, 24)
    print('The loan information will be:')
    print('Loan‘s face value(in US dollars):',loan_1.notional,'\nLoan’s annual interest rate:',loan_1.rate,'\nLoan‘s terms(in months):',loan_1.term)

    #Initialize face, rate, term and period
    face=200000
    rate=0.05
    term=24
    period=22

    # This test block will calculate the given loan's monthly payment using class method.
    print('\n------Testing block 1-----')
    print('Test monthly functions in class and original object-level methods:')
    print('The monthly payment for this loan is(class method):',loan_1.calcMonthlyPmt(face,rate,term))
    print('The monthly payment for this loan is(object-level method to delegate to the class-level method):',loan_1.monthlyPayment())


    # This test block will calculate the given loan's outstanding balance using class method.
    print('\n------Testing block 2-----')
    print('Test outstanding balance functions in class and original object-level methods:')
    print('The outstanding balance for this loan is(class method):', loan_1.calcBalance(face, rate, term, period))
    print('The outstanding balance for this loan is(object-level method to delegate to the class-level method):', loan_1.balance(period))



    #What are the benefits of class-level methods? When are they useful?
    # It allows you pass in the specific object and it will save time.
    # When the object is not instantiated, these methods can be considered using.



    # Initialize period of negative value
    period = -22

    # This test block will calculate the given loan's outstanding balance using class method.
    print('\n------Testing block 3-----')
    print('Testing with negative periods:')
    print('Test outstanding balance functions in class and original object-level methods:')
    print('The outstanding balance for this loan is(class method):', loan_1.calcBalance(face, rate, term, period))
    print('The outstanding balance for this loan is(object-level method to delegate to the class-level method):',
          loan_1.balance(period))




    print('\n***Program Complete***')


if __name__ == '__main__':
    main()