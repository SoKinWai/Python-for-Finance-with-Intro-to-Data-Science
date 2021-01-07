#Create a list of ten numbers.
#Should contain some integers and some decimals.
#Perform the following operations:

def main():
    #Code goes here
    list=[1,2,3,4,5,6,7,8.1,9.2,10.3]

    #Display the first two numbers from the list (using indexing).
    print('Display the first two numbers from the list (using indexing):',list[0:2])

    #Display the last two numbers
    print('Display the last two numbers:',list[-2:])

    #Display all the numbers besides the last number, using a single print statement
    print('Display all the numbers besides the last number, using a single print statement:',list[:-1])

    #Display all the numbers besides the first number, using a single print statement.
    print('Display all the numbers besides the first number, using a single print statement:',list[1:])

    #Display all the numbers besides the first two and last three numbers, using a single print.
    print('Display all the numbers besides the first two and last three numbers, using a single print:',list[2:-3])

    #Append one number to the end of the list.
    list.append(11)
    print('Append one number to the end of the list:',list)

    #Append five numbers to the end of the list, using a single operation.
    list.extend([12,13,14,15,16.1])
    print('Append five numbers to the end of the list, using a single operation:',list)

    #Insert one number right after the third number in the list.
    list.insert(3,3.5)
    print('Insert one number right after the third number in the list:',list)

    #Modify the fourth-to-last number in the list.
    list[-4]=list[-4]+0.5
    print('Modify the fourth-to-last number in the list:',list)

    #Display the list backwards, using splicing.
    list_1=list[::-1]
    print('Display the list backwards, using splicing:',list_1)

    #Display every second item in the list
    list_2=list[1::2]
    print('Display every second item in the list:',list_2)

    #Display every second item in the list, backwards
    list = list[::-1][1::2]
    print('Display every second item in the list, backwards:', list)

if __name__ == '__main__':
    main()