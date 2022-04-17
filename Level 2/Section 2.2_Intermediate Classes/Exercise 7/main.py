#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.7

# Import different classes from asset and loan
from asset.asset import *
from loan.loan_base import *
from loan.mortgage import *
from loan.loans import *


def main():
    print('------Exercise 2.2.7------')
    print('Testing different Loan types with different assets\n')

    print('\n------Testing block 1----')
    print('Test the init function from Loan base class:')

    # Initialize values for different classes
    asset_a=Asset(3000000)
    car_a=CarMixin(1000000)
    loan_a=Loan(3000000,0.05, 35,asset_a)
    loan_b=Loan(1000000,0.06, 30,car_a)

    print('The asset loan information will be:')
    print('Asset Loan‘s face value(in US dollars):', loan_a.notional, '\nAsset Loan’s annual interest rate:', loan_a.getRate(),
          '\nAsset Loan‘s terms(in months):', loan_a.term, '\nAsset‘s initial value:', loan_a.asset.init_val)

    print('\nThe car loan information will be:')
    print('Car Loan‘s face value(in US dollars):', loan_b.notional, '\nCar Loan’s annual interest rate:',
          loan_b.getRate(),'\nCar Loan‘s terms(in months):', loan_b.term, '\nCar‘s initial value:', loan_b.asset.init_val)

    print('\n------Testing block 2----')
    print('Test the init function from MortgageMixin class:')

    # Initialize values for different classes

    primaryhome_a=PrimaryHome(400000)
    vacayhome_a = VacationHome(500000)
    mortgage_a = FixedMortgage(400000, .05, 30, primaryhome_a)
    mortgage_b = FixedMortgage(500000, .05, 35, vacayhome_a)

    print('The mortgage_a information will be:')
    print('Mortgage‘s face value(in US dollars):', mortgage_a.notional, '\nMortgage’s interest rate:',
          mortgage_a.getRate(), '\nMortgage‘s terms(in months):', mortgage_a.term, '\nMortgage‘s initial value:', mortgage_a.asset.init_val)

    print('\nThe mortgage_b information will be:')
    print('Mortgage‘s face value(in US dollars):', mortgage_b.notional, '\nMortgage’s interest rate:',
          mortgage_b.getRate(), '\nMortgage‘s terms(in months):', mortgage_b.term, '\nMortgage‘s initial value:', mortgage_b.asset.init_val)

    print('\n------Testing block 3----')
    print('Test the PMI() function from MortgageMixin class:')
    #input is within the term of the loan and greater than 0
    print('mortgage_b in period 30 is',mortgage_b.PMI(30))
    print('mortgage_b in period 5 is',mortgage_b.PMI(5))

    print('\n------Testing block 4----')
    print('Test the init function from AutoLoan class:')

    # Initialize value for Toyota class
    car_b = Toyota(30000)
    autoloan_a= AutoLoan(1000000, .06, 40, car_a)
    autoloan_b = AutoLoan(30000, .04, 30, car_b)

    print('The auto_a loan information will be:')
    print('Auto Loan‘s face value(in US dollars):', autoloan_a.notional, '\nAuto Loan’s interest rate:',
          autoloan_a.getRate(), '\nAuto Loan‘s terms(in months):', autoloan_a.term, '\nAuto‘s initial value:',autoloan_a.asset.init_val)

    print('\nThe auto_b loan information will be:')
    print('Auto Loan‘s face value(in US dollars):', autoloan_b.notional, '\nAuto Loan’s interest rate:',
          autoloan_b.getRate(), '\nAuto Loan‘s terms(in months):', autoloan_b.term, '\nAuto‘s initial value:',autoloan_b.asset.init_val)

    print('\n------Testing block 5----')
    print('Test the recoveryValue() function from Loan Base class:')

    #input is within the term of the loan and greater than 0

    print('The recovery value for autoloan_b in period 25 is',autoloan_b.recoveryValue(25))
    print('The recovery value for autoloan_a in period 30 is',autoloan_a.recoveryValue(30))

    print('The recovery value for mortgage_a in period 20 is',mortgage_a.recoveryValue(20))
    print('The recovery value for mortgage_b in period 28 is',mortgage_b.recoveryValue(28))

    #It will give an error because annualDeprRate() function from Asset class will raise an error
    #print('The recovery value for loan_a in period 26 is', loan_a.recoveryValue(26))

    #input is within the term of the loan and greater than 0
    print('The recovery value for loan_b in period 26 is', loan_b.recoveryValue(26))

    print('\n------Testing block 6----')
    print('Test the equity() function from Loan Base class:')

    #input is within the term of the loan and greater than 0
    print('The equity for loan_b in period 26 is', loan_b.equity(26))

    #It will give an error because annualDeprRate() function from Asset class will raise an error
    #print('The equity for loan_a in period 26 is', loan_a.equity(26))

    #input is within the term of the loan and greater than 0
    print('The equity for autoloan_b in period 25 is', autoloan_b.equity(25))
    print('The equity for autoloan_a in period 30 is', autoloan_a.equity(30))

    print('The equity for mortgage_a in period 20 is', mortgage_a.equity(20))
    print('The equity for mortgage_b in period 28 is', mortgage_b.equity(28))









    print('\n***Program Complete***')


if __name__ == '__main__':
    main()

