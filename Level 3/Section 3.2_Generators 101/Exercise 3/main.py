#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.3





# Import LoanPool from loan_pool
from loan.loan_pool import LoanPool

#Import Loan from loan_base
from loan.loan_base import Loan
from asset.asset import *


def main():
    # Code goes here
    print('\n==========Exercise 3.2.3==========')

    # Initialize loans
    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    loan_a = Loan(200000, .05, 40, asset_a)
    loan_b = Loan(300000, .06, 42, asset_a)
    loan_c = Loan(400000, .07, 44, car_a)
    loan_d = Loan(400000, .08, 44, car_a)
    loan_e = Loan(400000, .088, 44, car_a)

    # Make those loans above as a list, then initialize this list into loan pool
    Loans = [loan_a, loan_b, loan_c, loan_d, loan_e]

    loan_pool = LoanPool(Loans)

    print('\n------Testing block 1-----')
    print('Print out each loan‘s face value:')
    #The result will be that you should be able to loop over a LoanPool object’s individual Loan objects
    for loan in loan_pool:
        print(loan.notional)

    print('\n------Testing block 2-----')
    print('Print out each loan‘s annual rate:')
    # The result will be that you should be able to loop over a LoanPool object’s individual Loan objects
    for loan in loan_pool:
        print(loan.getRate())

    print('\n------Testing block 3-----')
    print('Print out each loan‘s term:')
    # The result will be that you should be able to loop over a LoanPool object’s individual Loan objects
    for loan in loan_pool:
        print(loan.term)

    print('\n------Testing block 4-----')
    print('Print out each loan‘s asset initial value:')
    # The result will be that you should be able to loop over a LoanPool object’s individual Loan objects
    for loan in loan_pool:
        print(loan.asset.init_val)

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()