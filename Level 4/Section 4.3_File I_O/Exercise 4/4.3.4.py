#Student Name: Jianwei Su
#Date: 05/03/2022
#4.3.4




# Import necessary packages
import os
import logging



def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info('\n==========Exercise 4.3.4==========')
    logging.info('Open a brand-new file and write to it (should write several lines).')
    logging.debug('Creating a new file.')

    with open('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 4\\new_file.txt','w') as fp1:
        fp1.write('This is a new file.\n')
        fp1.write('I am writing few lines into it.\n')
        fp1.write('This is exercise 4.\n')
        fp1.write('I am going to close it.')









    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()