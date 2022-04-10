#Student name: Jianwei Su
#Date: 04/05/2022
# #1.2.1


def main():
    # Code goes here
    print('\n==========Exercise 1.2.1===========')

    #This is an empty list. It is to store the numbers later.
    numList=[]

    # Keeps asking the user for a number, until the user enters the letter s.
    #Here it is to use a while loop to fullfill the conditions.
    while (True):
        num = input('Enter a number (s to stop): ')

        #If the user enters the letter s, the loop ends.
        if num == 's':
            break
        #If the user enters'', the loop will continue to ask the user to enter numbers
        elif num =='':
            continue
        #Here is to append the numbers to the empty list.
        else:
            numList.append(float(num))

    # Once the user finishes entering numbers, calculate and display the average of the numbers.
    # sum() function is to sum of numbers in the list
    # The len() function returns the length of a list
    # It prints out the average of the numbers in the list on screen
    print("Average of the numbers:",sum(numList)/len(numList))

    print('\n***Program Complete***')



if __name__ == '__main__':
    main()