#Student Name: Jianwei Su
#Date: 05/26/2022
#Level 7

import numpy as np
from doWaterfall import doWaterfall
from utils.timer import timer
from utils.memoize import memoize


# Create a global function called simulateWaterfall. Its input parameters should be a LoanPool, a
# StructuredSecurities object, and NSIM. NSIM specifies the number of simulations to run, and will be
# used to tell your loop how many times to iterate.

#@timer
def simulateWaterfall(loan_pool, StructuredSecurities, NSIM):

    dirr_tranche_A = []
    dirr_tranche_B = []
    AL_tranche_A = []
    AL_tranche_B = []

    irr_tranche_A=[]
    irr_tranche_B=[]

    for a in range(NSIM):
        #loan_pool.reset()
        #StructuredSecurities.reset()

        _, _, metrics = doWaterfall(loan_pool, StructuredSecurities)


        dirr_A= metrics[0][1]
        dirr_B=metrics[1][1]
        AL_A=metrics[0][3]
        AL_B = metrics[1][3]


        if not np.isnan(metrics[0][1]):
            dirr_tranche_A.append(dirr_A)

        if not np.isnan(metrics[1][1]):
            dirr_tranche_B.append(dirr_B)


        if AL_A is not None:
            AL_tranche_A.append(AL_A)

        if AL_B is not None:
            AL_tranche_B.append(AL_B)


    # Once NSIM iterations are complete, take the average of all the DIRR and AL values.
    Metrics=[(np.mean(dirr_tranche_A), np.mean(AL_tranche_A)),
             (np.mean(dirr_tranche_B), np.mean(AL_tranche_B))]

    return Metrics



