#Student name: Jianwei Su
#Date: 04/06/2022
#1.5.6

#freqMap() function
#It returns the frequency of each number from input
#I modified the function from the course video because this way is easier for me to understand
def freqMap(values):
    map={}
    for v in values:
        if v in map:
             map[v]+=1
        else:
             map[v]=1
    return map

#Mode() function
#Create the mode function, building off the frequency function that was demonstrated in the lecture.
#It prints most frequent numbers on screen
def Mode(values):
    a=freqMap(values)
    #Return a tuple, containing a list of mode values (containing one or more items) and their frequency
    mod = [(key,value) for key, value in a.items() if value==max(a.values())]
    #Print the result of a list of mode values on screen.
    print(mod)


def main():
    # Code goes here
    print('\n==========Exercise 1.5.6===========')

    #Create a list with few numbers
    my_list_1 = [1,1,2,2,3,4,5]

    #Print the frequency of each number as a dict on screen
    print("Frequency of each number for list 1:",freqMap(my_list_1))


    print("\nMost frequent numbers for list 1:")
    #Use the Mode() function to print the most frequent numbers on screen.
    Mode(my_list_1)

    #Create another list to test the functions
    my_list_2=[1,2,3,4,5]

    # Print the frequency of each number as a dict on screen
    print("\nFrequency of each number for list 2:", freqMap(my_list_2))

    print("\nMost frequent numbers for list 2:")
    # Use the Mode() function to print the most frequent numbers on screen.
    Mode(my_list_2)

    print('\n***Program Complete***')




if __name__ == '__main__':
    main()

