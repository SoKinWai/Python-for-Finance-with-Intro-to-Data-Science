#Student Name: Jianwei Su
#Date: 05/28/2022
#Level 7

import numpy as np
from simulation.simulateWaterfall import simulateWaterfall
from utils.timer import timer
import numpy as np
import multiprocessing
import logging
from utils.memoize import memoize

@memoize
def calculateYield(DIRR, WAL):

    return ((7 / (1 + .08 * np.exp(-0.19 * WAL / 12))) + 0.19 * np.sqrt((WAL / 12) * DIRR * 100)) / 100

@memoize
def new_tranche_rate(old_rate, yield_rate, coeff):

    return old_rate + coeff * (yield_rate - old_rate)

# 𝑛𝐴 𝑖𝑠 𝑇𝑟𝑎𝑛𝑐ℎ𝑒 𝐴 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙,
# 𝑛𝐵 𝑖𝑠 𝑇𝑟𝑎𝑛𝑐ℎ𝑒 𝐵 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙,
# 𝑁 𝑖𝑠 𝑡ℎ𝑒 𝑡𝑜𝑡𝑎𝑙 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙.
@memoize
def Diff(nA, nB, lastArate, lastBrate, newArate, newBrate):

    N= nA+nB
    diff = (nA * abs((lastArate - newArate) / lastArate) + nB * abs((lastBrate - newBrate) / lastBrate)) / N
    return diff

@memoize
def convert_rating(dirr_input):
    dirr = dirr_input / 100


    ABS_Rating = {'Aaa': 0.06,
                   'Aa1': 0.67,
                   'Aa2': 1.3,
                   'Aa3': 2.7,
                   'A1': 5.2,
                   'A2': 8.9,
                   'A3': 13,
                   'Baa1': 19,
                   'Baa2': 27,
                   'Baa3': 46,
                   'Ba1': 72,
                   'Ba2': 106,
                   'Ba3': 143,
                   'B1': 183,
                   'B2': 231,
                   'B3': 311,
                   'Caa': 2500,
                   'Ca': 10000}


    try:

        # Find the smallest value at which value >= dirr
        closest_value=min([x for x in ABS_Rating.values() if x>=dirr])


        ratings = {a: b for b, a in ABS_Rating.items()}


        return ratings[closest_value]

    except Exception:
        return 'Ca'






@timer
@memoize
#Modify the runMonte function to call runSimulationParallel instead of runSimulation
def runMonte(loan_pool, structured_securities, tolerance, NSIM, numProcesses):


    oldTrancheRate = [tranche.rate for tranche in structured_securities.tranches]
    Tranchenotional= [tranche.notional for tranche in structured_securities.tranches]



    # coeff is 1.2 for Tranche A and 0.8 for Tranche B
    coff_list=[1.2, 0.8]

    while True:

        #Metrics= simulateWaterfall(loan_pool, structured_securities, NSIM)
        Metrics=runSimulationParallel(loan_pool, structured_securities, NSIM, numProcesses)
        A=Metrics[0]
        B=Metrics[1]

        yield_values = [calculateYield(metric[0], metric[1]) for metric in Metrics]

        newTrancheRate = [new_tranche_rate(oldTrancheRate[a],yield_values[a], coff_list[a]) for a in [0,1]]

        diff = Diff(Tranchenotional[0], Tranchenotional[1], oldTrancheRate[0], oldTrancheRate[1], newTrancheRate[0], newTrancheRate[1])


        # If diff is lower than tolerance, then break from the infinite loop
        if diff < tolerance:
            break

        # If diff is greater than tolerance, then modify the tranche rates to reflect the yields and loop again.
        else:
            oldTrancheRate = newTrancheRate
            for a, tranche in enumerate(structured_securities.tranches):
                tranche.rate = newTrancheRate[a]

    letter_rating_A=convert_rating(A[0])
    letter_rating_B=convert_rating(B[0])

    A=list(A)
    B=list(B)

    A.insert(1,letter_rating_A)
    B.insert(1,letter_rating_B)

    A.append(newTrancheRate[0])
    B.append(newTrancheRate[1])

    A=tuple(A)
    B=tuple(B)

    # DIRR, Rating, WAL, and rate of each tranche
    return [A, B]


@memoize
def doWork(input, output):  # 2 parameters input queue and output queue

    # f is the function simulateWaterfall()
    # args in this case is (loan_pool, structured_securities, int(NSIM/numProcesses) from the input_queue
    f, args = input.get(timeout=1)

    res = f(*args)  # call f() with the list of arguments

    output.put(res)  # get the result from f() and put it on the output queue





@memoize
def runSimulationParallel(loan_pool, structured_securities, NSIM, numProcesses):

    # In this case, output contains the results from the function

    # Create a Queue type object, anything can be added to the queue
    # and communicate to each other
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()
    sub_sim=int(NSIM/numProcesses)

    process=[]


    for i in range(numProcesses):
        input_queue.put((simulateWaterfall,(loan_pool, structured_securities, sub_sim)))


    for i in range(numProcesses):

        # target = doWork() is the function you want the process to call
        # args = arguments to get passed to the target = doWork()

        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()
        process.append(p)




    # As soon as the process is started, the target = doWork() function gets called

    # Create an infinite loop and monitor output queue
    res = []



    while True:
        # Take something off the queue, if queue has nothing, it will block (wait)
        # until the queue has something, while other processes running in the background
        # when it has something, add it to the list res = []


        if len(res)!=numProcesses*2:
            r = output_queue.get()
            res.extend(r)
        else:

            # When it's done, break the loop
            break


    tranche_a_res=[res[a] for a in range(len(res)) if a%2==0]
    tranche_b_res = [res[b] for b in range(len(res)) if b % 2 != 0]

    #Once the output Queue monitoring loop completes, aggregate and average the resulting tranche metrics from each process
    sum_dirr_a=sum([tranche_a_res[x][0] for x in range(len(tranche_a_res))])
    sum_AL_a=sum([tranche_a_res[x][1] for x in range(len(tranche_a_res))])

    sum_dirr_b = sum([tranche_b_res[x][0] for x in range(len(tranche_b_res))])
    sum_AL_b = sum([tranche_b_res[x][1] for x in range(len(tranche_b_res))])

    result=[(sum_dirr_a/len(tranche_a_res),sum_AL_a/len(tranche_a_res)), (sum_dirr_b/len(tranche_b_res),sum_AL_b/len(tranche_b_res))]

    #Every spawned process should be stopped when finished with it.
    for x in process:

        #You can call join on the process
        x.join()
        x.terminate()


    return result