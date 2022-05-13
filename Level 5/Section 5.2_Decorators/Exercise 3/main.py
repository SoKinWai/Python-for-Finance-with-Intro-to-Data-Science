#Student Name: Jianwei Su
#Date: 05/11/2022
#5.2.3


import logging
import time
from utils.timer import Timer
from utils.timer import timer
from functools import wraps
from asset.asset import *
from loan.loan_base import *
from loan.mortgage import *
from loan.loans import *
import datetime



#Create a decorator that memoize’s the result of a function.
def memoize(f): #memoize function

    #Note that memoizing should happen on a per-parameter basis
    # This cache dict is to store every result
    cache_dict = {}

    #Nesting function
    @wraps(f) # Decorator that decorates the wrapped function to retain the representation of the function
    def wrapped(*args, **kwargs):  # Take all keyword and non-keyword parameters

        #Set the cache key
        cache_key=str(args)+str(kwargs)

        if cache_key not in cache_dict:
            cache_dict[cache_key]=f(*args, **kwargs)
        return cache_dict[cache_key]

    return wrapped


@memoize
@timer
def principalDue_a(loan,period):
    return loan.principalDue_recur(period)


@timer
def principalDue_b(loan,period):
    return loan.principalDue_recur(period)

@memoize
@timer
def interestDue_recur_a(loan,period):
    return loan.interestDue_recur(period)

@timer
def interestDue_recur_b(loan,period):
    return loan.interestDue_recur(period)

@memoize
@timer
def balance_recur_a(loan,period):
    return loan.balance_recur(period)

@timer
def balance_recur_b(loan,period):
    return loan.balance_recur(period)





def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.2.3=========')

    # Initialize values for different classes
    d1 = '2012-12-28 14:24:12:123456'
    d2 = '2016-09-25 18:23:14:012342'

    date_1 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S:%f')

    date_2 = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M:%S:%f')

    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    loan_a = Loan(3000000, 0.05, date_1, date_2, asset_a)
    loan_b = Loan(1000000, 0.06, date_1, date_2, car_a)

    logging.info(f'Asset Loan‘s terms( in months): {loan_a.term()}')

    logging.info('\n')

    logging.info('\n------Testing block 1-----')
    logging.info('\nTesting the principalDue(loan_a & loan_b) recursive function in memoized and normal way:')

    logging.info('Memoized way(loan_a,period=20):')
    logging.info(f'{principalDue_a(loan_a, 20)}')

    logging.info('\n')

    logging.info('Normal way(loan_a,period=20):')
    logging.info(f'{principalDue_b(loan_a, 20)}')

    logging.info('\n')

    logging.info('Memoized way(loan_b,period=25):')
    logging.info(f'{principalDue_a(loan_b, 25)}')

    logging.info('\n')

    logging.info('Normal way(loan_b,period=25):')
    logging.info(f'{principalDue_b(loan_b, 25)}')

    logging.info('\n')

    logging.info('\n------Testing block 2-----')
    logging.info('\nTesting the interestDue_recur(loan_a & loan_b) recursive function in memoized and normal way:')

    logging.info('Memoized way(loan_a,period=20):')
    logging.info(f'{interestDue_recur_a(loan_a, 20)}')

    logging.info('\n')

    logging.info('Normal way(loan_a,period=20):')
    logging.info(f'{interestDue_recur_b(loan_a, 20)}')

    logging.info('\n')

    logging.info('Memoized way(loan_b,period=25):')
    logging.info(f'{interestDue_recur_a(loan_b, 25)}')

    logging.info('\n')

    logging.info('Normal way(loan_b,period=25):')
    logging.info(f'{interestDue_recur_b(loan_b, 25)}')

    logging.info('\n')

    logging.info('\n------Testing block 3-----')
    logging.info('\nTesting the balance_recur(loan_a & loan_b) recursive function in memoized and normal way:')

    logging.info('Memoized way(loan_a,period=20):')
    logging.info(f'{balance_recur_a(loan_a, 20)}')

    logging.info('\n')

    logging.info('Normal way(loan_a,period=20):')
    logging.info(f'{balance_recur_b(loan_a, 20)}')

    logging.info('\n')

    logging.info('Memoized way(loan_b,period=25):')
    logging.info(f'{balance_recur_a(loan_b, 25)}')

    logging.info('\n')

    logging.info('Normal way(loan_b,period=25):')
    logging.info(f'{balance_recur_b(loan_b, 25)}')

    #Do you see a difference?
    #I chose large numbers to see the differences.
    #Memoied ways are faster than normal recursive ways.




    logging.info('\n***Program Complete***')



if __name__ == '__main__':
    main()