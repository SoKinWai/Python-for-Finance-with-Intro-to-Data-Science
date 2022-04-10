#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.4


def main():
    # Code goes here
    print('\n==========Exercise 1.2.4===========')

    # Create a list of all odd integers 1-1000.
    # list_4=[i for i in range(1, 1001) if i%2==1] wil have the same answer, but i%2 is considered cleaner syntax than i%2 == 1
    # i%2 means i%2==1 here
    # rang(1, 1000) means all integers from 1 to 999
    list_4 = [i for i in range(1, 1000) if i % 2]

    # Write a loop that prints all numbers in the above list, separated by commas.
    # This is a loop that prints all numbers in the above list
    for x in list_4:
        if x < 999:
            print(x, ',')
        else:
            print(x)


    print('\n***Program Complete***')


if __name__ == '__main__':
    main()