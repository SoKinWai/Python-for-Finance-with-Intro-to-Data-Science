#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.2 and 2.2.3

# Import necessary packages
from loan.mortgage import FixedMortgage,MortgageMixin,VariableMortgage



def main():

    print('------Exercise 2.2.2 & 2.2.3------')
    print('Testing the FixedMortgage and VariableMortgage classes\n')
    #The MortgageMixin class is not really meant to be a stand-alone class which you can initialize objects from.
    #It instead serves as a way to add the PMI functionality to the loan class through the derived
    #FixedMortgage and VariableMortgage classes
    #mortgage1 = MortgageMixin(100000, .050, 25, 100000) #It will give an error

    print('\n------Testing block 1-----')
    print('Test the FixedMortgage class:')

    # Initialize mortgage1 with FixedMortgage class
    mortgage1 = FixedMortgage(100000, .050, 25, 100000)
    print('The mortgage information will be:')
    print('Loan‘s face value(in US dollars):',mortgage1.notional,'\nLoan’s annual interest rate:',mortgage1.getRate(),'\nLoan‘s terms(in months):',
          mortgage1.term,'\nAsset‘s value:',mortgage1.asset)


    print('\n------Testing block 2-----')
    print('Testing MortgageMixin.PMI() of FixedMortgage:\n')

    #Try different time periods
    print('The PMI value for mortgage1 is in time period 3:',mortgage1.PMI(3))
    print('The PMI value for mortgage1 is in time period 5:',mortgage1.PMI(5))
    print('The PMI value for mortgage1 is in time period 6:',mortgage1.PMI(6))
    print('The PMI value for mortgage1 is in time period 27:', mortgage1.PMI(27))

    print('\n------Testing block 3-----')
    print('Testing MortgageMixin.monthlyPayment() of FixedMortgage:\n')

    # Try different time periods
    print('The monthly payment for mortgage1 in time period 3 is:', mortgage1.monthlyPayment(3))
    print('The monthly payment for mortgage1 in time period 8 is:', mortgage1.monthlyPayment(8))
    print('The monthly payment for mortgage1 in time period 11 is:', mortgage1.monthlyPayment(11))
    print('The monthly payment for mortgage1 in time period 27 is:', mortgage1.monthlyPayment(27))


    print('\n------Testing block 4-----')
    print('Testing MortgageMixin.principalDue() of FixedMortgage:\n')

    # Try different time periods
    print('The principal due for mortgage1 in time period 3 is:', mortgage1.principalDue(3))
    print('The principal due for mortgage1 in time period 8 is:', mortgage1.principalDue(8))
    print('The principal due for mortgage1 in time period 27 is:', mortgage1.principalDue(27))

    print('\n------Testing block 5-----')
    print('Testing MortgageMixin.principalDue_recur() of FixedMortgage:\n')


    # Try different time periods
    print('The principal due for mortgage1 in time period 3 is:', mortgage1.principalDue_recur(3))
    print('The principal due for mortgage1 in time period 8 is:', mortgage1.principalDue_recur(8))
    print('The principal due for mortgage1 in time period 27 is:', mortgage1.principalDue_recur(27))




    print('\n------Testing block 6-----')
    print('Test the init function of MortgageMixin via VariableMortgage')



    # Initialize mortgage with VariableMortgage class
    mortgage2 = VariableMortgage(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30, 100000)


    # Time periods will be the keys
    print('The annual rate dictionary for this mortgage2 will be:', mortgage2.rate)

    print('\n------Testing block 7-----')
    print('Test the VariableMortgage.getRate() function of VariableMortgage')


    print('The annual mortgage2’s rate at time period 22 will be:', mortgage2.getRate(28))

    print('\n------Testing block 8-----')
    print('Test MortgageMixin.PMI() function of VariableMortgage:')

    # Try different time periods
    print('The PMI value for mortgage2 is in time period 20:', mortgage2.PMI(20))
    print('The PMI value for mortgage2 is in time period 5:', mortgage2.PMI(5))
    print('The PMI value for mortgage2 is in time period 6:', mortgage2.PMI(6))

    print('\n------Testing block 9-----')
    print('Testing MortgageMixin.monthlyPayment() of VariableMortgage:\n')

    # Try different time periods
    print('The monthly payment for mortgage2 in time period 3 is:', mortgage2.monthlyPayment(5))
    print('The monthly payment for mortgage2 in time period 8 is:', mortgage2.monthlyPayment(8))
    print('The monthly payment for mortgage2 in time period 11 is:', mortgage2.monthlyPayment(11))

    print('\n------Testing block 10-----')
    print('Testing MortgageMixin.principalDue() of VariableMortgage:\n')

    # Try different time periods
    print('The principal due for mortgage2 in time period 3 is:', mortgage2.principalDue(3))
    print('The principal due for mortgage2 in time period 8 is:', mortgage2.principalDue(8))
    print('The principal due for mortgage2 in time period 11 is:', mortgage2.principalDue(11))

    print('\n------Testing block 11-----')
    print('Testing MortgageMixin.principalDue_recur() of VariableMortgage:\n')
    print('The principal due for mortgage2 in time period 3 is:', mortgage2.principalDue_recur(3))
    print('The principal due for mortgage2 in time period 8 is:', mortgage2.principalDue_recur(8))
    print('The principal due for mortgage2 in time period 11 is:', mortgage2.principalDue_recur(11))

    print('\n***Program Complete***')








if __name__ == '__main__':
    main()