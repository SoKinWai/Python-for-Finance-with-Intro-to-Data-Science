#Student Name: Jianwei Su
#Date: 04/08/2022
#2.1.3

# Importing necessary packages

from Timer_and_Loan.loan import Loan
from Timer_and_Loan.timer import Timer

def main():
    # Test Loan class thoroughly.

    print('------Exercise 2.1.3------')
    print('Testing the Loan class\n')

    # Initialize loan_1 with Loan class
    loan_1=Loan(200000,0.05, 24)
    print('The loan information will be:')
    print('Loan‘s face value(in US dollars):',loan_1.notional,'\nLoan’s annual interest rate:',loan_1.rate,'\nLoan‘s terms(in months):',loan_1.term)

    # Test the balance() and balance_recur() functions.
    # Use the balance()  and balance_recur() to calculate the balance
    # Use the timer to see which function is faster.
    print('\n------Testing block 1-----')
    print('Test balance functions in normal and recursive forms:\n')

    #The balance here should be equal to the face value because at time period 0, it means interst and principal have not been paid.
    print('Test the balance function in normal form:')
    print('The balance in time period 0 will be(normal form):', loan_1.balance(0))
    print('Test the balance function in recursive form:')
    print('The balance in time period 0 will be(recursive form):', loan_1.balance_recur(0))


    # Test the balance() and balance_recur() functions.
    # Use the balance()  and balance_recur() to calculate the balance
    # Use the timer to see which function is faster.
    print('\n------Testing block 2-----')
    print('Test balance functions in normal and recursive forms:\n')

    #Use the timer here and set 'seconds' to show on screen
    t1 = Timer('seconds')
    print('Test the balance function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The balance in time period 15 will be(normal form):',loan_1.balance(15))
    t1.end()# This should stop the timer and print the time taken

    print('\n')

    print('Test the balance function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The balance in time period 15 will be(recursive form):',loan_1.balance_recur(15))
    t1.end()# This should stop the timer and print the time taken

    # Test the interestDue() and interestDue_recur() functions.
    # Use the interestDue()  and interestDue_recur() to calculate the interest due.
    # Use the timer to see which function is faster.
    print('\n------Testing block 3-----')
    print('Test interest due functions in normal and recursive forms:\n')

    print('Test the interest due function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The interest due function in time period 15 will be(normal form):', loan_1.interestDue(15))
    t1.end()# This should stop the timer and print the time taken

    print('\n')

    print('Test the interest due function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The interest due in time period 15 will be(recursive form):', loan_1.interestDue_recur(15))
    t1.end()# This should stop the timer and print the time taken

    # Test the principalDue() and principalDue_recur() functions.
    # Use the principalDue()  and principalDue_recur() to calculate the principal due.
    # Use the timer to see which function is faster.
    print('\n------Testing block 4-----')
    print('Test principal due functions in normal and recursive forms:\n')

    print('Test the principal due function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The principal due function in time period 15 will be(normal form):', loan_1.principalDue(15))
    t1.end()# This should stop the timer and print the time taken

    print('\n')

    print('Test the principal due function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The principal due in time period 15 will be(recursive form):', loan_1.principalDue_recur(15))
    t1.end()# This should stop the timer and print the time taken


    #Increase the time period to 22 and let's see what will happen in the following:

    # Test the balance() and balance_recur() functions.
    # Use the balance()  and balance_recur() to calculate the balance
    # Use the timer to see which function is faster.
    print('\n------Testing block 5-----')
    print('Test balance functions in normal and recursive forms:\n')

    # Use the timer here and set 'seconds' to show on screen
    t1 = Timer('seconds')
    print('Test the balance function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The balance in time period 22 will be(normal form):', loan_1.balance(22))
    t1.end()  # This should stop the timer and print the time taken

    print('\n')

    print('Test the balance function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The balance in time period 22 will be(recursive form):', loan_1.balance_recur(22))
    t1.end()  # This should stop the timer and print the time taken

    # Test the interestDue() and interestDue_recur() functions.
    # Use the interestDue()  and interestDue_recur() to calculate the interest due.
    # Use the timer to see which function is faster.
    print('\n------Testing block 6-----')
    print('Test interest due functions in normal and recursive forms:\n')

    print('Test the interest due function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The interest due function in time period 22 will be(normal form):', loan_1.interestDue(22))
    t1.end()  # This should stop the timer and print the time taken

    print('\n')

    print('Test the interest due function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The interest due in time period 22 will be(recursive form):', loan_1.interestDue_recur(22))
    t1.end()  # This should stop the timer and print the time taken

    # Test the principalDue() and principalDue_recur() functions.
    # Use the principalDue()  and principalDue_recur() to calculate the principal due.
    # Use the timer to see which function is faster.
    print('\n------Testing block 7-----')
    print('Test principal due functions in normal and recursive forms:\n')

    print('Test the principal due function in normal form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The principal due function in time period 22 will be(normal form):', loan_1.principalDue(22))
    t1.end()  # This should stop the timer and print the time taken

    print('\n')

    print('Test the principal due function in recursive form:')
    t1.start()

    #input is within the term of the loan and greater than 0
    print('The principal due in time period 22 will be(recursive form):', loan_1.principalDue_recur(22))
    t1.end()  # This should stop the timer and print the time taken

    #what do you observe?
    #For interestDue(), balance() and principalDue(), they took 0s to get the results.
    #But for interestDue_recur(),principalDue_recur() and balance_recur(), they took longer time to get the same results compared to the direct normal functions.

    #What happens as the time period increases?
    #When I increased time period 15 to 22, the direct normal form functions of balance(), interestDue() and principalDue() still took
    #0 seconds to get the results. However, for interestDue_recur(), balance_recur() and principalDue(), they would take more time when I increased time period 15 to 22.

    #Test functions with periods greater than terms and less than 0
    print('\n------Testing block 8-----')
    print('functions with periods greater than terms and less than 0:\n')
    print('Test the balance function in normal form(period=-1):')
    print('The balance in time period 0 will be(normal form):', loan_1.balance(-1))
    print('Test the balance function in recursive form(period=-1):')
    print('The balance in time period 0 will be(recursive form):', loan_1.balance_recur(-1))

    print('\n')
    print('Test the balance function in normal form(period=50):')
    print('The balance in time period 0 will be(normal form):', loan_1.balance(50))
    print('Test the balance function in recursive form(period=50):')
    print('The balance in time period 0 will be(recursive form):', loan_1.balance_recur(50))

    #principalDue() and interestDue() functions in normal and recursive forms should be the same as above when the period is less than 0 and
    #greater than term of the loan.







    print('\n***Program Complete***')


if __name__ == '__main__':
    main()