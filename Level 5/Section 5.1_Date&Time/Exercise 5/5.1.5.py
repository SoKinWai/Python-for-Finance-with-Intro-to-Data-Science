#Student Name: Jianwei Su
#Date: 05/09/2022
#5.1.5

import logging
import datetime


def date_differential():
    # Prompt the user to enter any date and time.
    d_1 = input('Please enter the date in the following format(YYYY-mm-dd HH:MM:SS:fffff e.g.2016-09-25 18:23:14:012342):')

    # Prompt the user to enter another date and time.
    d_2 = input('Please enter the date in the following format(YYYY-mm-dd HH:MM:SS:fffff e.g.2016-09-25 18:23:14:012342):')

    date_1=datetime.datetime.strptime(d_1,'%Y-%m-%d %H:%M:%S:%f')

    date_2=datetime.datetime.strptime(d_2,'%Y-%m-%d %H:%M:%S:%f')

    date_delta=date_1-date_2

    total_days=abs(date_delta.total_seconds()/86400)
    total_hours=abs(date_delta.total_seconds()/3600)
    total_minutes=abs(date_delta.total_seconds()/60)
    total_microseconds=abs(date_delta.total_seconds()* 1000000)


    hours=int(total_hours-date_delta.days*24)
    minutes=int(total_minutes-date_delta.days*1440-hours*60)
    secconds=int(date_delta.total_seconds()-date_delta.days*86400-hours*3600-minutes*60)



    logging.info(f'Total number of days (including fractions of days):{total_days}')
    logging.info(f'Total number of hours (including fractions):{total_hours}')
    logging.info(f'Total number of minutes (including fractions):{total_minutes}')
    logging.info(f'Total number of seconds (including fractions):{abs(date_delta.total_seconds())}')
    logging.info(f'Total number of microseconds (including fractions):{total_microseconds}')

    #A complete (grammatically-correct) sentence that breaks everything down to the correct units and excluding any 0s
    logging.info(f'The difference is {date_delta.days} days, {hours} hours, {minutes} minutes, {secconds} seconds, and {date_delta.microseconds} microseconds.')

    #Here is to check if the answer is correct
    logging.info(f'time difference: {date_delta}')






def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.1.5==========')


    logging.info('\n------Testing block-----')

    try:
        date_differential()
    except Exception as ex:
        logging.exception(ex)
        logging.error('Invalid date info entered.')

    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()