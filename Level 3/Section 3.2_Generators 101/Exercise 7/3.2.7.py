#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.7



def main():
    # Code goes here
    print('\n==========Exercise 3.2.7==========')

    #Create three generator expressions with different lengths
    A=[i for i in range(10)]
    B=[x**2 for x in range(3)]
    C=[a**3 for a in range((5))]



    #Zip three generator expressions together.
    Together_a=zip(A,B,C)

    #Create other three generator expressions with same length.
    D = [i for i in range(5)]
    E = [x ** 2 for x in range(5)]
    F = [a ** 3 for a in range((5))]

    # Zip three generator expressions together.
    Together_b = zip(D, E, F)


    print('\n------Testing block 1-----')
    print('Display three generator expressions:')
    print('Generator A:',A)
    print('Generator B:',B)
    print('Generator C:',C)

    print('\n------Testing block 2-----')
    print('Display the list after zip A,B and C together(List A, B and C have different lengths):')
    #Print out the result as a list.
    print('The list after zip A,B and C:',list(Together_a))

    print('\n------Testing block 3-----')
    print('Display three generator expressions:')
    print('Generator D:', D)
    print('Generator E:', E)
    print('Generator F:', F)

    print('\n------Testing block 4-----')
    print('Display the list after zip D,E and F together(List D, E and F have the same length):')
    # Print out the result as a list.
    print('The list after zip D,E and F:', list(Together_b))

    #From block 2 and block 4, we can see the difference when we use zip() to deal with lists with same length and different lengths.


    print('\n***Program Complete***')

if __name__ == '__main__':
    main()