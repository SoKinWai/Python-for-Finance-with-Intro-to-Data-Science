#Student Name: Jianwei Su
#Date: 05/09/2022
#5.1.6

import logging
import datetime
from asset.asset import *
from loan.loan_base import *
from loan.mortgage import *
from loan.loans import *


def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.1.6==========')

    logging.info('\n------Testing block 1-----')
    logging.info('\nTest the init function from Loan base class')

    # Initialize values for different classes
    d1='2012-12-28 14:24:12:123456'
    d2='2016-09-25 18:23:14:012342'

    date_1 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S:%f')

    date_2 = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M:%S:%f')

    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    loan_a = Loan(3000000, 0.05, date_1,date_2, asset_a)
    loan_b = Loan(1000000, 0.06, date_1,date_2, car_a)

    logging.info('The asset loan information will be:')
    logging.info(f'Asset Loan‘s face value(in US dollars):{loan_a.notional} \nAsset Loan’s annual interest rate:{loan_a.getRate()} \nAsset Loan‘s terms(in months): {loan_a.term()} \nAsset‘s initial value:  {loan_a.asset.init_val}')

    logging.info('\n')
    logging.info('The car loan information will be:')
    logging.info(f'Asset Loan‘s face value(in US dollars):{loan_b.notional} \nAsset Loan’s annual interest rate:{loan_b.getRate()} \nAsset Loan‘s terms(in months): {loan_b.term()} \nAsset‘s initial value:  {loan_b.asset.init_val}')

    logging.info('\n')
    logging.info('\n------Testing block 2----')
    logging.info('Test the init function from MortgageMixin class:')

    # Initialize values for different classes

    primaryhome_a = PrimaryHome(400000)
    vacayhome_a = VacationHome(500000)
    mortgage_a = FixedMortgage(400000, .05, date_1,date_2, primaryhome_a)
    mortgage_b = FixedMortgage(500000, .05, date_1,date_2, vacayhome_a)

    logging.info('The mortgage_a information will be:')
    logging.info(f'Mortgage‘s face value(in US dollars): {mortgage_a.notional} \nMortgage’s interest rate:{mortgage_a.getRate()} \nMortgage‘s terms(in months): {mortgage_a.term()} \nMortgage‘s initial value:{mortgage_a.asset.init_val}')

    logging.info('\n')
    logging.info('The mortgage_b information will be:')
    logging.info(f'Mortgage‘s face value(in US dollars): {mortgage_b.notional} \nMortgage’s interest rate:{mortgage_b.getRate()} \nMortgage‘s terms(in months): {mortgage_b.term()} \nMortgage‘s initial value:{mortgage_b.asset.init_val}')

    logging.info('\n')
    logging.info('------Testing block 3----')
    logging.info('Test the PMI() function from MortgageMixin class:')
    # input is within the term of the loan and greater than 0
    logging.info(f'mortgage_b in period 30 is {mortgage_b.PMI(30)}')
    logging.info(f'mortgage_b in period 5 is {mortgage_b.PMI(5)}')

    logging.info('\n')
    logging.info('------Testing block 4----')
    logging.info('Test the init function from AutoLoan class:')

    # Initialize value for Toyota class
    car_b = Toyota(30000)
    autoloan_a = AutoLoan(1000000, .06, date_1,date_2, car_a)
    autoloan_b = AutoLoan(30000, .04, date_1,date_2, car_b)

    logging.info('The auto_a loan information will be:')
    logging.info(f'Auto Loan‘s face value(in US dollars): {autoloan_a.notional} \nAuto Loan’s interest rate {autoloan_a.getRate()} \nAuto Loan‘s terms(in months): {autoloan_a.term()} \nAuto‘s initial value: {autoloan_a.asset.init_val}')

    logging.info('\n')
    logging.info('The auto_b loan information will be:')
    logging.info(f'Auto Loan‘s face value(in US dollars): {autoloan_b.notional} \nAuto Loan’s interest rate {autoloan_b.getRate()} \nAuto Loan‘s terms(in months): {autoloan_b.term()} \nAuto‘s initial value: {autoloan_b.asset.init_val}')

    logging.info('\n')
    logging.info('------Testing block 5----')
    logging.info('Test the recoveryValue() function from Loan Base class:')

    # input is within the term of the loan and greater than 0

    logging.info(f'The recovery value for autoloan_b in period 25 is {autoloan_b.recoveryValue(25)}')
    logging.info(f'The recovery value for autoloan_a in period 30 is {autoloan_a.recoveryValue(30)}')

    logging.info(f'The recovery value for mortgage_a in period 20 is {mortgage_a.recoveryValue(20)}')
    logging.info(f'The recovery value for mortgage_b in period 28 is {mortgage_b.recoveryValue(28)}')

    # It will give an error because annualDeprRate() function from Asset class will raise an error
    #logging.info(f'The recovery value for loan_a in period 26 is {loan_a.recoveryValue(26)}')

    # input is within the term of the loan and greater than 0
    logging.info(f'The recovery value for loan_b in period 26 is {loan_b.recoveryValue(26)}')

    logging.info('\n')
    logging.info('------Testing block 6----')
    logging.info('Test the equity() function from Loan Base class:')

    # input is within the term of the loan and greater than 0
    logging.info(f'The equity for loan_b in period 26 is {loan_b.equity(26)}')

    # It will give an error because annualDeprRate() function from Asset class will raise an error
    # logging.info(f'The equity for loan_a in period 26 is {loan_a.equity(26)}')

    # input is within the term of the loan and greater than 0
    logging.info(f'The equity for autoloan_b in period 25 is {autoloan_b.equity(25)}')
    logging.info(f'The equity for autoloan_a in period 30 is {autoloan_a.equity(30)}')

    logging.info(f'The equity for mortgage_a in period 20 is {mortgage_a.equity(20)}')
    logging.info(f'The equity for mortgage_b in period 28 is {mortgage_b.equity(28)}')






    logging.info('\n***Program Complete***')


if __name__ == '__main__':
    main()