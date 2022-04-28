#Student Name: Jianwei Su
#Date: 04/19/2022
#3.2.9

#Creat a function to loop through the list and output each name
def name_loop(Names):
    for name in Names:
        yield name

def main():
    # Code goes here
    print('\n==========Exercise 3.2.9==========')


    #Create a list of ten names.
    Names=['Ankur','Tim', 'Farbod', 'David', 'Adam', 'Rakesh', 'Jon', 'Fabino','Jim', 'Alex']

    #Check the length of the list of ten names
    print('Check the length of the list of ten names:',len(Names))

    #Loop through the list and output each name

    #Method 1
    #Just use the normal loop method.
    print('\n------Testing block 1-----')
    print('Display each name the list(Method 1):')
    a=0
    for name in Names:
        a=a+1
        print('Name',a,':',name)


    #Method 2
    #Use the name_loop function I created above
    print('\n------Testing block 2-----')
    print('Display each name the list(Method 2):')
    Output_names = name_loop(Names)
    a=0
    while a<10:
        #It will just print out 10 first names of the list if I put Output_names here
        #Output_names = name_loop(Names)
        a=a+1
        print('Name',a,':',next(Output_names))


    #Method 3
    #Use the enumerate() function
    print('\n------Testing block 3-----')
    names=list(enumerate(Names))
    print('The list after using enumerate() will be:',names)
    print('Display each name the list(Method 3):')
    for (x,y) in names:
        print('Name',x+1,':',y)

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()