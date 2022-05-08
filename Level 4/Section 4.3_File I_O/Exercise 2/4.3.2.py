#Student Name: Jianwei Su
#Date: 05/02/2022
#4.3.2

# Import necessary packages
import os
import logging

def main():
    # Code goes here

    #This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)



    logging.info('\n==========Exercise 4.3.2==========')
    logging.info('Write code that searches your entire computer for all files of extension py. ')

    logging.info('------Testing block -----')
    list_py=[]

    for x, y, files in os.walk('C:\\'):
        for file in files:
            if file[-3:]=='.py':
                list_py.append(file)


    logging.info(f'There are {len(list_py)} files of extension py in my entire computer.')





    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()