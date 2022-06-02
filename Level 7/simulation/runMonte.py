#Student Name: Jianwei Su
#Date: 05/27/2022
#Level 7

import numpy as np
from simulation.simulateWaterfall import simulateWaterfall
from utils.timer import timer
import numpy as np







def calculateYield(DIRR, WAL):

    return ((7 / (1 + .08 * np.exp(-0.19 * WAL / 12))) + 0.19 * np.sqrt((WAL / 12) * DIRR * 100)) / 100


def new_tranche_rate(old_rate, yield_rate, coeff):

    return old_rate + coeff * (yield_rate - old_rate)

# 𝑛𝐴 𝑖𝑠 𝑇𝑟𝑎𝑛𝑐ℎ𝑒 𝐴 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙,
# 𝑛𝐵 𝑖𝑠 𝑇𝑟𝑎𝑛𝑐ℎ𝑒 𝐵 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙,
# 𝑁 𝑖𝑠 𝑡ℎ𝑒 𝑡𝑜𝑡𝑎𝑙 𝑛𝑜𝑡𝑖𝑜𝑛𝑎𝑙.
def Diff(nA, nB, lastArate, lastBrate, newArate, newBrate):

    N= nA+nB
    diff = (nA * abs((lastArate - newArate) / lastArate) + nB * abs((lastBrate - newBrate) / lastBrate)) / N
    return diff


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




def runMonte(loan_pool, structured_securities, tolerance, NSIM):


    oldTrancheRate = [tranche.rate for tranche in structured_securities.tranches]
    Tranchenotional= [tranche.notional for tranche in structured_securities.tranches]



    # coeff is 1.2 for Tranche A and 0.8 for Tranche B
    coff_list=[1.2, 0.8]

    while True:

        Metrics= simulateWaterfall(loan_pool, structured_securities, NSIM)
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




