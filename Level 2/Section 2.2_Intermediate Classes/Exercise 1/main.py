#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.1

#Import necessary packages
from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan


def main():
    # Test Asset class thoroughly.
    print('------Exercise 2.2.1------')
    print('Testing the FixedRateLoan and VariableRateLoan classes\n')

    print('\n------Testing block 1-----')
    print('Test the FixedRateLoan class: ')

    # Initialize loan with FixedRateLoan class
    loan=FixedRateLoan(200000, 0.05, 24)

    print('The fixed rate for this loan will be:',loan.getRate())

    print('\n------Testing block 2-----')
    print('Test the VariableRateLoan class with a rate dictionary: ')

    #Create a rate dictionary, time periods will be the keys
    rate_dict={0:0.05, 4:0.07, 6:0.08, 9:0.015, 15:0.022}

    # Initialize loan with VariableRateLoan class
    loan_2=VariableRateLoan(200000,rate_dict,24)

    #Time periods will be the keys
    print('The annual rate dictionary for this loan will be:',loan_2.rate)

    print('\n------Testing block 3-----')
    print('Test the VariableRateLoan class with just a single rate: ')

    # Initialize loan with VariableRateLoan class
    loan_3 = VariableRateLoan(200000, 0.05, 24)

    try:
        #It will give an error
        print('The annual rate for this loan will be:', loan_3.rate)
    except Exception as ex:
        print(ex)

    print('\nTry the VariableRateLoan class with just a single .getRate():')
    try:
        #There will be an error if we use loan_3.getRate()
        print(loan_3.getRate(2))
    except Exception as ex:
        print('Error:',ex)



    print('\n------Testing block 4-----')
    print('Test the VariableRateLoan class via using getRate() function with a period which is greater than all dict‘s periods: ')

    #It should show time period 15's annual rate.
    print('The annual rate for this loan will be(period=30):', loan_2.getRate(30))

    print('\n------Testing block 5-----')
    print('Test the VariableRateLoan class via using getRate() function with a period which is among the dict‘s periods: ')

    # It should show time period 9's annual rate.
    print('The annual rate for this loan will be(period=14):', loan_2.getRate(14))

    print('\n------Testing block 6-----')
    print('Test the VariableRateLoan class via using getRate() function with a period which is smaller than all dict‘s periods: ')

    # It should show time period 0's annual rate.
    # period equals to -1 is just for the purpose to test the function
    print('The annual rate for this loan will be(period=-1):', loan_2.getRate(-1))



    print('\n***Program Complete***')







if __name__ == '__main__':
    main()