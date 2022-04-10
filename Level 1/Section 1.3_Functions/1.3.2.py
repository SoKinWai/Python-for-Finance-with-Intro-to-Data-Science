#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.2


#This is the iterative function for Fibonacci sequence.
def Fibonacci_iterative(N):
    # return Fibonacci series up to N
    #Set up res to be an empty list here to store the integers as the Fibonacci list
    res = []
    a=0
    b=1

    #Integers input from the user have to greater than 0
    if N<=0:
     print("Please enter a positive integer")

    #Set up the first integer to be 0 in Fibonacci sequence list when the input from the user is 1
    elif N==1:
     return([0])

    #When integers input greater than 1, do the following
    else:
        res.append(a)
        res.append(b)

        #When the length of the list is not equal to the integer from input
        while len(res) != N:
            #temp is to store the addition from the previous two integers, then append the temp to the list
            temp = a + b
            res.append(temp)
            a = b
            b = temp

        return(res)



def Fibonacci_recursive(N):
    # Set up res to be a list here to store the first two integers from the Fibonacci list
    res = [0, 1]

    #Integers input from the user have to greater than 0
    if N <= 0:
        print("Please enter a positive integer")

    # Set up the first integer to be 0 in Fibonacci sequence list when the input from the user is 1
    elif N == 1:
        return([0])

    else:
    #range(2,N) means all integers from 2 to N-1
    #res.append(res[i - 1] + res[i - 2]) means to append the previous two numbers' addition to the res list as the Fibonacci list
     for i in range(2, N):
        res.append(res[i - 1] + res[i - 2])
     return (res)



def main():
    # Code goes here
    print('\n==========Exercise 1.3.2===========')

    #Iterative
    print('---Iteratuve---')
    print('Fibonacci iterative for 1:',Fibonacci_iterative(1))
    print('Fibonacci iterative for 2:',Fibonacci_iterative(2))
    print('Fibonacci iterative for 3:',Fibonacci_iterative(3))
    print('Fibonacci iterative for 5:', Fibonacci_iterative(5))
    print('Fibonacci iterative for 6:', Fibonacci_iterative(6))

    #Recursive
    print('\n---Recursive---')
    print('Fibonacci recursive for 1:',Fibonacci_recursive(1))
    print('Fibonacci recursive for 2:',Fibonacci_recursive(2))
    print('Fibonacci recursive for 3:',Fibonacci_recursive(3))
    print('Fibonacci recursive for 5:',Fibonacci_recursive(5))
    print('Fibonacci recursive for 6:', Fibonacci_recursive(6))

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()



