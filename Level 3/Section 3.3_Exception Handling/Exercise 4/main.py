#Student Name: Jianwei Su
#Date: 04/20/2022
#3.3.4


# Import necessary packages
from loan.loan_pool import *
from loan.loan_base import *
from asset.asset import *
from loan.mortgage import *
from loan.loans import *

def main():
    # Code goes here
    print('\n==========Exercise 3.3.4==========')

    # Initialize assets
    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    house = HouseBase(3000000)



    print('\n------Testing block 1-----')
    print('Testing  __init__ function of Loan in the base loan class(TypeError).')

    try:

        #The __int__ function will not work here because it is an incorrect Asset type
        #This will show the type error
        loan_a=Loan(40000, .088, 44, 'asset_a')

    except TypeError as ex:
        print('TypeError exception:',ex,'\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a TypeError and NameError:', ex, '\nPlease try again.')




    print('\n------Testing block 2-----')
    print('Testing  __init__ function of Loan in the base loan class(NameError).')

    try:
        # The __int__ function will not work here because it is an incorrect Asset type
        # This will show the name error
        loan_b=Loan(45555, .088, 44,efewfwf)

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a ValueError and NameError:', ex, '\nPlease try again.')




    print('\n------Testing block 3-----')
    print('Testing  __init__ function of FixedMortgage(TypeError).')

    try:
        # The __int__ function will not work here because it is an incorrect Asset type
        # This will show the value error
        mortgage_a = FixedMortgage(400000, .05, 30, car_a)

    except TypeError as ex:
        print('TypeError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a TypeError and NameError:', ex, '\nPlease try again.')


    print('\n------Testing block 4-----')
    print('Testing  __init__ function of AutoLoan(TypeError).')

    try:
        # The __int__ function will not work here because it is an incorrect Asset type
        # This will show the value error
        auto_a = AutoLoan(400000, .05, 30, house)

    except TypeError as ex:
        print('TypeError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a TypeError and NameError:', ex, '\nPlease try again.')



    #Let's test other exceptions from those classes below.

    print('\n------Testing block 5-----')
    print('Testing  __init__ function of Loan class(Name Error).')

    try:
        # The __int__ function will not work here because it is an incorrect Loan type
        # This will show the name error
        loan_c = Loan(wdqdwq, .05, 30, house)

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a ValueError and NameError:', ex, '\nPlease try again.')


    print('\n------Testing block 6-----')
    print('Testing  __init__ function of Loan class(Value Error).')

    try:
        # Initialize the loan class with negative input
        loan_d = Loan(-500000, .05, 30, house)


    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a ValueError and NameError:', ex, '\nPlease try again.')



    print('\n------Testing block 7-----')
    print('Testing __init__ function of Loan class(Unknown error).')

    try:
        # Initialize the loan class with a string
        loan_e = Loan('xxx', .05, 30, house)


    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a ValueError and NameError:', ex, '\nPlease try again.')


    print('\n------Testing block 8-----')
    print('Testing  PMI() of MortgageMixin class(Value Error).')

    try:
        mortgage_b = FixedMortgage(100000, .050, 25, house)

        # The function will not work here because the period is greater than term.
        print(mortgage_b.PMI(30))

    except ValueError as ex:
        print('ValueError exception:', ex, '\nPlease try again.')

    except NameError as ex:
        print('NameError exception:', ex, '\nPlease try again.')

    except Exception as ex:
        print('Unknown error besides a ValueError and NameError:', ex, '\nPlease try again.')






    print('\n***Program Complete***')

if __name__ == '__main__':
    main()