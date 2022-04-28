#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.5

# Import necessary packages
# Import the Timer class from utils
from utils.timer import Timer


def main():
    # Code goes here
    print('\n==========Exercise 3.2.5==========')

    #Create a list comprehension that contains the square of all numbers from 0-5,000,000
    list_a=[x**2 for x in range(5000001)]

    print('\n------Testing block 1-----')
    print('Display the length of list_a and check the first 5 numbers of list_a:')
    print('The length of list_a is:',len(list_a))
    print('The first 5 numbers of list_a is:',list_a[0:5])

    #Sum this using the built-in sum function
    print('\n------Testing block 2-----')
    print('Display the sum of list_a using the built-in sum function via using list comprehension:')
    print('The sum of list_a is:', sum(list_a))


    #Compare the total time taken to build and sum each via using generator expression and list comprehension
    print('\n------Testing block 3-----')
    print('Display the total time taken of the sum of the square of all numbers from 0-5,000,000 using generator expression:')

    #Instantiate t1 with Timer class
    t1 = Timer()
    t1.start()
    sum_a_gen=sum(x**2 for x in range(5000001))
    print('The sum of the square of all numbers from 0-5,000,000 using generator expression is:',sum_a_gen)
    t1.end()

    print('\n------Testing block 4-----')
    print('Display the total time taken of the sum of the square of all numbers from 0-5,000,000 using list comprehension:')

    # Instantiate t2 with Timer class
    t2 = Timer()
    t2.start()
    sum_list_a = sum([x ** 2 for x in range(5000001)])
    print('The sum of the square of all numbers from 0-5,000,000 using list comprehension is:', sum_list_a)
    t2.end()

    #Compare the total time taken to build and sum each. Which one is faster? What are the
    # benefits of using the generator instead of the list comprehension? Why?

    #For this question, list comprehension is faster, but I think when dealing with very large numbers, using the generator should be
    #faster. Because it can be much more efficient than using list comprehensions. It saves a computational step, as a list comprehension
    #requires creating an entire list into the function, and performing the operation. Whereas, the generator will only first be evaluated as
    #and when it's needed. It also saves memory(no need to pass around large lists).

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()