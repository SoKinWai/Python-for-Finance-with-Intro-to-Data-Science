#Student Name: Jianwei Su
#Date: 05/23/2022
#Level 7




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

      logging.info('Test the doWaterfall function for Sequential mode')

      lp=[]


      file_path_a='C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 7\\Loans.csv'

      #Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data to create these Loan objects
      with open(file_path_a,'r') as fp:
          file=csv.DictReader(fp)
          for line in file:
              loanType=line.get('Loan Type')
              assetName=line.get('Asset')
              assetValue=line.get('Asset Value')
              notional=line.get('Balance')
              rate=line.get('Rate')
              term=line.get('Term')

              loan = createLoan(loanType, assetName, assetValue, notional, rate, term)
              if loan:
                lp.append(loan)

              loan_pool=LoanPool(lp)




      #Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool)
      # Specify sequential mode.
      tranches=StructuredSecurities(loan_pool.Total_principal(),'Sequential')


      #Add two standard tranches (class A and class B in terms of subordination)
      tranches.addTranche(0.8, 0.05, 'A')
      tranches.addTranche(0.2, 0.08, 'B')



      #Call doWaterfall and save the results into two CSV files
      #one for the asset side and one for the liabilities side
      assets, liabilities, metrics = doWaterfall(loan_pool, tranches)

      logging.info(f'{metrics}')



      list_a=[]

      for line in liabilities:
          x = [item for sublist in line for item in sublist]
          list_a.append(x)

      file_path_b = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 7\\csv_file\\Liabilities_Sequential.csv'

      with open(file_path_b, 'w', newline='') as fp:
          # All the tranches’ data for a given time period should be a single row in the CSV.
          # The reserve account balance should also be in liabilities CSV, for each time period. Each time period gets its own row.
          #Note that you may need to do some clever list comprehensions and string parsing to get this to output correctly.


          line = csv.writer(fp)
          head = ['Period',
                    'Interest_due A ', 'Interest_paid A', 'Interest_shortfall A', 'Principal_paid A', 'Balance A',
                    'Interest_due B', 'Interest_paid B', 'Interest_shortfall B', 'Principal_paid B', 'Balance B',
                    'Reserve Account']
          line.writerow(head)
          line.writerows(list_a)



      file_path_c = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 7\\csv_file\\Assets_Sequential.csv'

      with open(file_path_c, 'w', newline='') as fp:
          line = csv.writer(fp)
          head = ['Period', 'Total_principalDue', 'Total_interestDue', 'Total_monthlyPayment', 'Recoveries','Total_balance']
          line.writerow(head)
          line.writerows(assets)












      logging.info('\n***Program Complete***')







if __name__ == '__main__':
    main()
