#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.8


#Time module provides us with various functions to inculcate the system time
import time

def main():
    # Code goes here
    print('\n==========Exercise 1.2.8===========')

    #Create a list of names, and a second list of ages which correspond to a name in the first list
    Names=['KaKa', 'Ankur','John','Jean']
    Ages=[38,30,23,16]

    #start=time.time() is to count the starting time of the process
    start = time.time()
    #Zip them together and print the result.
    # zip(Names, Ages) means zip the names from list Names and ages from list Ages together in this form [(Name1,Age1),(Name2,Age2)...]
    Names_with_Ages=list(zip(Names,Ages))
    #Here prints out the list of zip(Names,Ages)
    print('Names with Ages:',Names_with_Ages)


    #Using a list comprehension, create a list that contains all the names for which the corresponding age is greater than or equals to 18.
    #This is the list comprehension method to filter who's age is greater or equal to 18
    List=[(Names, Ages) for Names, Ages in Names_with_Ages if Ages>=18]
    print('Ages are greater than or equal to 18:', List)

    #end=time.time() is to count the end time of this process
    end=time.time()
    # str(end-start) is to calculate the time it takes for this process.
    print('Seconds with zip:',str(end-start))

    start = time.time()

    print('\n')

    #Do this without zip
    #This is the enmumerate method to do the same
    #list(enumerate(Names)) will have a list in this way:[(0, 'KaKa'), (1, 'Ankur'), (2, 'John'), (3, 'Jean')]
    #I also used list comprehension here
    #i means the number order, so i is 0,1,2 or 3. For example, Ages[0] is 38
    List_a=[(x,Ages[i]) for i, x in enumerate(Names)]
    print('Names with Ages(without zip):', List_a)

    List_b=[(Names,Ages) for Names, Ages in List_a if Ages>=18]
    print('Without zip:',List_b)
    end = time.time()
    print('Seconds without zip:', str(end - start))

    #Can you also do this without zip? Which is better?
    #Yes, I can. We can see they do not have any time difference with these two methods, but I prefer to use the zip method
    #because it is easier for me to understand those codes.

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()
