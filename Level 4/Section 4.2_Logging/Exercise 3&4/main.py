#Student Name: Jianwei Su
#Date: 04/29/2022
#4.2.3 & 4.2.4


# Import necessary packages
from loan.loan_pool import *
from loan.loan_base import *
from asset.asset import *
from loan.mortgage import *
from loan.loans import *
from utils.timer import Timer
import time
import logging

def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.ERROR)
    logging.getLogger().setLevel(logging.DEBUG)


    logging.info('\n==========Exercise 4.2.3 & 4.2.4==========')

    # Initialize assets
    house = HouseBase(3000000)
    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    loan_a = Loan(3000000, 0.05, 35, asset_a)
    loan_b = Loan(1000000, 0.06, 30, car_a)
    car_b = Toyota(30000)
    autoloan_a = AutoLoan(1000000, .06, 40, car_a)
    autoloan_b = AutoLoan(30000, .04, 30, car_b)



    logging.info('------Testing block 1-----')

    logging.info('Testing  __init__ function of Loan in the base loan class(TypeError).')

    try:

        # The __int__ function will not work here because it is an incorrect Asset type
        # This will show the type error
        loan_1 = Loan(40000, .088, 44, 'asset_a')

    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')

    logging.info('\n------Testing block 2-----')
    logging.info('Testing __init__ function of Loan class(Unknown error).')

    try:
        # Initialize the loan class with a string
        loan_2 = Loan('xxx', .05, 30, house)

    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')




    logging.info('\n------Testing block 3----')
    logging.info('Test the init function from Loan base class:')

    logging.info('The asset loan information will be:')
    logging.info(f'Asset Loan‘s face value(in US dollars): {loan_a.notional}  \nAsset Loan’s annual interest rate:{loan_a.getRate()} \nAsset Loan‘s terms(in months): {loan_a.term}  \nAsset‘s initial value: {loan_a.asset.init_val}\n')

    logging.info('\nThe car loan information will be:')
    logging.info(f'Asset Loan‘s face value(in US dollars): {loan_b.notional}  \nAsset Loan’s annual interest rate:{loan_b.getRate()} \nAsset Loan‘s terms(in months): {loan_b.term}  \nAsset‘s initial value: {loan_b.asset.init_val}\n')


    logging.info('\n------Testing block 4----')
    logging.info('Test the init function from MortgageMixin class:')

    # Initialize values for different classes

    primaryhome_a=PrimaryHome(400000)
    vacayhome_a = VacationHome(500000)
    mortgage_a = FixedMortgage(400000, .05, 30, primaryhome_a)
    mortgage_b = FixedMortgage(500000, .05, 35, vacayhome_a)

    logging.info('The mortgage_a information will be:')
    logging.info(f'Mortgage‘s face value(in US dollars): {mortgage_a.notional} \nMortgage’s interest rate: {mortgage_a.getRate()} \nMortgage‘s terms(in months): {mortgage_a.term} \nMortgage‘s initial value: {mortgage_a.asset.init_val}\n')

    logging.info('\nThe mortgage_b information will be:')
    logging.info(f'Mortgage‘s face value(in US dollars): {mortgage_b.notional} \nMortgage’s interest rate: {mortgage_b.getRate()} \nMortgage‘s terms(in months): {mortgage_b.term} \nMortgage‘s initial value: {mortgage_b.asset.init_val}\n')

    logging.info('\n------Testing block 5----')
    logging.info('Test the PMI() function from MortgageMixin class:')

    try:
        logging.info(f'mortgage_b in period 36 is {mortgage_b.PMI(36)}\n')
    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')

    logging.info(f'mortgage_b in period 5 is {mortgage_b.PMI(5)}\n')

    logging.info('\n------Testing block 6----')

    logging.info('Test the recoveryValue() function from Loan Base class:')

    logging.info(f'The recovery value for autoloan_b in period 25 is {autoloan_b.recoveryValue(25)}\n')
    logging.info(f'The recovery value for autoloan_a in period 36 is {autoloan_a.recoveryValue(36)}\n')

    logging.info(f'The recovery value for mortgage_a in period 20 is  {mortgage_a.recoveryValue(20)}\n')
    logging.info(f'The recovery value for mortgage_b in period 28 is  {mortgage_b.recoveryValue(28)}\n')

    logging.info('\n------Testing block 7----')

    logging.info('Test the balance functions in normal and recursive form from Loan Base class:')
    # Turn off DEBUG logs
    logging.disable('DEBUG')

    logging.info(f'The balance for loan_a in period 20(normal form) is  {loan_a.balance(20)}\n')

    #logging.warning('This is a recursive function, so it will take a long time to run.')
    logging.info(f'The balance for loan_a in period 20(recursive form) is  {loan_a.balance_recur(20)}\n')



    logging.info('\n------Testing block 8-----')
    logging.info('Testing the timer class with using "as" and showing it in seconds')

    with Timer('timerName') as t0:
        t0.configureTimerDisplay('seconds')
        logging.info(f'The principal due for loan_a in period 22(recursive form) is  {loan_a.principalDue_recur(22)}\n')

    logging.info('\n')

    logging.info('\n------Testing block 9-----')
    logging.info('Testing the timer class with using "as" and showing it in minutes')

    with Timer('timerName') as t1:
        t1.configureTimerDisplay('minutes')
        logging.info(f'The interest due for loan_a in period 22(recursive form) is  {loan_a.interestDue_recur(22)}\n')

    logging.info('\n')

    logging.info('\n------Testing block 10-----')
    logging.info('Testing the timer class with using "as" and showing it in hours')

    with Timer('timerName') as t2:
        t2.configureTimerDisplay('hours')
        logging.info(f'The balance for loan_a in period 25(recursive form) is  {loan_a.balance_recur(25)}\n')








    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()