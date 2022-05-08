#Student Name: Jianwei Su
#Date: 05/03/2022
#4.3.3

# Import necessary packages
import os
import logging



def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 4.3.3==========')
    logging.info('Write code that searches your entire computer for all pdf files which reside in any directory (at any level) that contains the string ‘gr’ in its name.')

    logging.info('------Testing block -----')
    list_pdf = []

    for x, y, files in os.walk('C:\\'):
        for file in files:
            if file[-4:]=='.pdf' and file.find('gr')!=-1:
                list_pdf.append(file)


    logging.info(f'There are {len(list_pdf)} files of extension py in my entire computer.')









    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()