#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.2


def main():
    # Code goes here
    print('\n==========Exercise 1.2.2===========')

    # Create a list of ten numbers.
    list = [1, 2, 3, 4, 5, 6, 7, 8.1, 9.2, 10.3]

    # Display the first two numbers from the list (using indexing).
    #[0:2] is to show the first two numbers from the list
    print('Display the first two numbers from the list (using indexing):', list[0:2],'\n')

    # Display the last two numbers
    #[-2:] is to show the last two numbers from the list
    print('Display the last two numbers:', list[-2:],'\n')

    # Display all the numbers besides the last number, using a single print statement
    #[:-1] is to show all the numbers besides the last number from the list
    print('Display all the numbers besides the last number, using a single print statement:', list[:-1],'\n')

    # Display all the numbers besides the first number, using a single print statement.
    #[1:] is to show all the numbers besides the first number from the list
    print('Display all the numbers besides the first number, using a single print statement:', list[1:],'\n')

    # Display all the numbers besides the first two and last three numbers, using a single print.
    #[2:-3] is to show all the numbers besides the first two and last three numbers from the list
    print('Display all the numbers besides the first two and last three numbers, using a single print:', list[2:-3],'\n')

    # Append one number to the end of the list.
    # .append() is to add its argument as a single element to the end of a list. The length of the list increases by one.
    list.append(11)
    print('Append one number to the end of the list:', list,'\n')

    # Append five numbers to the end of the list, using a single operation.
    #.entend() is to iterate over its argument and adding each element to the list
    # and extending the list. The length of the list increases by number of elements in it’s argument.
    list.extend([12, 13, 14, 15, 16.1])
    print('Append five numbers to the end of the list, using a single operation:', list,'\n')

    # Insert one number right after the third number in the list.
    # .insert() is to insert a given element at a given index in a list.
    #  .insert(3, 3.5) is to insert 3.5 right after the third number in the list
    list.insert(3, 3.5)
    print('Insert one number right after the third number in the list:', list,'\n')

    # Modify the fourth-to-last number in the list.
    #list[-4] means the fourth-to-last number in the list.
    #list[-4] = list[-4] + 0.5 means the the fourth-to-last number will plus 0.5 in the list.
    list[-4] = list[-4] + 0.5
    print('Modify the fourth-to-last number in the list:', list,'\n')

    # Display the list backwards, using splicing.
    #list[::-1] shows the list backwards
    list_1 = list[::-1]
    print('Display the list backwards, using splicing:', list_1,'\n')

    # Display every second item in the list
    #list[1::2] shows every second item in the list
    list_2 = list[1::2]
    print('Display every second item in the list:', list_2,'\n')

    # Display every second item in the list, backwards
    #list[::-1] shows the list backwards
    #list[1::2] shows every second item in the list
    #so togethers list[::-1][1::2] shows every second item in the list, backwards
    list_3 = list[::-1][1::2]
    print('Display every second item in the list, backwards:', list_3,'\n')


    print('\n***Program Complete***')



if __name__ == '__main__':
    main()