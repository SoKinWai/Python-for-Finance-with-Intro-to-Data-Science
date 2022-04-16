#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.2

# Import necessary packages

from loan.loan import Loan

def main():
    # Test Loan class thoroughly.

    print('------Exercise 2.1.2------')
    print('Testing the Loan class\n')

    # Initialize loan_1 with Loan class
    loan_1=Loan(200000,0.05, 24)
    print('The loan information will be:')
    print('Loan‘s face value(in US dollars):',loan_1.notional,'\nLoan’s interest annual rate:',loan_1.rate,'\nLoan‘s terms(in months):',loan_1.term)

    #Test the totalPayments() function
    #Use the totalPayments() to calculate the total loan payment
    print('\n------Testing block 1-----')
    print('Testing the totalPayments() function:')


    #round to 0.01
    print('The total payment for loan_1 round to 0.01 will be(in US dollars):',round(loan_1.totalPayments(),2))

    #Test the monthlyPayment() function
    # Use the monthlyPayment() to calculate the monthly loan payment
    print('\n------Testing block 2-----')
    print('Testing the monthlyPayment() function:')

    # round to 0.01
    print('The monthly payment for loan_1 round to 0.01 will be(in US dollars):', round(loan_1.monthlyPayment(),2))

    # Test the totalInterest() function
    # Use the totalInterest() to calculate the total loan interest
    print('\n------Testing block 3-----')
    print('Testing the totalInterest() function:')


    #round to 0.01
    print('The total interest payment for loan_1 round to 0.01 will be(in US dollars):', round(loan_1.totalInterest(),2))

    # Initialize loan_2 with negative inputs
    loan_2 = Loan(-200000, -0.05, 24.5)

    # Test the totalPayments() function
    # Use the totalPayments() to calculate the total loan payment
    print('\n------Testing block 4-----')
    print('Testing the __int__ function with negative inputs:')
    print('The loan information will be:')


    print('Loan‘s face value(in US dollars):',loan_2.notional,'\nLoan’s interest annual rate:',loan_2.rate,'\nLoan‘s terms(in months):',loan_2.term)





    print('\n***Program Complete***')








if __name__ == '__main__':
    main()