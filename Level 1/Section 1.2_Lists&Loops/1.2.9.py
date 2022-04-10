#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.9

#Time module provides us with various functions to inculcate the system time
import time

def main():
    # Code goes here
    print('\n==========Exercise 1.2.9===========')

    #Write a list comprehension that results in a list of all numbers 0 through 10,000,000
    #range(10000001) means all integers from 0 through 10,000,000
    list_a = [i for i in range(10000001)]

    #start=time.time() is to count the starting time of the process
    start = time.time()
    list_b=[]
    # a.Using a loop, filter the resulting list, to create another list that only contains numbers ending with the digit 0
    # iterating each number in list
    # if i%10==0 wil have the same answer, but not i%10 is considered cleaner syntax than i%10 == 0
    for num in list_a:
        # checking condition
        if not num % 10:
            list_b.append(num)

    #Check if the list only contains numbers ending with the digit 0
    #print(list_b)

    #end=time.time() is to count the end time of this process
    end = time.time()
    # str(end-start) is to calculate the time it takes for this process.
    print('Seconds using a loop', str(end - start))

    start=time.time()
    #b.Do the same as a) using a list comprehension
    # if i%10==0 wil have the same answer, but not i%10 is considered cleaner syntax than i%10 == 0
    list_c=[i for i in list_a if not i%10]

    # Check if the list only contains numbers ending with the digit 0
    # print(list_c)

    end = time.time()
    print('Seconds using a list comprehension:', str(end - start))

    #Which is quicker?Why?
    #b is quicker.
    #List comprehensions is faster because they do not need to call the append function at each iteration.

    print('\n***Program Complete***')






if __name__ == '__main__':
    main()