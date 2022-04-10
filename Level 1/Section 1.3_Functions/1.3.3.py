#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.3

#Average() Function
# This function takes in a list of ints and/or floats（List) as its input parameter and calculates the average of all
#the entries of the input list. The function then returns the calculated average on screen
def Average(List):
    #Calculate the average of List by taking the sum of all its elements and dividing it by the length of the List.
    #Then return the resulting average
    return (sum(List) / len(List))


def main():
    # Code goes here
    print('\n==========Exercise 1.3.3===========')

    print('\nCalculates the mean of a passed-in list:')
    l=[1,3,4,50]

    #Calculate the average of the numbers in the list.
    print(Average(l))

    print('\n***Program Complete***')

if __name__ == '__main__':
        main()

