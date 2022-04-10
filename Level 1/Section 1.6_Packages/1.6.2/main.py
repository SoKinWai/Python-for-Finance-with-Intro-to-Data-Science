#Student name: Jianwei Su
#Date: 04/06/2022
#1.6.2



from Sub_a.Hello_world import Hello_world
from Sub_a.subsub_1.Fibonacci_iterative import Fibonacci_iterative
from Sub_a.subsub_2.Fibonacci_recursive import Fibonacci_recursive
from Sub_b.Mortgage_amounts import Mortgage_amounts
from Sub_b.subsub_1.freqMap import freqMap
import Sub_a.subsub_1.week_day_function.week_day_function
#from Sub_a.subsub_1.week_day_function.week_day_function import week_day_function
from Sub_a.subsub_2.mean_of_list_function.mean_of_list_function import Average
import Sub_b.subsub_1.mode.mode as mode
from Sub_b.subsub_2.function import function
from Sub_b.subsub_2.argsMean_function.argsMean import argsMean

def main():

    #Code goes here
    print('\n==========Exercise 1.6.2===========')

    print('Testing Hello_world function:')
    Hello_world()
    print('\n')

    # Iterative
    print('Fibonacci function using Iterative:')
    print(Fibonacci_iterative(1))
    print(Fibonacci_iterative(2))
    print(Fibonacci_iterative(3))
    print('\n')

    # Recursive
    print('Fibonacci function using Recursive:')
    print(Fibonacci_recursive(1))
    print(Fibonacci_recursive(2))
    print(Fibonacci_recursive(3))
    print(Fibonacci_recursive(5))
    print('\n')



    #I.e. Sunday is 1, Monday is 2, etc. It should return a tuple of the original number and the corresponding name of the day.
    print('Testing week_day_function function:')
    Sub_a.subsub_1.week_day_function.week_day_function.week_day_function(6)
    #week_day_function(6)
    print('\n')

    #mean of a list
    print('Testing mean of a list function:')
    l = [1, 3, 4, 50]
    Average(l)
    print('\n')

    print('Testing Mortgage_amounts function:')
    mortgage_amounts = Mortgage_amounts()
    print("A function that returns an unsorted list of mortgage amounts,range from 100 to 1000:", mortgage_amounts)
    print('\n')

    print('Testing freqMap function:')
    my_list = [1, 1, 2, 2, 3, 4, 5]
    print("Frequency of each number:", freqMap(my_list))
    print('\n')

    #Mode
    print('Testing mode function:')
    print(mode.mode())
    print('\n')

    print('Testing the function with names, ages, and different combinations of keyword arguments (state, height, weight, hairColor, etc.):')
    function('Adam', 23, State='Iowa', Height=69)
    function('Tim', 22, HairColor='Yellow')
    print('\n')

    #argsMean
    # Pass a tuple
    print('Testing argsMean function via passing a tuple:')
    l_1 = (1.3, 4.5, 6.7, 11.2, 100, 987.6)
    print("Pass a tuple:", argsMean(*l_1))
    print('\n')


    # Pass a list
    print('Testing argsMean function via passing a list:')
    l_2 = [1.3, 4.5, 6.7, 11.2, 100, 987.6]
    print("Pass a list:", argsMean(*l_2))

    print('\n')

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()