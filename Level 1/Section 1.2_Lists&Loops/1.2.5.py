#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.5

def main():
    # Code goes here
    print('\n==========Exercise 1.2.5===========')

    # Create a list of all even integers 1-1000.
    # list_3=[i for i in range(1, 1001) if i%2==0] wil have the same answer, but not i%2 is considered cleaner syntax than i%2 == 0
    # i%2 means i%2==1 here
    # rang(1, 1001) means all integers from 1 to 1000
    list_3 = [i for i in range(1, 1001) if not i % 2]

    # Create a list of all odd integers 1-1000.
    # list_4=[i for i in range(1, 1001) if i%2==1] wil have the same answer, but i%2 is considered cleaner syntax than i%2 == 1
    # i%2 means i%2==1 here
    # rang(1, 1000) means all integers from 1 to 999
    list_4 = [i for i in range(1, 1000) if i % 2]

    #Print out list 3 and list 4 on screen
    print('List 3:',list_3,'\n')
    print('List 4:',list_4,'\n')

    #Create an aggregate list from 3) and 4) and print it out, backwards and separated by commas.
    list_5=list_3+list_4
    print('List 5 in backwards:',list_5[::-1],'\n')

    #sorted() returns a list with the elements in sorted manner, without modifying the original sequence.
    List_5=sorted(list_5,reverse=True)

    #Print out an aggregate list from 3) and 4) and print it out from the largest to the least.
    print('List 5 from the largest to the least:', List_5, '\n')



    print('\n***Program Complete***')



if __name__ == '__main__':
    main()