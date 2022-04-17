#Student Name: Jianwei Su
#Date: 04/09/2022
#2.2.5

# Import LoanPool from loan_pool
from loan.loan_pool import LoanPool

#Import Loan from loan_base
from loan.loan_base import Loan


def main():
    print('------Exercise 2.2.5------')
    print('Testing the Loan Pool class\n')

    # Initialize loans
    loan_a=Loan(200000, .05, 40,30000)
    loan_b=Loan(300000, .06, 42,20000)
    loan_c=Loan(400000, .07, 44,50000)
    loan_d=Loan(400000, .08, 44,500000)
    loan_e=Loan(400000, .088, 44,890000)

    #Make those loans above as a list, then initialize this list into loan pool
    Loans=[loan_a,loan_b,loan_c,loan_d,loan_e]



    loan_pool=LoanPool(Loans)

    print('\n------Testing block 1-----')
    print('Test the Total_principal() function via LoanPool class:')
    print('Total principal for those 5 loans is',loan_pool.Total_principal())

    print('\n------Testing block 2-----')
    print('Test the Total_balance() function via LoanPool class:')
    #input is within the term of the loan and greater than 0
    print('Total balance for those 5 loans in period 35 is', loan_pool.Total_balance(35))

    print('\n------Testing block 3-----')
    print('Test the Total_principalDue() function via LoanPool class:')
    #input is within the term of the loan and greater than 0
    print('Total principal due for those 5 loans in period 35 is', loan_pool.Total_principalDue(35))

    print('\n------Testing block 4-----')
    print('Test the Total_interestDue() function via LoanPool class:')
    #input is within the term of the loan and greater than 0
    print('Total interest due for those 5 loans in period 35 is', loan_pool.Total_interestDue(35))

    print('\n------Testing block 5-----')
    print('Test the Total_monthlyPayment() function via LoanPool class:')
    #input is within the term of the loan and greater than 0
    print('Total monthly payment for those 5 loans in period 35 is', loan_pool.Total_monthlyPayment(35))

    print('\n------Testing block 6-----')
    print('Test the active_loans() function via LoanPool class:')
    #input is within the term of the loan and greater than 0
    print('Total active loans for those 5 loans in period 35 is', loan_pool.active_loans(35))

    print('\n------Testing block 7-----')
    print('Test the WAR() function via LoanPool class:')
    print('Total the Weighted Average Rate for those 5 loans rounded to the nearest hundredths is:",', ('{:.2%}'.format(loan_pool.WAR())))

    print('\n------Testing block 8-----')
    print('Test the WAM() function via LoanPool class:')
    print('Total the Weighted Average Maturity for those 5 loans is:' ,loan_pool.WAM())








    print('\n***Program Complete***')


if __name__ == '__main__':
    main()

