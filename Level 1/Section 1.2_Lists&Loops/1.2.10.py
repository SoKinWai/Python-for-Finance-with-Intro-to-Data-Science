#Student name: Jianwei Su
#Date: 04/05/2022
#1.2.10


def main():
    # Code goes here
    print('\n==========Exercise 1.2.10===========')

    #Create a list of lists of any type.
    list1=[[1,2],[1,2,3],[2,3,4],[3,4,5,6]]

    #Use the double list-comprehension syntax, as described in the lecture, to create a flattened single list.
    #This is the double list-comprehension syntax to remove those [] of a list.
    flat_list =[item for sublist in list1 for item in sublist]

    print('The flattened single is: ',flat_list )

    # which means
    #Flat_list=[]
    #for sublist in list1:
    #    for item in sublist:
    #        Flat_list.append(item)

    #print(Flat_list)

    print('\n***Program Complete***')


if __name__ == '__main__':
    main()