#Student Name: Jianwei Su
#Date: 04/18/2022
#3.1.2

#import necessary functions and classes
from functools import reduce
from operator import add
import string
import random
# Import LoanPool from loan_pool
from loan.loan_pool import LoanPool

#Import Loan from loan_base
from loan.loan_base import Loan
from asset.asset import *

#Mortgage() function
#This function returns a dict of address keys and the following tuple as address:(amount,rate,term)
def Mortgage():
    #amount=[
    # random.randint(100000, 1000000) for a in range(100)]
    return {''.join(random.choices(string.ascii_uppercase + string.digits, k=6)):(random.randint(100000, 1000000), round(random.uniform(0, 1),4),random.randint(120, 360)) for i in range(100)}

#This WAR_test() function is the original WAR() function. It's to compare the result of WAR() function via using reduce function.
def WAR_test(loans):
    total_amount=0
    weighted_rate=0
    for amount,rate,_ in loans:
        total_amount += amount
        weighted_rate +=amount *rate
    #Here returns the Weighted Average Rate of the mortgage pool.
    return weighted_rate/total_amount


#Create an alternate version of WAR, which takes a list of mortgage tuples; for this version,
#use the reduce function, with a lambda as its callable, to calculate the WAR of the list of rates

#WAR() function via using reduce function with a lambda as its callable
def WAR(loans):
    #return reduce(lambda total,loan:total+(loan[0]*loan[1])/sum(loan[0] for loan in loans),loans,0)

    # I am showing another method because this method it is easier for me to understand how they work.
    weighted_rate = reduce(lambda total, loan: total + (loan[0] * loan[1]), loans, 0)
    total_amount = reduce(lambda total, loan: total + loan[0], loans, 0)
    return weighted_rate / total_amount



#This WAM_test() function is the original WAR() function. It's to compare the result of WAR() function via using reduce function.
def WAM_test(loans):
    total_amount = 0
    weighted_maturity = 0
    for amount,_,term in loans:
        total_amount += amount
        weighted_maturity += amount * term
    #Here returns the Weighted Average Maturity (term) of the mortgage pool
    return weighted_maturity / total_amount


#Create an alternate version of WAM, which takes a list of mortgage tuples; for this version,
#use the reduce function, with a regular function as its callable, to calculate the WAM.


#WAM() function via using regular reduce function
def WAM(loans):
    amounts=[]
    terms=[]

    for elements in loans:
        amounts.append(elements[0])
        terms.append(elements[2])

    weighted_maturity = reduce(add, [amount*term for amount,term in zip(amounts,terms)])

    #Or total_amount=sum(amounts)
    total_amount = reduce(add, amounts)

    return weighted_maturity / total_amount



'''def WAM(loans):
     #return reduce(lambda total,loan:total+(loan[0]*loan[2])/sum(loan[0] for loan in loans),loans,0)
     #I am showing another method because this method it is easier for me to understand how they work.
     weighted_maturity=reduce(lambda total,loan:total+(loan[0]*loan[2]),loans,0)
     total_amount=reduce(lambda total,loan:total+loan[0],loans,0)
     return weighted_maturity/total_amount'''


def main():
    # Code goes here
    print('\n==========Exercise 3.1.2==========')

    mortgage = Mortgage()
    print("A function that returns an unsorted list of 'address keys':(amount, rate, term in months):", mortgage, '\n')

    #Extract a list of tuple values from the dict, and sort the list by amount (descending).
    sorted_mortgage = list(sorted(mortgage.values(), reverse=True))
    print('Extract a list of tuple values from the dict, and sort the list by amount (descending):', sorted_mortgage,
          '\n')



    print('\n------Testing block 1-----')
    print('Test the WAR functions via using the WAR function with reduce function and the original WAR function:')
    # The input parameter should be a list of mortgage tuples (amount,rate,term). Print the rate percentage, rounded to the nearest hundredths.
    print("The Weighted Average Rate of the mortgage pool via using the WAR function with reduce function,the rate percentage, rounded to the nearest hundredths:",
          ('{:.2%}'.format(WAR(sorted_mortgage))))

    print("The Weighted Average Rate of the mortgage pool via using the original WAR function,the rate percentage, rounded to the nearest hundredths:",
          ('{:.2%}'.format(WAR_test(sorted_mortgage))), '\n')

    print('\n------Testing block 2-----')
    print('Test the WAM functions via using the WAM function with reduce function and the original WAM function:')
    # The input parameter should be a list of mortgage tuples (amount,rate,term).
    print("The Weighted Average Maturity (term) of the mortgage pool via using the WAM function with reduce function:", WAM(sorted_mortgage))

    print("The Weighted Average Maturity (term) of the mortgage pool via using the original WAM function:", WAM_test(sorted_mortgage), '\n')

    # Initialize loans
    asset_a = Asset(3000000)
    car_a = CarMixin(1000000)
    loan_a = Loan(200000, .05, 40,asset_a)
    loan_b = Loan(300000, .06, 42,asset_a)
    loan_c = Loan(400000, .07, 44,car_a)
    loan_d = Loan(400000, .08, 44,car_a)
    loan_e = Loan(400000, .088, 44,car_a)

    # Make those loans above as a list, then initialize this list into loan pool
    Loans = [loan_a, loan_b, loan_c, loan_d, loan_e]


    loan_pool = LoanPool(Loans)

    print('\n------Testing block 3-----')
    print('Test the WAR() function via LoanPool class with different methods:')
    print('Total the Weighted Average Rate for those 5 loans via using reduce function rounded to the nearest hundredths is:",',
          ('{:.2%}'.format(loan_pool.WAR())))

    print('Total the Weighted Average Rate for those 5 loans via using the original method rounded to the nearest hundredths is:",',
          ('{:.2%}'.format(loan_pool.WAR_original())))

    print('\n------Testing block 4-----')
    print('Test the WAM() function via LoanPool class with different methods:')
    print('Total the Weighted Average Maturity for those 5 loans via using reduce function is:', loan_pool.WAM())
    print('Total the Weighted Average Maturity for those 5 loans via using the original method is:', loan_pool.WAM_original())

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()