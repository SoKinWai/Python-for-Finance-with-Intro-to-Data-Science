#Student name: Jianwei Su
#Date: 04/04/2022
#1.3.5

#Mean fuction
#This function takes in a list of ints and/or floats（List) as its input parameter and calculates the average of all
#the entries of the input list. The function then returns the calculated average
def Average(List):
    #Calculate the average of List by taking the sum of all its elements and dividing it by the length of the List.
    #Return the resulting average
    return (sum(List) / len(List))

#This function takes in a list of ints and/or floats(List) as its input paremeter and calculates the variance of
#all entries of the input List. The function then returns the calculated variance on screen.
#Set the degOfFreedom variable to 1 by default
def get_variance(List,degOfFreedom=1):
    # Calcualte the variance of List by taking the sum of all its emememts minus the mean and dividing it by the length of the List minus degOfFreedom.
    # Return the resulting variance
    return sum((i - Average(List)) ** 2 for i in List) / (len(List)-degOfFreedom)



def main():
    # Code goes here
    print('\n==========Exercise 1.3.5===========')

    l=[1,3,4,50]

    #Population mean with entering 0
    #Type 0 as the input of degOfFreedom without degOfFreedom =
    print("Population variance with entering 0 without degOfFreedom =:",get_variance(l,0))

    #Sample mean
    # Type 1 as the input of degOfFreedom without degOfFreedom =
    print("Sample variance with entering 1 without degOfFreedom =:",get_variance(l,1))

    #Using key argument
    #Type 0 and 1 as the inputs of degOfFreedom with degOfFreedom =
    print("Sample variance via using key argument degOfFreedom =:",get_variance(l, degOfFreedom = 1))
    print("Population variance via using key argument degOfFreedom =:",get_variance(l, degOfFreedom = 0))

    #Using without key argument
    print("Sample variance without using key argument:", get_variance(l))

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()