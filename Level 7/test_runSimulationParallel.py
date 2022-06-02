#Student Name: Jianwei Su
#Date: 05/29/2022
#Level 7



from simulation.runSimulationParallel import runMonte
from tranche.standard_tranche import StandardTranche
from tranche.tranche_base import Tranche
from tranche.structured_securities import StructuredSecurities
import logging
from asset.asset import *
from loan.mortgage import *
from loan.loans import *
from loan.loan_pool import *
from loan.loan_base import *
import csv
from doWaterfall import doWaterfall
from simulation.simulateWaterfall import simulateWaterfall


loan_name={'FixedMortgage':FixedMortgage, 'Auto Loan':AutoLoan}

asset_name={'HouseBase':HouseBase,
            'PrimaryHome':PrimaryHome,
            'VacationHome':VacationHome,
            'Car':CarMixin,
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
    logging.getLogger().setLevel(logging.INFO)

    logging.info('Test the runSimulationParallel function')

    lp = []

    file_path_a = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 7\\Loans.csv'

    # Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data to create these Loan objects
    with open(file_path_a, 'r') as fp:
        file = csv.DictReader(fp)
        for line in file:
            loanType = line.get('Loan Type')
            assetName = line.get('Asset')
            assetValue = line.get('Asset Value')
            notional = line.get('Balance')
            rate = line.get('Rate')
            term = line.get('Term')

            loan = createLoan(loanType, assetName, assetValue, notional, rate, term)
            if loan:
                lp.append(loan)

            loan_pool = LoanPool(lp)

    # Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool)
    # Specify Sequential mode.
    tranches = StructuredSecurities(loan_pool.Total_principal(), 'Sequential')

    # Add two standard tranches (class A and class B in terms of subordination)
    tranches.addTranche(0.8, 0.05, 'A')
    tranches.addTranche(0.2, 0.08, 'B')


    # Call runMonte
    # DIRR, Rating, WAL, and rate of each tranche
    logging.info('\n')
    logging.info('This is Sequential mode:')
    logging.info('The format will be (DIRR, Rating, WAL, and rate of each tranche) for each tranche:')
    logging.info('\n')
    logging.info(f'2000 simulations(tranche A and tranche B):{runMonte(loan_pool, tranches, 0.005, 2000, 20)}')

    logging.info('\n')

    # Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool)
    # Specify Pro Rata mode.
    tranches_b = StructuredSecurities(loan_pool.Total_principal(), 'Pro Rata')

    # Add two standard tranches (class A and class B in terms of subordination)
    tranches_b.addTranche(0.8, 0.05, 'A')
    tranches_b.addTranche(0.2, 0.08, 'B')

    # Call runMonte
    # DIRR, Rating, WAL, and rate of each tranche
    logging.info('\n')
    logging.info('This is Pro Rata mode:')
    logging.info('The format will be (DIRR, Rating, WAL, and rate of each tranche) for each tranche:')
    logging.info('\n')
    logging.info(f'2000 simulations(tranche A and tranche B): {runMonte(loan_pool, tranches_b, 0.005, 2000, 20)}')

    logging.info('\n')




    #The following is just for testing purpose to find the optimal number
    logging.info('\n')
    logging.info(f'try 10:{runMonte(loan_pool, tranches, 0.005, 2000, 10)}')
    logging.info(f'try 10: {runMonte(loan_pool, tranches_b, 0.005, 2000, 10)}')

    logging.info('\n')
    logging.info(f'try 5:{runMonte(loan_pool, tranches, 0.005, 2000, 5)}')
    logging.info(f'try 5: {runMonte(loan_pool, tranches_b, 0.005, 2000, 5)}')



    #5 processes is the fastest one.







if __name__ == '__main__':
    main()