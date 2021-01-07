#1.1.5
#Extend the program from 4) to display the type of the variable that contains the value that the user
#entered.


def main():
    #Code goes here

    integer=input('Please enter an integer:')

    #The type should be a string.
    print('Integer is:',integer,'.The type is',type(integer))

if __name__ == '__main__':
    main()
