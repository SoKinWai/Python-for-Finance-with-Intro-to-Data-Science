#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.5

# Importing necessary packages

from loan.loan import Loan

def main():
    # Test Loan class thoroughly.
    print('------Exercise 2.1.5------')
    print('Testing the Loan class\n')

    # Initialize loan_1 with Loan class
    loan_1 = Loan(200000, 0.05, 24)
    print('The loan information will be:')
    print('Loan‘s face value(in US dollars):', loan_1.notional, '\nLoan’s annual interest rate:', loan_1.rate,
          '\nLoan‘s terms(in months):', loan_1.term)

    print('\n------Testing block 1-----')

    # Initialize annual interest rate
    Annual_rate=0.05
    print('Test the static monthly rate function:')
    print('The monthly rate will be:', loan_1.monthlyRate(Annual_rate))

    print('\n------Testing block 2-----')

    # Initialize annual interest rate
    monthly_rate = loan_1.monthlyRate(Annual_rate)
    print('Test the static annual rate function:')
    print('The annual rate will be:', loan_1.Annual_rate(monthly_rate))


    #Initialize face, annual rate, term and period
    face = 200000
    rate = 0.05
    term = 24
    period = 22

    # This test block will calculate the given loan's monthly payment using class method.
    print('\n------Testing block 3-----')
    print('Test monthly functions in class:')
    print('The monthly payment for this loan is(class method):', loan_1.calcMonthlyPmt(face, rate, term))

    # This test block will calculate the given loan's outstanding balance using class method.
    print('\n------Testing block 4-----')
    print('Test outstanding balance functions in class:')
    print('The outstanding balance for this loan is(class method):', loan_1.calcBalance(face, rate, term, period))


    # This test block will calculate the given loan's monthly payment using object-level
    # method to delegate to the class-level method
    print('\n------Testing block 5-----')
    print('Test monthly functions in object-level method to delegate to the class-level method:')
    print('The monthly payment for this loan is(object-level method to delegate to the class-level method):',
          loan_1.monthlyPayment())

    # This test block will calculate the given loan's outstanding balance using object-level
    # method to delegate to the class-level method
    print('\n------Testing block 6-----')
    print('Test outstanding balance functions in object-level method to delegate to the class-level method:')

    #input is within the term of the loan and greater than 0
    print('The outstanding balance for this loan is(object-level method to delegate to the class-level method):',
          loan_1.balance(period))

    # Test the balance_recur() function.
    #Use the balance_recur() to calculate the balance
    print('\n------Testing block 7-----')
    print('Test balance functions in recursive forms:')

    #input is within the term of the loan and greater than 0
    print('The balance in time period 22 will be(recursive form):', loan_1.balance_recur(period))

    # Test the interestDue() and interestDue_recur() functions.
    # Use the interestDue()  and interestDue_recur() to calculate the interest due.
    # Compare the following two results to make sure they are the same.
    print('\n------Testing block 8-----')
    print('Test interest due functions in normal and recursive forms:')

    #input is within the term of the loan and greater than 0
    print('The interest due function in time period 22 will be(normal form):', loan_1.interestDue(period))

    #input is within the term of the loan and greater than 0
    print('The interest due in time period 22 will be(recursive form):', loan_1.interestDue(period))

    # Test the principalDue() and principalDue_recur() functions.
    # Use the principalDue()  and principalDue_recur() to calculate the principal due.
    # Compare the following two results to make sure they are the same.
    print('\n------Testing block 9-----')
    print('Test principal due functions in normal and recursive forms:')

    #input is within the term of the loan and greater than 0
    print('The principal due function in time period 22 will be(normal form):', loan_1.principalDue(period))
    print('The principal due in time period 22 will be(recursive form):', loan_1.principalDue_recur(period))

    # Test the totalPayments() function
    # Use the totalPayments() to calculate the total loan payment
    print('\n------Testing block 10-----')
    print('Testing the totalPayments() function:')
    # Round to 0.01
    print('The total payment for loan_1 round to 0.01 will be(in US dollars):', round(loan_1.totalPayments(), 2))

    # Test the totalInterest() function
    # Use the totalInterest() to calculate the total loan interest
    print('\n------Testing block 11-----')
    print('Testing the totalInterest() function:')
    # Round to 0.01
    print('The total interest payment for loan_1 round to 0.01 will be(in US dollars):',
          round(loan_1.totalInterest(), 2))

    #What are the benefits of static-level methods? When are they useful?
    #Static-level method is very useful for grouping common things together instead of having the
    #functions all over the place. It gives us logical grouping to keep things organized and together.

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()