#Student Name: Jianwei Su
#Date: 05/05/2022
#4.3.8


import logging




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


def createLoan(loanType, assetName,  notional, rate, term,assetValue):

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


    print('\n==========Exercise 4.3.8==========')

    #Create an empty list
    lp_a = []
    lp_b = []

    while True:
        choice = 0

        while choice not in ['1', '2','3','4']:
            choice = input('Please choose:\n(1) Add Loan\n(2) Write file and exit\n'
                           '(3) Load loan .csv file\n(4) Calculate WAR/WAM\n')

        if choice == '1':
            loanType = None
            while (loanType not in ('AutoLoan', 'FixedMortgage')):
                loanType = input('Enter loan type (AutoLoan, FixedMortgage): ')

                assetName = input('Enter asset name: ')
                assetValue = input('Enter asset value: ')
                notional = float(input('Enter loan amount: '))
                rate = float(input('Enter loan rate: '))
                term = int(input('Enter loan term: '))

                loan = createLoan(loanType, assetName, notional, rate, term,assetValue)
                if loan:
                    lp_a.append(loan)
                loan_pool = LoanPool(lp_a)

        elif choice == '2':
            filePath = input('Enter file path of the loan .csv file: ')
            writeLoansToCSV(loan_pool, filePath)
            break

        elif choice =='3':
            filePath = input('Enter file path of the loan .csv file: ')

            with open(filePath, 'r') as fp:
                cnt = 0
                for line in fp:
                    cnt += 1
                    vals = line

                    #logging.info(f'{vals}').split(',')

                    loan = createLoan(*vals)

                    if loan:
                        lp_b.append(loan)

            loan_pool = LoanPool(lp_b)

            logging.info('{0} loans loaded: '.format(cnt))

        else:
            print('WAM: {0}'.format(loan_pool.WAM()))
            print('WAR: {0}'.format(loan_pool.WAR()))



    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()