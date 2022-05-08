#Student Name: Jianwei Su
#Date: 05/04/2022
#4.3.7


import logging
from asset.asset import *
from loan.mortgage import *
from loan.loans import *
from loan.loan_pool import *


loan_name={'FixedMortgage':FixedMortgage, 'AutoLoan':AutoLoan}

asset_name={'HouseBase':HouseBase,
            'PrimaryHome':PrimaryHome,
            'VacationHome':VacationHome,
            'CarMixin':CarMixin,
            'Toyota':Toyota,
            'Civic':Civic,
            'Lexus':Lexus,
            'Lamborghini':Lamborghini}


def createLoan(loanType, assetName, assetValue, notional, rate, term):

    assetCls = asset_name.get(assetName)

    if assetCls:
        asset = assetCls(float(assetValue))

    else:
        logging.error('Invalid asset type entered.')

    loanCls = loan_name.get(loanType)

    if loanCls:
        loan = loanCls(float(notional), float(rate), int(term), asset)

        return loan
    else:
        logging.error('Invalid loan type entered.')



def writeLoansToCSV(loanPool, filename):
    lines = []
    for loan in loanPool:
        lines.append(','.join([loan.__class__.__name__, loan.asset.__class__.__name__,
         str(loan.notional), str(loan.rate), str(loan.term),str(loan.asset.init_val)]))

    outputString = '\n'.join(lines)

    with open(filename, 'w') as fp:
     fp.write(outputString)



def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)


    print('\n==========Exercise 4.3.7==========')

    #Create an empty list
    lp = []

    while True:
        choice = 0

        while choice not in ['1', '2']:
            choice = input('Please choose:\n(1) Add Loan\n(2) Write file and exit   \n')

        if choice == '1':
                loanType = None
                while (loanType not in ('AutoLoan', 'FixedMortgage')):
                    loanType = input('Enter loan type (AutoLoan, FixedMortgage): ')

                    assetName = input('Enter asset name: ')
                    assetValue = input('Enter asset value: ')
                    notional = float(input('Enter loan amount: '))
                    rate = float(input('Enter loan rate: '))
                    term = int(input('Enter loan term: '))

                    loan = createLoan(loanType, assetName, assetValue, notional, rate, term)
                    if loan:
                        lp.append(loan)
                    loan_pool = LoanPool(lp)


        elif choice == '2':
                filePath = input('Enter file path of the loan .csv file: ')
                writeLoansToCSV(loan_pool, filePath)
                break





    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()