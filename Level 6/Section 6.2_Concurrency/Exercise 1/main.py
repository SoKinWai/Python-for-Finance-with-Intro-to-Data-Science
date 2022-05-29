#Student Name: Jianwei Su
#Date: 05/16/2022
#6.2.1


from utils.timer import timer
from Monty_Hall.game import Game
from Monty_Hall.player import Player
import logging
import random
from utils.timer import timer
import multiprocessing
import time




@timer
def monte_pro(game,N):

    list_a = runSimulation(game,N)

    pro=list_a.count(True)/len(list_a)
    return logging.info(f'The winning probability is {pro}')


# runSimulation  (for monte hall problem)
def runSimulation (game,N):
    # run simulation
    result_list=[]

    for a in range(N):
        result_list.append(game.playGame())

    return result_list



def doWork(input, output):  # 2 parameters input queue and output queue

        # f is the function runSimulation()
        # args in this case is (game, int(N_sim/N_process) from the input_queue
        f, args = input

        res = f(*args)  # call f() with the list of arguments

        output.put(res)  # get the result from f() and put it on the output queue



@timer
def runSimulationParallel(game,N_sim,N_process):

    # In this case, output contains the results from the function

    # Create a Queue type object, anything can be added to the queue
    # and communicate to each other
    output_queue = multiprocessing.Queue()

    process=[]

    for i in range(N_process):


        # target = doWork() is the function you want the process to call
        # args = arguments to get passed to the target = doWork()
        p = multiprocessing.Process(target=doWork, args=((runSimulation, (game, int(N_sim / N_process))), output_queue))

        p.start()
        process.append(p)




    # As soon as the process is started, the target = doWork() function gets called

    # Create an infinite loop and monitor output queue
    res = []



    while True:
        # Take something off the queue, if queue has nothing, it will block (wait)
        # until the queue has something, while other processes running in the background
        # when it has something, add it to the list res = []


        if len(res)!=N_sim:
            r = output_queue.get()
            res.extend(r)
        else:

            # When it's done, break the loop
            break


    logging.info(f'The result‘s length is {len(res)}.')
    logging.info(f'The winning probability is {res.count(True)/len(res)}.')


    #Every spawned process should be stopped when finished with it.
    for x in process:

        #You can call join on the process
        x.join()
        x.terminate()

def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 6.2.1=========')

    player_a = Player(True)
    player_b = Player(False)

    game_a = Game(player_a)
    game_b = Game(player_b)

    logging.info('\n------Testing block 1-----')
    logging.info('Compare the time taken with previous level(Stay with the door, try 10000000 times):')

    #Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each)
    runSimulationParallel(game_a, 10000000, 5)

    logging.info('\n')
    monte_pro(game_a, 10000000)



    logging.info('\n')
    logging.info('\n------Testing block 2----')
    logging.info('Compare the time taken with previous level(Switch the door, try 10000000 times)')

    # Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each)
    runSimulationParallel(game_b, 10000000, 5)

    logging.info('\n')
    monte_pro(game_b, 10000000)


    #multiprocessing is faster than the previous level's.

    logging.info('\n')
    logging.info('\n------Testing block 3----')
    logging.info('Try decreasing/increasing the number of processes to determine the optimal runtime')


    logging.info('\n')
    logging.info('Try 20 processes(stay with the door.)')
    runSimulationParallel(game_a, 10000000, 20)

    logging.info('\n')
    logging.info('Try 20 processes(switch the door.)')
    runSimulationParallel(game_b, 10000000, 20)

    logging.info('\n')
    logging.info('Try 40 processes(stay with the door.)')
    runSimulationParallel(game_a, 10000000, 40)

    logging.info('\n')
    logging.info('Try 40 processes(switch the door.)')
    runSimulationParallel(game_b, 10000000, 40)

    logging.info('\n')
    logging.info('Try 100 processes(stay with the door.)')
    runSimulationParallel(game_a, 10000000, 100)

    logging.info('\n')
    logging.info('Try 100 processes(switch the door.)')
    runSimulationParallel(game_b, 10000000, 100)

    logging.info('\n')
    logging.info('Try 2 processes(stay with the door.)')
    runSimulationParallel(game_a, 10000000, 2)

    logging.info('\n')
    logging.info('Try 2 processes(switch the door.)')
    runSimulationParallel(game_b, 10000000, 2)




    #When I increased the processes, it would take less time.
    #So I think it will be the fastest to try 10,000,000 times.
    #However, I could not try 10,000,000 times because my program will crash.








    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()