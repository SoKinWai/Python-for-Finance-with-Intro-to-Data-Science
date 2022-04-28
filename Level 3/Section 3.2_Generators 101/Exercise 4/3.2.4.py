#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.4


#Fibonacci sequence generator function.
def Fibonacci():

    #Set up num to be -1 to yield the first two numbers of Fibonacci sequence
    num=-1

    #a and b will be using to calculate Fibonacci sequence in the following
    a=0
    b=1

    while True:
        num=num+1
        # Set up the first integer to be 0 in Fibonacci sequence
        if num==0:
            yield 0
        # Set up the second integer to be 1 in Fibonacci sequence
        elif num==1:
            yield 1
        else:
            # temp is to store the addition from the previous two integers, then yield the temp
            temp = a + b
            a = b
            b = temp
            yield temp








def main():
    # Code goes here
    print('\n==========Exercise 3.2.4==========')

    print('\n------Testing block 1-----')
    print('Display the first and second values of the Fibonacci sequence:')

    #Display the first and second values of the Fibonacci sequence.
    x=Fibonacci()

    print('The first value of the Fibonacci sequence:',next(x))
    print('The second value of the Fibonacci sequence:',next(x))

    print('\n------Testing block 2-----')
    print('Display the next 100 values of the sequence.:')
    #Iterate through and display the next 100 values of the sequence
    for i in range(100):
        print('Number',i+1,'is ',next(x))







    print('\n***Program Complete***')


if __name__ == '__main__':
    main()