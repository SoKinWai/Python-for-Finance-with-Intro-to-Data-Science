#Student Name: Jianwei Su
#Date: 05/22/2022
#7.1.4



import logging
from loan.loan_pool import LoanPool
from tranche.structured_securities import StructuredSecurities
from utils.memoize import memoize


#This function should take two parameters:
# A LoanPool object and a StructuredSecurities object
@memoize
def doWaterfall(loan_pool, tranches):
    loan_pool.reset()
    tranches.reset()

    #The function should loop through time periods, starting from 0
    time_period=0

    loanpool_waterfall=[]
    structured_security_waterfall=[]


    #Keep going until the LoanPool has no more active loans (no more payments coming from the LoanPool)
    while loan_pool.active_loans(time_period):

        #Increase the time period on the StructuredSecurities object (which will, in turn, increase for all the tranches).
        tranches.increaseTranchesTimePeriod()
        time_period+=1


        recovery_amount = loan_pool.checkDefaults(time_period)


        #Ask the LoanPool for its total payment for the current time period.
        tranches.loanpool=loan_pool
        collections=loan_pool.Total_monthlyPayment(time_period)+recovery_amount


        #Pay the StructuredSecurities with the amount provided by the LoanPool.
        tranches.makePayments(collections)

        #Call getWaterfall on both the LoanPool and StructuredSecurities objects and save the info into two variables
        loanpool_waterfall.append(loan_pool.getWaterfall(time_period))
        structured_security_waterfall.append(tranches.getWaterfall(time_period))

        # save tranche DIRR and ALL as a list in metrics
        metrics = [[tranche.IRR(), tranche.DIRR(), tranche.DIRR_Letter(),tranche.AL()] for tranche in tranches.tranches]

    return [loanpool_waterfall,structured_security_waterfall, metrics]