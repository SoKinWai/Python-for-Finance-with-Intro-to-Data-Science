#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.6

#Mean fuction
#This function takes in a list, a tuple or variable numbers of arguments
# of ints and/or floats（List) as its input parameter and calculates the average of all
#the entries of the input list. The function then returns the calculated average
def argsMean(*args):
    # Calculate the average of a list, a tuple or variable numbers of arguments
    # by taking the sum of all its elements and dividing it by the length of the list, the tuple or the variable numbers of arguments.
    # Then returns the resulting average
    return sum(args) / len(args)

def main():
    # Code goes here
    print('\n==========Exercise 1.3.6===========')

    #Take variable numbers of arguments as input
    #Print out the mean function with variable numbers of arguments
    print("Test the function with variable numbers of arguments:",argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6))

    # Pass a tuple
    #Take a tuple of numbers as input
    #Print out the mean function with a tuple of numbers
    #Remember to type * before the tuple as input
    l_1=(1.3, 4.5, 6.7, 11.2, 100, 987.6)
    print("Pass a tuple:",argsMean(*l_1))


    #Pass a list
    # Take a list of numbers as input
    # Print out the mean function with a list of numbers
    #Remember to type * before the list as input
    l_2=[1.3, 4.5, 6.7, 11.2, 100, 987.6]
    print("Pass a list:",argsMean(*l_2))

    # Errors will show on screen if you do not type * before the list and the tuple as inputs
    #print(argsMean(l_1))
    #print(argsMean(l_2))

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()



