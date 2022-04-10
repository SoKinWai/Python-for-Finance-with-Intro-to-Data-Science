#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.6


def main():
    # Code goes here
    print('\n==========Exercise 1.2.6===========')

    # Write a list comprehension that results in a list of the squares of all numbers 0 through 100:
    #i**2 means i's square
    #rang(101) means all integers from 0 to 100
    list_a=[i**2 for i in range(101)]
    print('List a:',list_a,'\n')

    #Filter the resulting list, to create another list that only contains numbers greater than 1000
    list_b=[i for i in list_a if i>1000]
    print('List b:',list_b,'\n')

    #Filter further, to create another list that only contains even numbers (hint: use the Modulus operator).
    #list_c=[i for i in list_a if i%2==0] wil have the same answer, but not i%2 is considered cleaner syntax than i%2 == 0
    #i%2 means i%2==1 here
    list_c = [i for i in list_a if not i % 2]
    print('List c:',list_c,'\n')

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()

