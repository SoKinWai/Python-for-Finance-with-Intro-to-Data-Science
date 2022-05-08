#Student Name: Jianwei Su
#Date: 04/23/2022
#4.1.3

def main():
    # Code goes here
    print('\n==========Exercise 4.1.3==========')

    #Create a file path list
    file_list=['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']

    print('------Testing block 1-----')
    print('Join the list together to create a valid pathname.')

    print('Put the list together to create a valid pathname:','\\'.join(file_list))

    print('\n------Testing block 2-----')
    print('Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ and join the resulting list to create a valid pathname.')

    #Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’
    file_list.insert(4,'New_folder')

    #Check the list after inserting
    print('The new list after inserting:',file_list)

    #Join the resulting list to create a valid pathname
    print('Join the resulting list to create a valid pathname:', '\\'.join(file_list))








    print('\n***Program Complete***')

if __name__ == '__main__':
    main()