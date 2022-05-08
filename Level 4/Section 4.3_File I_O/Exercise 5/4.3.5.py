#Student Name: Jianwei Su
#Date: 05/03/2022
#4.3.5




# Import necessary packages
import os
import logging


def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info('\n==========Exercise 4.3.5==========')

    logging.info('Open the file from 4) and read it. Display each line.')
    logging.debug('Opening the file from 4)...\n')

    with open('C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\\Level 4\\Section 4.3_File I_O\\Exercise 4\\new_file.txt','r') as fp:
        for line in fp:
            logging.info({line})





    logging.info('\n***Program Complete***')





if __name__ == '__main__':
    main()