#Student Name: Jianwei Su
#Date: 05/02/2022
#4.3.1


# Import necessary packages
import os
import logging
import shutil


def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.DEBUG)


    logging.info('\n==========Exercise 4.3.1==========')

    logging.info('------Testing block 1-----')

    logging.info('Create a new directory.')

    try:
        #Create a new directory
        os.mkdir('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\New Dir')
    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')

    logging.info('\n------Testing block 2-----')

    logging.info('Rename the above directory.')
    try:
        #Rename the above directory
        os.rename('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\New Dir', 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\New Dir rename')
    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')

    logging.info('\n------Testing block 3-----')

    logging.info('Delete the above directory.')

    try:
        #Delete the above directory.
        os.rmdir('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\New Dir rename')
    except Exception as ex:
        logging.exception(ex)

    # Path
    path_1 = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\New Dir rename'
    # Check whether the specified path is existing
    isFile_1 = os.path.isfile(path_1)
    logging.info(f'The above directory is existing: {isFile_1}')





    logging.info('\n')

    logging.info('\n------Testing block 4-----')

    logging.info('Create another directory and create two text files in this directory.')

    try:
        #Create a new directory
        os.mkdir('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir')
    except Exception as ex:
        logging.exception(ex)

    logging.debug('Creating two text files...')
    with open('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\textfile_a.txt','w') as fp1:
        fp1.write('This is the first file.')

    with open('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\textfile_b.txt','w') as fp2:
        fp2.write('This is the second file.')



    logging.info('\n')

    logging.info('\n------Testing block 5-----')

    logging.info('Delete one of the text files from the above directory.')

    os.remove('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\textfile_b.txt')

    # Path
    path_2 = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\textfile_b.txt'
    # Check whether the specified file is existing
    isFile_2 = os.path.isfile(path_2)
    logging.info(f'The above file is existing: {isFile_2}')



    logging.info('\n')

    logging.info('\n------Testing block 6-----')

    logging.info('Rename the remaining text file.')

    try:
        #Rename the remaining text file.
        os.rename('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\textfile_a.txt','C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\new_textfile_a.txt')
    except Exception as ex:
        logging.exception(ex)



    logging.info('\n')

    logging.info('\n------Testing block 7-----')

    logging.info('Create a subdirectory within the above created directory.')

    try:
        #Create a subdirectory within the above created directory.
        os.mkdir('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\subdirectory')
    except Exception as ex:
        logging.exception(ex)



    logging.info('\n')

    logging.info('\n------Testing block 8-----')

    logging.info('Move the remaining text file into the subdirectory.')

    try:
        #Move the remaining text file into the subdirectory.
        os.rename('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\new_textfile_a.txt','C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir\\subdirectory\\new_textfile_a.txt')
    except Exception as ex:
        logging.exception(ex)

    logging.info('\n')

    logging.info('\n------Testing block 8-----')

    logging.info('Remove the top level directory with all its contents (using a single function call). Be careful!')

    path_3='C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 1\\Another New Dir'

    #User has to use shutil.rmtree() to remove non empty directory
    shutil.rmtree(path_3)

    isFile_3 = os.path.isfile(path_3)
    logging.info(f'The above directory is existing: {isFile_3}')

    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()
