#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.8

import string
import random

#Mortgage() function
#This function returns a dict of address keys and the following tuple as address:(amount,rate,term)
def Mortgage():
    #amount=[
    # random.randint(100000, 1000000) for a in range(100)]
    return {''.join(random.choices(string.ascii_uppercase + string.digits, k=6)):(random.randint(100000, 1000000), round(random.uniform(0, 1),4),random.randint(120, 360)) for i in range(100)}

# b. Create a function that calculates the Weighted Average Rate of the mortgage pool.
#WAR() function
# The input parameter should be a list of mortgage tuples (amount,rate,term).
def WAR(loans):
    total_amount=0
    weighted_rate=0
    for amount,rate,_ in loans:
        total_amount += amount
        weighted_rate +=amount *rate
    #Here returns the Weighted Average Rate of the mortgage pool.
    return weighted_rate/total_amount

#c. Create a function that calculates the Weighted Average Maturity (term) of the mortgage pool.
#WAM() function
#The input parameter should be a list of mortgage tuples (amount,rate,term).
def WAM(loans):
    total_amount = 0
    weighted_maturity = 0
    for amount,_,term in loans:
        total_amount += amount
        weighted_maturity += amount * term
    #Here returns the Weighted Average Maturity (term) of the mortgage pool
    return weighted_maturity / total_amount


def main():
    # Code goes here
    print('\n==========Exercise 1.5.8===========')

    mortgage=Mortgage()
    print("A function that returns an unsorted list of 'address keys':(amount, rate, term in months):",mortgage,'\n')


    # a. Extract a list of tuple values from the dict, and sort the list by amount (descending).
    sorted_mortgage=list(sorted(mortgage.values(), reverse=True))
    print('Extract a list of tuple values from the dict, and sort the list by amount (descending):',sorted_mortgage,'\n')

    # The input parameter should be a list of mortgage tuples (amount,rate,term). Print the rate percentage, rounded to the nearest hundredths.
    print("The Weighted Average Rate of the mortgage pool,the rate percentage, rounded to the nearest hundredths:",('{:.2%}'.format(WAR(sorted_mortgage))),'\n')

    # The input parameter should be a list of mortgage tuples (amount,rate,term).
    print("The Weighted Average Maturity (term) of the mortgage pool:", WAM(sorted_mortgage),'\n')

    # d. Create a new dict (by processing the original dict) with Term as the key and a list of (amount, rate) tuples for each Term key.
    unsorted_mortgage=list(mortgage.values())

    #I found out 3 methods to solve this problem.

    #Method 1
    new_dict1=dict((z,(x,y)) for x,y,z in unsorted_mortgage)
    print("A new dict (by processing the original dict) with Term as the key and a list of (amount, rate) tuples for each Term key(Method 1):",new_dict1)

    #Method 2
    new_dict2={key:(values1,values2) for values1,values2,key in unsorted_mortgage}
    print("A new dict (by processing the original dict) with Term as the key and a list of (amount, rate) tuples for each Term key(Method 2):",new_dict2)

    #Method 3
    new_dict3=dict()
    for i in unsorted_mortgage:
     new_dict3[i[2]]=(i[0],i[1])
    return print("A new dict (by processing the original dict) with Term as the key and a list of (amount, rate) tuples for each Term key(Method 3):",new_dict3)




if __name__ == '__main__':
    main()