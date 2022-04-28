#Student Name: Jianwei Su
#Date: 04/18/2022
#3.1.3

#reconcileLists() function
#It takes two separate lists as its parameters.
def reconcileLists(list_a,list_b):

    #It will return to a list of True or False values when these two lists have the same length
    if len(list_a)==len(list_b):

        return [i==j for i, j in zip(list_a,list_b)]


    #It will show an error message when these two lists have different lengths.
    else:
        return 'Error:These two lists do not have the same length.'




def main():
    # Code goes here
    print('\n==========Exercise 3.1.3==========\n')


    # Initialize loans
    list_a=[1,2,3,4,5,6,7,8,9,10]
    list_b=[2,4,6,8,10,12,14,16,18,20]
    list_c=[]
    list_d=[]
    list_e=[1,2,3,4,5,6,7,8,10,11]
    list_f=[1,2,3,4,5,6,7,8,9,10,11]





    print('\n------Testing block 1-----')
    print('Test the reconcileLists() function via using two same length lists with total different numbers:')
    print(reconcileLists(list_a,list_b))

    print('\n------Testing block 2-----')
    print('Test the reconcileLists() function via using two same length lists with some same numbers:')
    print(reconcileLists(list_a,list_e))

    print('\n------Testing block 3-----')
    print('Test the reconcileLists() function via using different length lists:')
    print(reconcileLists(list_a,list_f))

    print('\n------Testing block 4-----')
    print('Test the reconcileLists() function via using one empty list')
    print(reconcileLists(list_a,list_c))

    print('\n------Testing block 5-----')
    print('Test the reconcileLists() function via using both empty lists')
    print(reconcileLists(list_c, list_d))







    print('\n***Program Complete***')


if __name__ == '__main__':
    main()