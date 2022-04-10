#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.4

#Average() Function
#This function takes in a list of ints and/or floats（List) as its input parameter and calculates the average of all
#the entries of the input list. The function then returns the calculated average
def Average(List):
    #Calculate the average of List by taking the sum of all its elements and dividing it by the length of the List.
    #Then return the resulting average
    return (sum(List) / len(List))

#Variance function
#This function takes in a list of ints and/or floats(List) as its input paremeter and calculates the variance of
#all entries of the input List. The function then returns the calculated variance on screen
def get_variance(List):
    #Calcualte the variance of List by taking the sum of all its emememts minus the mean and dividing it by the length of the List.
    #Then print the resulting variance
    return sum((i - Average(List)) ** 2 for i in List) / len(List)



def main():
    # Code goes here
    print('\n==========Exercise 1.3.4===========')

    print('\nCalculates the variance of a passed-in list:')
    l=[1,3,4,50]

    #Calculate the variance of the numbers in the list.
    print(get_variance(l))

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()