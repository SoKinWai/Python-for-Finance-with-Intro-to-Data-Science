#Student Name: Jianwei Su
#Date: 05/13/2022
#6.1.1

import logging
import random




def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 6.1.1=========')


    #Set seed
    random.seed(5)

    logging.info('\n------Testing block 1-----')
    logging.info('Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20')

    random_uniform=[random.uniform(1,20) for a in range(200000)]

    logging.info(f'Check the length of random_uniform list: {len(random_uniform)}')

    logging.info('\n')
    logging.info('------Testing block 2-----')
    logging.info('Generate 200,000 normally distributed random numbers (mu=10, sigma=7)')

    random_nor_dis = [random.normalvariate(mu=10,sigma=7) for b in range(200000)]

    logging.info(f'Check the length of random_nor_dis list: {len(random_nor_dis)}')

    logging.info('\n')
    logging.info('------Testing block 3-----')
    logging.info('Generate 200,000 lognormally distributed random numbers (mu=1, sigma=0.5)')

    random_log_nor = [random.lognormvariate(mu=1,sigma=0.5) for c in range(200000)]

    logging.info(f'Check the length of random_log_nor list: {len(random_log_nor)}')

    logging.info('\n')
    logging.info('------Testing block 4-----')
    logging.info('Export these lists of numbers to a single CSV file (should have 200,000 rows and three columns)')

    lines=[]
    list_csv=list(zip(random_uniform,random_nor_dis,random_log_nor))
    for x in list_csv:
        lines.append(','.join([str(x[0]),str(x[1]),str(x[2])]))



    outputString = '\n'.join(lines)

    file_path = 'C:\\Users\\sujhu\\OneDrive\\桌面\\Online Courses\\Python for Finance with Intro to Data Science\\Assignments\Level 6\\Section 6.1_Random Number Generation\\Exercise 1\\number_list.csv'


    with open(file_path, 'w') as fp:
     fp.write(outputString)










    logging.info('\n***Program Complete***')



if __name__ == '__main__':
    main()