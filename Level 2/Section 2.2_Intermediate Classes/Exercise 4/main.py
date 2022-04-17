#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.4


# Import AutoLoan and FixedRateLoan from loans
from loan.loans import AutoLoan, FixedRateLoan


def main():
    print('------Exercise 2.2.4------')
    print('Testing the Auto Loan class\n')

    print('\n------Testing block ----')
    print('Test the init function from Auto Loan class:')

    # Initialize auto with AutoLoan class
    auto=AutoLoan(200000, 0.05, 24,200000)
    print('The auto loan information will be:')
    print('Auto Loan‘s face value(in US dollars):', auto.notional, '\nAuto Loan’s annual interest rate:', auto.getRate(),
          '\nAuto Loan‘s terms(in months):', auto.term, '\nAuto‘s value:', auto.asset)







    print('\n***Program Complete***')


if __name__ == '__main__':
    main()