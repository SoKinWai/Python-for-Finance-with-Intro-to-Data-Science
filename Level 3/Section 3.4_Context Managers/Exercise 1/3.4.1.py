#Student Name: Jianwei Su
#Date: 04/22/2022
#3.4.1

def main():
    # Code goes here
    print('\n==========Exercise 3.4.1==========')

    print('\n------Testing block-----')
    print('Testing  context manager demo.')

    #Open a file and write to it, using the with statement.
    with open("contextManager_a.txt",'w') as f:
        f.write('Python is even better with context managers!\n')

        #Verify that the file has indeed been closed.
        #Here will show False.
        print('Is the file closed?',f.closed)

        f.write('Isn‘t it?\n')
        f.write('Yes, I think it is!')

    #Verify that the file has indeed been closed.
    #The flie is automatically closed when using with statement to open it and write it.
    print('Is the file closed?',f.closed)



    print('\n***Program Complete***')

if __name__ == '__main__':
    main()