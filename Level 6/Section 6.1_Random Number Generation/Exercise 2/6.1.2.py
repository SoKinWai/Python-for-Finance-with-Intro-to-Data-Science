#Student Name: Jianwei Su
#Date: 05/13/2022
#6.1.2


import logging
import random
from collections import OrderedDict




def freq(input):
    number_dict={}

    #Round all the numbers to be integers
    a=[round(x) for x in input]

    #Number to be counted
    num_count=set(a)
    for num in num_count:
        number_dict[num]=a.count(num)

    #This is to make sure the dict is sorted
    dict1 = OrderedDict(sorted(number_dict.items()))

    return dict1


def scale(input):
    scale_dic={}

    x=freq(input)

    #Get the max_old and min_old
    max_old=max(list(x.values()))
    min_old=min(list(x.values()))

    max_new=100
    min_new=1

    for key in list(x.keys()):
        scal=round(((max_new-min_new)/(max_old-min_old))*(x[key]-max_old)+max_new)
        scale_dic[key]=scal

    return scale_dic

def hist(input):

    x=scale(input)


    for a, b in x.items():
        string='-'
        logging.info(f'{a}:{b*string}')











def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 6.1.2=========')

    # Set seed
    random.seed(6)

    logging.info('\n------Testing block 1-----')
    logging.info('Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20')

    random_uniform = [random.uniform(1, 20) for a in range(200000)]

    logging.info(f'Check the length of random_uniform list: {len(random_uniform)}')

    logging.info('\n')
    logging.info('------Testing block 2-----')
    logging.info('Generate 200,000 normally distributed random numbers (mu=10, sigma=7)')

    random_nor_dis = [random.normalvariate(mu=10, sigma=7) for b in range(200000)]

    logging.info(f'Check the length of random_nor_dis list: {len(random_nor_dis)}')

    logging.info('\n')
    logging.info('------Testing block 3-----')
    logging.info('Generate 200,000 lognormally distributed random numbers (mu=1, sigma=0.5)')

    random_log_nor = [random.lognormvariate(mu=1, sigma=0.5) for c in range(200000)]

    logging.info(f'Check the length of random_log_nor list: {len(random_log_nor)}')



    logging.info('\n')
    logging.info('------Testing block 4-----')
    logging.info('Using horizontal dashes (-) to represent 200,000 uniform random numbers:')

    hist(random_uniform)

    logging.info('\n')
    logging.info('------Testing block 5-----')
    logging.info('Using horizontal dashes (-) to represent 200,000 normally distributed random numbers (mu=10, sigma=7):')
    hist(random_nor_dis)



    logging.info('\n')
    logging.info('------Testing block 6-----')
    logging.info('Using horizontal dashes (-) to represent 200,000 lognormally distributed random numbers (mu=1, sigma=0.5):')

    hist(random_log_nor)






    logging.info('\n***Program Complete***')



if __name__ == '__main__':
    main()

