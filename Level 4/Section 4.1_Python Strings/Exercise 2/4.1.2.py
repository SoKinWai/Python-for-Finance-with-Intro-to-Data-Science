#Student Name: Jianwei Su
#Date: 04/23/2022
#4.1.2

def main():
    # Code goes here
    print('\n==========Exercise 4.1.2==========')

    #Save the following Windows file-path into a string variable
    file_path = 'C:\\Users\\Me\\Desktop\\MyTable.csv'

    print('------Testing block 1-----')
    print('Extract the filename with extension from the path.')

    #Method 1
    print('The filename with extension from the path(method 1):',file_path.split('\\')[-1])

    #Method 2
    print('The filename with extension from the path(method 2):', file_path.rsplit('\\',1)[1])

    # Method 3
    print('The filename with extension from the path(method 3):', file_path.rsplit('\\')[-1])

    print('\n------Testing block 2-----')
    print('Extract the file extension only.')


    #Method 1
    print('The file extension(method 1):',file_path.split('.')[-1])

    #Method 2
    print('The file extension(method 2):', file_path.rsplit('.')[1])





    print('\n------Testing block 3-----')
    print('Add another folder between ‘Desktop’ and the filename.')

    #Covert the file-path to a list without \\
    file_list=file_path.split('\\')
    print('The file-path list:',file_list)

    #Add another folder name between ‘Desktop’ and the filename.
    file_list.insert(4,'new_folder')
    print('The new file-path list:',file_list)

    #Convert back the list to a file path string
    print('The new file path:','\\'.join(file_list))


    print('\n***Program Complete***')

if __name__ == '__main__':
    main()